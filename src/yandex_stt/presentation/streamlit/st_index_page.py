import streamlit as st
from typing import BinaryIO

from yandex_stt.application.recognize_stt_interactor import RecognizeSTTInteractor


def display_dummy_text() -> None:
    """Displays welcome message and app description."""
    st.title("🎈 My Speech to Text app")
    st.write("Let's start recognizing speech to text! [docs.streamlit.io](https://docs.streamlit.io/).")


def display_input_audio_form(interactor: RecognizeSTTInteractor) -> None:
    """Displays file upload form with submit button for audio recognition."""
    with st.form(key='audio_form'):
        uploaded_file: BinaryIO | None = st.file_uploader(
            "Choose an audio file",
            type=['wav', 'mp3', 'ogg', 'flac'],
            help="Upload an audio file to transcribe speech to text"
        )
        submit_button: bool = st.form_submit_button(label='Submit', use_container_width=True)

        if submit_button:
            if uploaded_file is not None:
                with st.spinner('Recognizing speech...'):
                    try:
                        result: str = interactor.execute(uploaded_file)
                        st.success('Recognition completed!')
                        st.text_area(
                            "Recognized Text",
                            value=result,
                            height=200,
                            disabled=False
                        )
                    except Exception as e:
                        st.error(f'Error during recognition: {str(e)}')
            else:
                st.warning('Please upload a file before submitting.')
