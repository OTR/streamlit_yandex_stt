import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from yandex_stt.application.interface.base_speech_client import BaseSpeechClient

# Add src directory to Python path
src_path: Path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from yandex_stt.adapter.sync_yandex_speech_client import SyncYandexSpeechClient


def main() -> None:
    load_dotenv()
    audio_file: Path = Path(__file__).parent.parent / "assets" / "russian_speech.wav"

    if not audio_file.exists():
        print(f"Error: Audio file not found at {audio_file}")
        sys.exit(1)

    print(f"Loading audio file: {audio_file}")
    print(f"Audio file size: {audio_file.stat().st_size / 1024:.2f} KB")

    print("\nInitializing SyncYandexSpeechClient...")
    print("(Reading API key from .env file: YANDEX_AI_STUDIO_API_KEY)")

    try:
        api_key: str = os.getenv('YANDEX_AI_STUDIO_API_KEY', '')
        client: BaseSpeechClient = SyncYandexSpeechClient(api_key=api_key)
        print("✓ Client initialized successfully")

        print(f"\nRecognizing speech from {audio_file.name}...")
        print("This may take a moment...")
        result: str = client.recognize(str(audio_file))

        print("\n" + "=" * 80)
        print("RECOGNITION RESULT:")
        print("=" * 80)
        print(result)
        print("=" * 80)
        print(f"\n✓ Recognition completed successfully!")
        print(f"Recognized text length: {len(result)} characters")

    except ValueError as e:
        if "YANDEX_AI_STUDIO_API_KEY" in str(e):
            print(f"\n✗ Configuration Error: {e}")
            print("\nPlease ensure your .env file contains:")
            print("  YANDEX_AI_STUDIO_API_KEY=your_api_key_here")
            sys.exit(1)
        else:
            raise
    except Exception as e:
        print(f"\n✗ Error during recognition: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
