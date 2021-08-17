install:
	pip install --upgrade pip && pip install -r requirements.txt
	pip install pipwin
	pipwin install pyaudio
lint:
	py -m pylint app.py

test:
	python -m pytest -vv

all:
	install lint test
