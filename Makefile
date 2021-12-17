remove:
	docker rm -v -f sqrt_seq

build:
	docker build -t sqrt_seq .

tests: remove build
	docker run sqrt_seq python -m pytest tests.py