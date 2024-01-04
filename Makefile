EXECUTABLE_NAME = DYGTube-v5.0.0-x86_64

PYINSTALLER_CMD = pyinstaller

PYINSTALLER_FLAGS = --onefile --noconsole --windowed

MAIN_FILE = main.py

build:
	$(PYINSTALLER_CMD) --name $(EXECUTABLE_NAME) $(PYINSTALLER_FLAGS) $(MAIN_FILE)

clean:
	rm -rf build dist __pycache__ $(EXECUTABLE_NAME).spec

.PHONY: build clean
