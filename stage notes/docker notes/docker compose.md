- we will start working with configurations in yaml files 
- if we want to set up complex application running multiple services , best practice is to use **docker compose** ; with docker compose we could create a configuration file in yaml format called ***docker-compose.yml*** 
	and put together the different services running them in this file 
- then we can use **docker-compose up** command to bring out all the application's stack , all changes are stored in the docker-compose file .all of this possible to do in only one docker host 
## Sample application to understand - voting app
![[Pasted image 20240708174326.png]]
- this is the sample application that will help  you understand docker , redis is an in memory storing db and postgres is used to persist the data collected
- lets set aside docker swarm services and see how we can put all thesse in a single docker host using only docker run command and docker host
- first of all , we gonna use the command 
```
- docker run -d --name=redis redis 
```
we used the -d to run this container in the background and named the container redis 
- then we gonna deploy the postgresql database by running this command
```
docker run -d --name=db postgres:9.4
```
- next we gonna start with the application services , with this command 
```
 docker run -d --name=vote -p 5000:80 voting-pp #name of the UI app image
```
- next we will deploy the results web app to the user 
```
docker run -d --name=result -p 5001:80
```
- finally we run an instance of the worker image 
- we got all the containers running but we didnt link them since the app wont work at all if we dont link them all ; this is when we use **Link**
- link is a command line option which can be used to link two containers together
- to link the voting-app and the redis instance , we gonna run this command instead
```
docker run -d --name=vote -p 5000:8à --link redis:redis voting-app #the first redis is the redis service and the second is the name of the container 
```
and these commands too 
![[Pasted image 20240708175957.png]]
![[Pasted image 20240708180036.png]]