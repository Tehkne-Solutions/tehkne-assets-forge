from __future__ import annotations

import json
from pathlib import Path

import pytest

from tehkne_assets_forge.hoc_landmarks import HocLandmarkError, validate_hoc_landmark_manifest


def write_manifest(root: Path, assets: list[dict[str, str]]) -> Path:
    manifest = root / "pack-manifest.json"
    manifest.write_text(
        json.dumps(
            {
                "schema": "hoc/world-landmarks/v1",
                "project": "Hexa Octarina Conquer",
                "signature": "Tehkné Solutions",
                "assets": assets,
            }
        ),
        encoding="utf-8",
    )
    return manifest


def required_assets() -> list[dict[str, str]]:
    return [
        {"id": "LANDMARK_CITY_NEUTRAL_01", "role": "city", "file": "art/city-neutral.png"},
        {"id": "LANDMARK_MINE_NEUTRAL_01", "role": "mine", "file": "art/mine-neutral.png"},
    ]


def test_hoc_landmark_manifest_accepts_required_neutral_pair(tmp_path: Path) -> None:
    art = tmp_path / "art"
    art.mkdir()
    (art / "city-neutral.png").write_bytes(b"city")
    (art / "mine-neutral.png").write_bytes(b"mine")
    result = validate_hoc_landmark_manifest(write_manifest(tmp_path, required_assets()), root=tmp_path)
    assert result["valid"] is True
    assert result["asset_count"] == 2


def test_hoc_landmark_manifest_rejects_missing_mine(tmp_path: Path) -> None:
    manifest = write_manifest(tmp_path, [required_assets()[0]])
    with pytest.raises(HocLandmarkError, match="LANDMARK_MINE_NEUTRAL_01"):
        validate_hoc_landmark_manifest(manifest)


def test_hoc_landmark_manifest_rejects_ui_semantics(tmp_path: Path) -> None:
    assets = required_assets()
    assets[0] = {"id": "LANDMARK_CITY_NEUTRAL_01", "role": "city", "file": "icons/city-marker.png"}
    manifest = write_manifest(tmp_path, assets)
    with pytest.raises(HocLandmarkError, match="forbidden world-space semantics"):
        validate_hoc_landmark_manifest(manifest)


def test_hoc_landmark_manifest_rejects_semantic_role_mismatch(tmp_path: Path) -> None:
    assets = required_assets()
    assets[0] = {"id": "LANDMARK_CITY_NEUTRAL_01", "role": "mine", "file": "art/city.png"}
    manifest = write_manifest(tmp_path, assets)
    with pytest.raises(HocLandmarkError, match="family/role mismatch"):
        validate_hoc_landmark_manifest(manifest)


def test_hoc_landmark_manifest_rejects_empty_renderable(tmp_path: Path) -> None:
    art = tmp_path / "art"
    art.mkdir()
    (art / "city-neutral.png").write_bytes(b"")
    (art / "mine-neutral.png").write_bytes(b"mine")
    manifest = write_manifest(tmp_path, required_assets())
    with pytest.raises(HocLandmarkError, match="missing or empty"):
        validate_hoc_landmark_manifest(manifest, root=tmp_path)
