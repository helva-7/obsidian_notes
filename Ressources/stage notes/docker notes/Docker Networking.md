## Default networks 
 - when we install docker , it creates three networks automatically . **bridge**, **none** and **host** / bridge is the default network a container gets attached to , if you would like to associate the container to a network use the command 

```
docker run [container] --network= (none or host)
```
- the bridge network is a private internal network created by docker on the host , all the containers are attached to this network . containers get ip addresses and they can communicate with other containers on this internal network ; to access any container from outside , map the ports of the container on the docker host  or associate the container to the **host network** 
- on the none network , a container is not attach to any network . they are in an isolated network 

## User-defined Network
- if we want to isolate the containers within the docker host ,per example two containers on one the network 172 and other two on the network 182 . since docker create only one bridge , we can create out internal network using the command 
```
docker network create \ --driver [driver] \ --subnet [subnet address] [network name]
```
- run this command to list all networks 
```
docker network ls 
```
## Inspect Network 

- to inspect the network part of a container , run the docker inspect (container) and see it on the "Networks" section 
## Embedded DNS 
- containers can reach each other using their names .per example if i have web server and an mysql database container , the best practice is to use its name since it exists an internal DNS server that creates separate namespaces and attach container's name to its address , and it uses virtual ethernet pairs to connect containers together 