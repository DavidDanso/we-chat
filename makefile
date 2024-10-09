build_image:
	docker build -t we-chat-image .

run_container:
	docker run -d --name we-chat-container -p 9001:9000 we-chat-image 