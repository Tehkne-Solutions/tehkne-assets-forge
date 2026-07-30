from __future__ import annotations

import argparse
import json
from pathlib import Path

from . import __version__
from .budget import AssetBudget, evaluate_budget, scan_disk_metrics
from .checksums import ChecksumError, sha256_file, verify_sha256
from .intake import IntakeError, extract_zip_intake


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="tehkne-assets-forge")
    parser.add_argument("--version", action="version", version=__version__)
    sub = parser.add_subparsers(dest="command", required=True)

    validate = sub.add_parser("validate-catalog", help="Valida um catálogo de packs.")
    validate.add_argument("catalog", type=Path)

    checksum = sub.add_parser("checksum", help="Calcula SHA-256 de um arquivo.")
    checksum.add_argument("file", type=Path)

    verify = sub.add_parser("verify-checksum", help="Valida o SHA-256 esperado.")
    verify.add_argument("file", type=Path)
    verify.add_argument("expected")

    intake = sub.add_parser("inspect-zip", help="Inspeciona um ZIP em intake seguro.")
    intake.add_argument("archive", type=Path)
    intake.add_argument("--max-files", type=int, default=1000)
    intake.add_argument("--max-uncompressed-bytes", type=int, default=512 * 1024 * 1024)

    budget = sub.add_parser("check-budget", help="Valida orçamento básico de uma pasta.")
    budget.add_argument("root", type=Path)
    budget.add_argument("--max-files", type=int)
    budget.add_argument("--max-disk-bytes", type=int)
    return parser


def validate_catalog(path: Path) -> dict[str, object]:
    if not path.is_file():
        raise FileNotFoundError(f"Catálogo não encontrado: {path}")

    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("A raiz do catálogo deve ser um objeto JSON.")
    if data.get("schema") != "taijifu/asset-vault-catalog/v1":
        raise ValueError("Schema de catálogo não suportado.")
    if not isinstance(data.get("packs"), list):
        raise ValueError("O campo 'packs' deve ser uma lista.")

    required = {"pack_id", "version", "release_tag", "filename", "status"}
    for index, pack in enumerate(data["packs"]):
        if not isinstance(pack, dict):
            raise ValueError(f"Pack #{index} deve ser um objeto JSON.")
        missing = sorted(required - set(pack))
        if missing:
            raise ValueError(f"Pack #{index} sem campos: {', '.join(missing)}")

    return {"valid": True, "packs": len(data["packs"])}


def run(args: argparse.Namespace) -> tuple[int, dict[str, object]]:
    if args.command == "validate-catalog":
        return 0, validate_catalog(args.catalog)
    if args.command == "checksum":
        return 0, {"valid": True, "file": str(args.file), "sha256": sha256_file(args.file)}
    if args.command == "verify-checksum":
        digest = verify_sha256(args.file, args.expected)
        return 0, {"valid": True, "file": str(args.file), "sha256": digest}
    if args.command == "inspect-zip":
        with extract_zip_intake(
            args.archive,
            max_files=args.max_files,
            max_uncompressed_bytes=args.max_uncompressed_bytes,
        ) as intake:
            files = sorted(str(path.relative_to(intake)).replace("\\", "/") for path in intake.rglob("*") if path.is_file())
        return 0, {"valid": True, "archive": str(args.archive), "files": files, "file_count": len(files)}
    if args.command == "check-budget":
        metrics = scan_disk_metrics(args.root)
        result = evaluate_budget(
            metrics,
            AssetBudget(max_files=args.max_files, max_disk_bytes=args.max_disk_bytes),
        )
        return (0 if result.passed else 3), result.to_dict()
    return 1, {"valid": False, "error": "Comando não suportado."}


def main() -> int:
    args = build_parser().parse_args()
    try:
        code, payload = run(args)
    except (OSError, ValueError, json.JSONDecodeError, ChecksumError, IntakeError) as exc:
        code, payload = 2, {"valid": False, "error": str(exc)}
    print(json.dumps(payload, ensure_ascii=False, sort_keys=True))
    return code


if __name__ == "__main__":
    raise SystemExit(main())
