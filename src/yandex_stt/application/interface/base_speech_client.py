from typing import Protocol


class BaseSpeechClient(Protocol):
    """Protocol defining the interface for speech recognition clients."""

    def recognize(self, audio_path: str) -> str:
        """Recognizes speech from audio file and returns transcribed text."""
        ...
