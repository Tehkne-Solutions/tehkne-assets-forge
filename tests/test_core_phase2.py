from __future__ import annotations

import hashlib
import zipfile
from pathlib import Path

import pytest

from tehkne_assets_forge.budget import AssetBudget, AssetMetrics, evaluate_budget
from tehkne_assets_forge.checksums import ChecksumError, verify_sha256
from tehkne_assets_forge.intake import IntakeError, extract_zip_intake


def test_checksum_validation(tmp_path: Path) -> None:
    target = tmp_path / "asset.bin"
    target.write_bytes(b"taijifu")
    expected = hashlib.sha256(b"taijifu").hexdigest()
    assert verify_sha256(target, expected) == expected
    with pytest.raises(ChecksumError):
        verify_sha256(target, "0" * 64)


def test_safe_intake(tmp_path: Path) -> None:
    archive = tmp_path / "pack.zip"
    with zipfile.ZipFile(archive, "w") as bundle:
        bundle.writestr("manifest.json", "{}")
    with extract_zip_intake(archive) as intake:
        assert (intake / "manifest.json").is_file()


def test_rejects_zip_slip(tmp_path: Path) -> None:
    archive = tmp_path / "unsafe.zip"
    with zipfile.ZipFile(archive, "w") as bundle:
        bundle.writestr("../escape.txt", "blocked")
    with pytest.raises(IntakeError):
        with extract_zip_intake(archive):
            pass


def test_budget_contract() -> None:
    result = evaluate_budget(
        AssetMetrics(files=181, disk_bytes=1024),
        AssetBudget(max_files=180, max_disk_bytes=2048),
    )
    assert result.passed is False
    assert result.to_dict()["schema"] == "tehkne/asset-budget-report/v1"
    assert result.violations == ("files: 181 exceeds 180",)
