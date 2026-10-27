"""Phase 0: verify the Python environment is ready.

Run from the project root:  python scripts/00_check_env.py
"""
import importlib
import platform
import sys
from pathlib import Path

PACKAGES = [
    "numpy", "scipy", "pandas", "sklearn", "nibabel",
    "nilearn", "matplotlib", "seaborn", "joblib", "requests",
]


def main() -> int:
    print(f"Python {platform.python_version()} on {platform.system()}")
    if sys.version_info < (3, 10):
        print("WARNING: Python 3.10+ is recommended.")

    failed = []
    for name in PACKAGES:
        try:
            module = importlib.import_module(name)
            print(f"  OK   {name:<12} {getattr(module, '__version__', '?')}")
        except ImportError:
            print(f"  FAIL {name:<12} not installed")
            failed.append(name)

    root = Path(__file__).resolve().parents[1]
    for folder in ("data", "literature", "scripts", "results"):
        (root / folder).mkdir(exist_ok=True)
    print(f"Project folders OK under {root}")

    if failed:
        print("\nMissing:", ", ".join(failed))
        print("Fix with: pip install -r requirements.txt")
        return 1
    print("\nEnvironment is ready.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
