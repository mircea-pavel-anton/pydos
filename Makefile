run:
	@python3 src/main.py

sample:
	@python3 src/sample/sample.py

clean:
	@rm -rf bin include lib lib64 share pyvenv.cfg

venv:
	@python3 -m venv .
	@echo "Virtual environment created. Activate it by running: source bin/activate"

install:
	pip install -r requirements.txt