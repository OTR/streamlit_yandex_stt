import sys
from pathlib import Path

# Add src directory to Python path for imports
src_path: Path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

# Import and run the main application
import yandex_stt.main
