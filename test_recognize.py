import os
import sys
from pathlib import Path
from dotenv import load_dotenv

from src.yandex_stt.adapter.yandex_speech_client import YandexSpeechClient


def main() -> None:
    load_dotenv()
    api_key: str = os.getenv('YANDEX_AI_STUDIO_API_KEY', '')
    if not api_key:
        print("Error: YANDEX_AI_STUDIO_API_KEY environment variable is not set")
        print("Please set it with: export YANDEX_AI_STUDIO_API_KEY='your_api_key'")
        sys.exit(1)

    audio_path: Path = Path('assets/russian_speech.wav')
    if not audio_path.exists():
        print(f"Error: Audio file not found at {audio_path}")
        sys.exit(1)

    print(f"Initializing YandexSpeechClient...")
    client = YandexSpeechClient(api_key=api_key)

    print(f"Recognizing speech from {audio_path}...")
    try:
        recognized_text: str = client.recognize(str(audio_path))
        print(f"\nRecognized text: {recognized_text}")
    except Exception as e:
        print(f"\nError during recognition: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
