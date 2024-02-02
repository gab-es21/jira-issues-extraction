.PHONY: venv activate install requirements

venv:
    python -m venv venv

activate: venv
    .\venv\Scripts\activate

install: activate
    pip install -r requirements.txt

requirements: activate
    pip freeze > requirements.txt
    @echo "Updated requirements.txt"

