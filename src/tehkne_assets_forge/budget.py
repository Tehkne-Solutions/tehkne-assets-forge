from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path


@dataclass(frozen=True)
class AssetBudget:
    max_files: int | None = None
    max_disk_bytes: int | None = None
    max_rgba_bytes: int | None = None
    max_dimension: int | None = None
    max_frames: int | None = None
    max_draw_calls: int | None = None


@dataclass(frozen=True)
class AssetMetrics:
    files: int
    disk_bytes: int
    rgba_bytes: int = 0
    max_dimension: int = 0
    frames: int = 0
    draw_calls: int = 0


@dataclass(frozen=True)
class BudgetResult:
    passed: bool
    metrics: AssetMetrics
    limits: AssetBudget
    violations: tuple[str, ...]

    def to_dict(self) -> dict[str, object]:
        return {
            "schema": "tehkne/asset-budget-report/v1",
            "passed": self.passed,
            "metrics": asdict(self.metrics),
            "limits": asdict(self.limits),
            "violations": list(self.violations),
        }


def scan_disk_metrics(root: str | Path) -> AssetMetrics:
    base = Path(root)
    if not base.is_dir():
        raise NotADirectoryError(base)
    files = [path for path in base.rglob("*") if path.is_file()]
    return AssetMetrics(files=len(files), disk_bytes=sum(path.stat().st_size for path in files))


def evaluate_budget(metrics: AssetMetrics, limits: AssetBudget) -> BudgetResult:
    violations: list[str] = []
    checks = (
        ("files", metrics.files, limits.max_files),
        ("disk_bytes", metrics.disk_bytes, limits.max_disk_bytes),
        ("rgba_bytes", metrics.rgba_bytes, limits.max_rgba_bytes),
        ("max_dimension", metrics.max_dimension, limits.max_dimension),
        ("frames", metrics.frames, limits.max_frames),
        ("draw_calls", metrics.draw_calls, limits.max_draw_calls),
    )
    for name, actual, maximum in checks:
        if maximum is not None and actual > maximum:
            violations.append(f"{name}: {actual} exceeds {maximum}")
    return BudgetResult(not violations, metrics, limits, tuple(violations))
