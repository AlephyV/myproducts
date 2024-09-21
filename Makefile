VENV = .venv
MAIN = main.py
REQUIREMENTS = requirements.txt
TESTS = tests/

run:
	uvicorn app.main:app --reload