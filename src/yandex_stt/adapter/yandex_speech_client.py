import os
from pathlib import Path
from dotenv import load_dotenv
from speechkit import model_repository, configure_credentials, creds
from speechkit.stt import AudioProcessingType


class YandexSpeechClient:
    def __init__(self, api_key: str | None = None) -> None:
        if api_key is None:
            api_key = os.getenv('YANDEX_AI_STUDIO_API_KEY')
            if api_key is None:
                project_root: Path = Path(__file__).parent.parent.parent.parent
                env_path: Path = project_root / '.env'
                load_dotenv(env_path)
                api_key = os.getenv('YANDEX_AI_STUDIO_API_KEY')
                if api_key is None:
                    raise ValueError(f'YANDEX_AI_STUDIO_API_KEY not found in environment or .env file at {env_path}')
        
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
