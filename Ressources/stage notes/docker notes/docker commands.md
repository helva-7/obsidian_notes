#docker 
# docker run 
- the `-it` argument in `docker run`  is used to make the container interactive and give it a terminal which means type commands inside of the container 
- the `docker run` runs a container from the image given , if its not on the host it pulls it for only one time from the docker hub and then preserves it 
- `docker run [image] sleep 5 `: since containers lives as long as there is a running process inside of it and it exits immediately, you can run a sleep process 5 seconds for example and then exits  
- the `-d` is to run the container at the background and go back to your prompt immediately 
# docker ps 
- the docker ps command lists all running containers on the machine and some basic info about them  
- the `-a` argument shows all the running and non running containers on the machine 
# docker stop
- to stop a running container use the `docker stop` command + the container ID or the container name in the stop command 
# docker rm
- this command is used to remove the container from the machine 
# docker rmi 
- to remove an image from the machine 
# docker pull [image]
- to download an image on the machine 
# docker exec
- we use this command when we want to run a command on a running container => `docker exec [container's name] [command ...]`
# docker attach 
- this command is used to attach back to a running container on the background when using the `docker run -d` command 
# docker container prune 
- this command delete all the stopped containers 
