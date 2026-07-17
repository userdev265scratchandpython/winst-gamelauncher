import importlib
from pathlib import Path

for file in Path(__file__).parent.glob("*.py"):
    if file.name in ("__init__.py",):
        continue

    name = file.stem

    module = importlib.import_module(f"{__name__}.{name}")

    globals()[name] = module
module = ""
