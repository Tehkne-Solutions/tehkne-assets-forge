from __future__ import annotations

import argparse
import json
from pathlib import Path

from . import __version__


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="tehkne-assets-forge")
    parser.add_argument("--version", action="version", version=__version__)
    sub = parser.add_subparsers(dest="command", required=True)

    validate = sub.add_parser("validate-catalog", help="Valida um catálogo de packs.")
    validate.add_argument("catalog", type=Path)
    return parser


def validate_catalog(path: Path) -> int:
    if not path.is_file():
        raise FileNotFoundError(f"Catálogo não encontrado: {path}")

    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("schema") != "taijifu/asset-vault-catalog/v1":
        raise ValueError("Schema de catálogo não suportado.")
    if not isinstance(data.get("packs"), list):
        raise ValueError("O campo 'packs' deve ser uma lista.")

    required = {"pack_id", "version", "release_tag", "filename", "status"}
    for index, pack in enumerate(data["packs"]):
        missing = sorted(required - set(pack))
        if missing:
            raise ValueError(f"Pack #{index} sem campos: {', '.join(missing)}")

    print(json.dumps({"valid": True, "packs": len(data["packs"])}, ensure_ascii=False))
    return 0


def main() -> int:
    args = build_parser().parse_args()
    try:
        if args.command == "validate-catalog":
            return validate_catalog(args.catalog)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(json.dumps({"valid": False, "error": str(exc)}, ensure_ascii=False))
        return 2
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
