DOCKER_TAG=mark-calculator
build:
	docker build -t ${DOCKER_TAG} .

marks:
	docker run --rm  -v `pwd`:/src -it ${DOCKER_TAG} python main.py
