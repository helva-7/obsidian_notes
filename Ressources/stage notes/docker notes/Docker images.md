- in this section we will see how to create your own image , but first of all we have to answer the question of "why would i need to create my own image?" , it could either be because you cannot find a component or a service only on docker hub ; or you and your team decided that the app will be dockerized for each shipping and deployment 
-  **how to create my own image ?** => first lets think what should i do if i want to deploy the application manually 
- we can create our docker image by setting the dockerfile =>creating a dockerfile(with no extension) and then applying the following steps:
	  1. OS - ubuntu per example
	  2. update the source repositories using apt
	  3. install dependencies using apt
	  4. install language used dependencies using the installer of the language used
	  5. copy source code to /opt folder 
	  6. run the web server using the language or the framework command
- after that u can build your image by using the build command 
```
docker build Dockerfile -t [image]
```
- to push it to docker hub use the command 
```
docker push [image]
```
- dockerfile is a text file written in a specific format that docker can understand , its an instruction and arguments format "INSTRUCTION + ARGUMENT", every image is based off of another image either an OS or another image that was created before 
- each line of the dockerfile define a layer of the image   