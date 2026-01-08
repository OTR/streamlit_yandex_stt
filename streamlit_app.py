import sys
from pathlib import Path

# Add src directory to Python path for imports
src_path: Path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

from yandex_stt.main import main


if __name__ == "__main__":
    main()
