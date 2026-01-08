from speechkit import model_repository, configure_credentials, creds
from speechkit.stt import AudioProcessingType


class YandexSpeechClient:

    def __init__(self, api_key: str) -> None:
        configure_credentials(
            yandex_credentials=creds.YandexCredentials(
                api_key=api_key
            )
        )
        self.model = model_repository.recognition_model()
        self.model.model = 'general'
        self.model.language = 'ru-RU'
        self.model.audio_processing_type = AudioProcessingType.Full

    def recognize(self, audio_path: str) -> str:
        result = self.model.transcribe_file(audio_path)
        recognized_text: list[str] = []
        for res in result:
            recognized_text.append(res.normalized_text)
        return ' '.join(recognized_text)
