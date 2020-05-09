all:
	docker build -t workstartendbot .

run:
	docker run -v "$PWD":/var/task workstartendbot

clean:
  
