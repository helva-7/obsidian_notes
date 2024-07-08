- in this section we going to see how docker stores data and how it manages file systems of the containers 
## File system
- when u install docker on a system , it creates this folder structure /var/lib/docker , this is where stores all its data by default (files related to images and containers running on the docker host)
## How does it stores its data?

- to understand that , we got to understand Docker's layered architecture (like we saw in docker images section) , which means every line on a dockerfile represents a layer and when a layer is built and an app restart or two apps uses common layers , it doesnt rebuild them . it reuses the same layers from the cache of the first application . this makes it easier to build and update fast and efficiently saves disk space  
	- these firs layers of an image is Read only layers once the image is built which means u cannot modify these layers only by initiating a new build . when u run a container based on this image , docker creates a container based off of these layers and create an additional layer on the of the image layers  . this layer is READ WRITE layer which means u can modify , store data created by the container .
	- once the container is destroyed , this layer and all of the changes are aslo destroyed  ,which means it only store data by default on the container layer 
	- in case i want to modify the image layers and before i can save this modified layers docker automatically creates a copy of a file in the container layer and then i will be able to modify it. all future modifications would be done on this copy of the file in the container layer ; this is calld **copy on write mechanism**. the data wont be modified on the image and at the deletion of the container , all of these data get removed . if we want to persist data  created by the container , we could add a persistent volume to the container
	- to use a volume , first of all we create this volume on the volume folder 
```
	- docker volume create volume_name
```
then when i run the docker container using docker run command , i could mount this volume inside docker container 
```
docker run -v volume_name:location [container]
```
![[Pasted image 20240708155220.png]]
	now all the data created is stored on the volume on the docker host , even if the container is destroyed the data is still active , this is called volume mounting 
 - to mount data to an  external storage at docker host , we use this command 
```
 - docker run -v /external/path/:/created/data container
```
this is called bind mounting , it mounts a directory from any location on the docker host  
- docker uses storage drivers to enable layered architecture 
