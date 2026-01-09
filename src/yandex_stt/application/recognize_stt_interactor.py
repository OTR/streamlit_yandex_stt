from dataclasses import dataclass, field
from pathlib import Path
from typing import BinaryIO

from yandex_stt.adapter.yandex_speech_client import YandexSpeechClient


@dataclass
class RecognizeSTTInteractor:
    speech_client: YandexSpeechClient = field(repr=False)

    def execute(self, audio_file: BinaryIO) -> str:
        """Recognizes speech from uploaded audio file and returns transcribed text."""
        import tempfile
        import os

        with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as tmp_file:
            tmp_path: Path = Path(tmp_file.name)
            tmp_file.write(audio_file.read())
            tmp_file.flush()

            try:
                result: str = self.speech_client.recognize(str(tmp_path))
                return result
            finally:
                if tmp_path.exists():
                    os.unlink(tmp_path)
