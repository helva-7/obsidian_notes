- lets say you have a variable in your application and it is set to a value , and i wanted to change it , i have to go to the app and change it . thats why its a best practice to move such information out of the application code and into an environment variable so we can change it outside of the app . when running a docker image , you have to pass the environment variable so it gets changed on the app by using 

```
docker run -e app_value=new_value [container]
```
each time you want to change the value , run this command with the value wanted 
- to find the environment variable set on a container thats already running, use the docker inspect command and u gonna find the variables on the "Env" section  