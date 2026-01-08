# 🎈 Yandex speech to text showcase

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://speech.streamlit.app/)

### How to run it on your own machine

1. Install dependencies using `uv sync`


2. Run the app `uv run streamlit run streamlit_app.py`

   Or activate the virtual environment and run directly:

   ```bash
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   streamlit run streamlit_app.py
   ```

### Managing dependencies

The `requirements.txt` file is automatically generated from the `uv.lock` file using:
```bash
uv export --format requirements-txt --no-hashes -o requirements.txt
```
