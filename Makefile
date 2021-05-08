.PHONY: install
install:
	@echo "Creating virtual environment. You may need to install venv."
	python3 -m venv env; \
	source ./env/bin/activate; \
	pip3 install adafruit-circuitpython-neopixel; \
	pip3 install board; \
	pip3 install astral; \
	pip3 install -r src/requirements.txt;
	
.PHONY: run
run:
	@echo "Running program."
	sudo ./env/bin/python3 src/main.py;

.PHONY: reset
reset:
	@echo "Resetting leds."
	sudo ./env/bin/python3 src/reset.py;

.PHONY: test
test:
	@echo "Testing leds."
	sudo ./env/bin/python3 src/test.py;
