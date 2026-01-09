import streamlit as st

from yandex_stt.adapter.yandex_speech_client import YandexSpeechClient
from yandex_stt.application.recognize_stt_interactor import RecognizeSTTInteractor
from yandex_stt.bootstrap.config.settings import Settings
from yandex_stt.presentation.streamlit.st_index_page import display_dummy_text, display_input_audio_form


def main() -> None:
    settings: Settings = Settings()

    speech_client: YandexSpeechClient = YandexSpeechClient(api_key=settings.yandex_ai_studio_api_key)
    interactor: RecognizeSTTInteractor = RecognizeSTTInteractor(speech_client=speech_client)

    display_input_audio_form(interactor=interactor)
