from __future__ import annotations

import hashlib
from pathlib import Path


class ChecksumError(ValueError):
    """Raised when a file digest does not match the expected value."""


def sha256_file(path: str | Path, chunk_size: int = 1024 * 1024) -> str:
    target = Path(path)
    if not target.is_file():
        raise FileNotFoundError(target)

    digest = hashlib.sha256()
    with target.open("rb") as stream:
        while chunk := stream.read(chunk_size):
            digest.update(chunk)
    return digest.hexdigest()


def verify_sha256(path: str | Path, expected: str) -> str:
    normalized = expected.strip().lower()
    if len(normalized) != 64 or any(char not in "0123456789abcdef" for char in normalized):
        raise ValueError("expected SHA-256 must contain exactly 64 hexadecimal characters")

    actual = sha256_file(path)
    if actual != normalized:
        raise ChecksumError(f"checksum mismatch for {Path(path).name}: expected {normalized}, got {actual}")
    return actual
