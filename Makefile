all:
	docker build -t workstartendbot .

zip:
	docker run -v "${PWD}/build":/var/task/build workstartendbot

clean:
	rm -rf build
