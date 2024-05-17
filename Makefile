.PHONY: all
.DEFAULT: all
all: pwn install

.PHONY: clean
clean:
	rm -rf pwn

pwn:
	python3 -m venv $@

.PHONY: install
install: requirements.txt
	. pwn/bin/activate && pip3 install --upgrade pip
	. pwn/bin/activate && pip3 install -r $<
	echo "source pwn/bin/activate"
