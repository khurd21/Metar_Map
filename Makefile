.PHONY: install
install:
	@echo "Creating virtual environment. You may need to install venv."
	virtualenv -p python3 env; \
	source ./env/bin/activate; \
	pip3 install -r src/requirements.txt;
	
.PHONY: run
run:
	@echo "Running program."
	sudo ./env/bin/python3 src/main.py;
