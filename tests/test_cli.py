from __future__ import annotations

import argparse
import hashlib
import json
import zipfile
from pathlib import Path

import pytest

from tehkne_assets_forge.cli import run, validate_catalog


def write_json(path: Path, value: object) -> None:
    path.write_text(json.dumps(value), encoding="utf-8")


def test_catalog_rejects_non_object_root(tmp_path: Path) -> None:
    catalog = tmp_path / "packs.json"
    write_json(catalog, [])
    with pytest.raises(ValueError, match="raiz"):
        validate_catalog(catalog)


def test_catalog_rejects_non_object_pack(tmp_path: Path) -> None:
    catalog = tmp_path / "packs.json"
    write_json(catalog, {"schema": "taijifu/asset-vault-catalog/v1", "packs": [None]})
    with pytest.raises(ValueError, match="Pack #0"):
        validate_catalog(catalog)


def test_checksum_command(tmp_path: Path) -> None:
    target = tmp_path / "asset.bin"
    target.write_bytes(b"forge")
    code, payload = run(argparse.Namespace(command="checksum", file=target))
    assert code == 0
    assert payload["sha256"] == hashlib.sha256(b"forge").hexdigest()


def test_inspect_zip_command(tmp_path: Path) -> None:
    archive = tmp_path / "pack.zip"
    with zipfile.ZipFile(archive, "w") as bundle:
        bundle.writestr("manifest.json", "{}")
    code, payload = run(
        argparse.Namespace(
            command="inspect-zip",
            archive=archive,
            max_files=10,
            max_uncompressed_bytes=1024,
        )
    )
    assert code == 0
    assert payload["files"] == ["manifest.json"]


def test_budget_command_returns_distinct_failure_code(tmp_path: Path) -> None:
    (tmp_path / "one.txt").write_text("1", encoding="utf-8")
    (tmp_path / "two.txt").write_text("2", encoding="utf-8")
    code, payload = run(
        argparse.Namespace(
            command="check-budget",
            root=tmp_path,
            max_files=1,
            max_disk_bytes=None,
        )
    )
    assert code == 3
    assert payload["passed"] is False
