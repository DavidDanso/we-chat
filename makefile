# Clean up Docker system
clean_docker:
	docker system prune -a

build_image:
	docker build -t we-chat .

run_container:
	docker run -d --name we-chat-container -p 9001:9000 we-chat 

compose_up:
	docker compose up -d

compose_down:
	docker compose down


###### Push Your Image to ECR

# get login credentials
get_ecr_login:
	aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 474668428902.dkr.ecr.us-east-1.amazonaws.com

# Tag image for ECR:
tag_image:
	docker tag we-chat 474668428902.dkr.ecr.us-east-1.amazonaws.com/we-chat-repo

# Push the image to ECR
push_to_ecr:
	docker push 474668428902.dkr.ecr.us-east-1.amazonaws.com/we-chat-repo

# Add helpful commands for Docker management
stop_container:
	docker stop we-chat-container

remove_container:
	docker rm we-chat-container