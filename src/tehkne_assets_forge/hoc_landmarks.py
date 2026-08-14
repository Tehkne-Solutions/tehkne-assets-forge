from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

SIGNATURE = "Tehkné Solutions"
SCHEMA = "hoc/world-landmarks/v1"
REQUIRED_IDS = {"LANDMARK_CITY_NEUTRAL_01", "LANDMARK_MINE_NEUTRAL_01"}
FORBIDDEN_TOKENS = {
    "icon",
    "badge",
    "marker",
    "portrait",
    "card",
    "button",
    "frame",
    "hud",
    "logo",
    "emblem",
    "preview",
    "mask",
}
ALLOWED_EXTENSIONS = {".png", ".webp", ".jpg", ".jpeg", ".svg"}


class HocLandmarkError(ValueError):
    """Raised when a HOC world-landmark production manifest violates the contract."""


def _tokens(value: str) -> set[str]:
    return set(re.findall(r"[a-z0-9]+", value.lower()))


def _read_manifest(path: Path) -> dict[str, Any]:
    if not path.is_file():
        raise FileNotFoundError(path)
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise HocLandmarkError("manifest root must be a JSON object")
    return data


def validate_hoc_landmark_manifest(path: Path, *, root: Path | None = None) -> dict[str, Any]:
    data = _read_manifest(path)
    if data.get("schema") != SCHEMA:
        raise HocLandmarkError(f"unsupported schema: {data.get('schema')!r}")
    if data.get("project") != "Hexa Octarina Conquer":
        raise HocLandmarkError("project must be 'Hexa Octarina Conquer'")
    if data.get("signature") != SIGNATURE:
        raise HocLandmarkError("invalid institutional signature")

    assets = data.get("assets")
    if not isinstance(assets, list):
        raise HocLandmarkError("assets must be a list")

    ids: list[str] = []
    for index, asset in enumerate(assets):
        if not isinstance(asset, dict):
            raise HocLandmarkError(f"asset #{index} must be an object")
        asset_id = asset.get("id")
        role = asset.get("role")
        file_value = asset.get("file")
        if not isinstance(asset_id, str) or not asset_id:
            raise HocLandmarkError(f"asset #{index} has no canonical id")
        if role not in {"city", "mine"}:
            raise HocLandmarkError(f"{asset_id}: role must be city or mine")
        if not isinstance(file_value, str) or not file_value:
            raise HocLandmarkError(f"{asset_id}: file is required")

        forbidden = sorted(_tokens(" ".join((asset_id, role, file_value))) & FORBIDDEN_TOKENS)
        if forbidden:
            raise HocLandmarkError(f"{asset_id}: forbidden world-space semantics: {', '.join(forbidden)}")

        suffix = Path(file_value).suffix.lower()
        if suffix not in ALLOWED_EXTENSIONS:
            raise HocLandmarkError(f"{asset_id}: unsupported renderable extension {suffix!r}")

        if asset_id.startswith("LANDMARK_CITY_") and role != "city":
            raise HocLandmarkError(f"{asset_id}: canonical family/role mismatch")
        if asset_id.startswith("LANDMARK_MINE_") and role != "mine":
            raise HocLandmarkError(f"{asset_id}: canonical family/role mismatch")
        if not asset_id.startswith(("LANDMARK_CITY_", "LANDMARK_MINE_")):
            raise HocLandmarkError(f"{asset_id}: unsupported canonical landmark family")

        if root is not None:
            candidate = (root / file_value).resolve()
            root_resolved = root.resolve()
            if candidate != root_resolved and root_resolved not in candidate.parents:
                raise HocLandmarkError(f"{asset_id}: file escapes package root")
            if not candidate.is_file() or candidate.stat().st_size == 0:
                raise HocLandmarkError(f"{asset_id}: renderable file is missing or empty")

        ids.append(asset_id)

    if len(ids) != len(set(ids)):
        raise HocLandmarkError("duplicate canonical landmark ids")

    missing = sorted(REQUIRED_IDS - set(ids))
    if missing:
        raise HocLandmarkError(f"missing required neutral landmarks: {', '.join(missing)}")

    return {
        "valid": True,
        "schema": SCHEMA,
        "project": "Hexa Octarina Conquer",
        "asset_count": len(ids),
        "required_neutral_ids": sorted(REQUIRED_IDS),
        "signature": SIGNATURE,
    }
