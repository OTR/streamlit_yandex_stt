import os
import streamlit as st
from dotenv import load_dotenv

from yandex_stt.adapter.yandex_speech_client import YandexSpeechClient
from yandex_stt.application.recognize_stt_interactor import RecognizeSTTInteractor
from yandex_stt.presentation.streamlit.st_index_page import display_dummy_text, display_input_audio_form


def main() -> None:
    load_dotenv()
    # display_dummy_text()

    api_key: str = os.getenv('YANDEX_AI_STUDIO_API_KEY', '')
    if not api_key:
        st.error('YANDEX_AI_STUDIO_API_KEY environment variable is not set. Please configure it in your .env file.')
        return

    speech_client: YandexSpeechClient = YandexSpeechClient(api_key=api_key)
    interactor: RecognizeSTTInteractor = RecognizeSTTInteractor(speech_client=speech_client)

    display_input_audio_form(interactor=interactor)
