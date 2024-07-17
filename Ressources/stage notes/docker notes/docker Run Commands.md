#docker

# docker Run -tag 
- we use it when we want to specify a version of the container we want to run seperated by a " : " , this is called a tag ,if the tag is not defined its considered as to be "latest" 

# docker run -STDIN 
- to run a container that has an app that needs inputs  
- to make it interactive so we can add an input , we use the -i "input" argument and the -t "pseudo terminal" argument which the command became `docker run -it  [container]` , then it prints the prompt and waits for an input

## Docker run -PORT mapping 
- *note : docker host == docker engine / the containers run inside of the docker host 
-  when running an app on a docker engine , it listens to a port per example 5000 , but the ip address that we gonna use is the issue ; there is two options 
  1. to use the ip of the docker container since every docker container gets an IP assigned by default , the internal ip address is accessible only within the docker host . the issue is that the users outside of the docker host cannot access it using this ip 
  2. we can use the ip address of the docker host to be accessible from outside , but that to work you must have mapped the port inside the docker **container** to a free port on the docker **host** for example to if i want the users to access my application through port 80 of my docker host , i could map the port 80 of local host (my computer) to port 5000 on the docker container 
 ```
  docker run -p 80:5000 [container] 
```
this way you can run multiples instances of your app or **different** apps and map them to different ports on the dockers host 
## Docker run -volume mapping (data persistence)
- for example, letss say you were to run a MYSQL container . when databases and tables are created , the data files are stored in location "/var/lib/mysql" inside of the docker container and any changes happen inside of the container . if u delete the mysql container , all the data inside of it get blown . if you would like to persist data , you would want to map a directory outside the container on the docker host   
```
docker run -v  (directory on host):(directory on container) [container]
```
- if u would like to see additional details about a specific container , use 

```
docker inspect [container name or id]
```

## container logs
- the logs are the contents written to the standard out of that container 
```
docker logs [container name or id]
```