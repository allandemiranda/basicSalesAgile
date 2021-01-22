# API FLASK

$ python3 -m venv venv

$ . venv/bin/activate

$ pip install requirements.txt

--> check database settings in `config.py`

$ python3 run.py db init

$ python3 run.py db migrate

$ python3 run.py db upgrade

$ python3 run.py runserver

# Test

$ python tests.py
