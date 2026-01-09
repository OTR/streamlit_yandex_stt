from pathlib import Path
from typing import BinaryIO

from yandex_stt.adapter.yandex_speech_client import YandexSpeechClient


class RecognizeSTTInteractor:
    """Handles speech-to-text recognition use case."""

    def __init__(self, speech_client: YandexSpeechClient) -> None:
        self._speech_client: YandexSpeechClient = speech_client

    def execute(self, audio_file: BinaryIO) -> str:
        """Recognizes speech from uploaded audio file and returns transcribed text."""
        import tempfile
        import os

        with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as tmp_file:
            tmp_path: Path = Path(tmp_file.name)
            tmp_file.write(audio_file.read())
            tmp_file.flush()

            try:
                result: str = self._speech_client.recognize(str(tmp_path))
                return result
            finally:
                if tmp_path.exists():
                    os.unlink(tmp_path)
