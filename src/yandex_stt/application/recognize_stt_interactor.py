from dataclasses import dataclass, field
from pathlib import Path
from typing import BinaryIO
import tempfile
import os

from yandex_stt.application.interface.base_speech_client import BaseSpeechClient


@dataclass
class RecognizeSTTInteractor:
    speech_client: BaseSpeechClient = field(repr=False)

    def execute(self, audio_file: BinaryIO) -> str:
        """Recognizes speech from uploaded audio file and returns transcribed text."""

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
