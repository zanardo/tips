.PHONY: all
all: README.md

.PHONY: README.md
README.md:
	@./index.py
