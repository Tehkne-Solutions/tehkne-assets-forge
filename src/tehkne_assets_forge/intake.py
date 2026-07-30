from __future__ import annotations

import shutil
import tempfile
import zipfile
from contextlib import contextmanager
from pathlib import Path
from typing import Iterator


class IntakeError(ValueError):
    """Raised when a source archive is unsafe or invalid."""


def _safe_member(root: Path, member: str) -> Path:
    destination = (root / member).resolve()
    if root.resolve() not in destination.parents and destination != root.resolve():
        raise IntakeError(f"unsafe archive path: {member}")
    return destination


@contextmanager
def extract_zip_intake(
    archive: str | Path,
    *,
    max_files: int = 1000,
    max_uncompressed_bytes: int = 512 * 1024 * 1024,
    keep: bool = False,
) -> Iterator[Path]:
    source = Path(archive)
    if not source.is_file():
        raise FileNotFoundError(source)

    temp_dir = Path(tempfile.mkdtemp(prefix="tehkne-assets-forge-"))
    try:
        with zipfile.ZipFile(source) as bundle:
            members = [item for item in bundle.infolist() if not item.is_dir()]
            if len(members) > max_files:
                raise IntakeError(f"archive has {len(members)} files; limit is {max_files}")
            total_size = sum(item.file_size for item in members)
            if total_size > max_uncompressed_bytes:
                raise IntakeError("archive exceeds the uncompressed size limit")
            for item in members:
                _safe_member(temp_dir, item.filename)
            bundle.extractall(temp_dir)
        yield temp_dir
    finally:
        if not keep:
            shutil.rmtree(temp_dir, ignore_errors=True)
