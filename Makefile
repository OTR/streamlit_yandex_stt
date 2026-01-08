.PHONY: test-recognize test-recognition help

help:
	@echo "Available targets:"
	@echo "  make test-recognize    - Run test_recognize.py"
	@echo "  make test-recognition  - Run test_recognition.py"

test-recognize:
	uv run python cli_tools/test_recognize.py

test-recognition:
	uv run python cli_tools/test_recognition.py
