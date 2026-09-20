import importlib
from pathlib import Path

if __name__ == "__main__":
    for file in sorted(Path("tests").glob("test_*.py")):
        module = importlib.import_module(f"tests.{file.stem}")
        for name, func in vars(module).items():
            if name.startswith("test_") and callable(func):
                func()
        print(f"Todos os testes passaram em: {file.name}")