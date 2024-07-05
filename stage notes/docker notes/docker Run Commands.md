#docker

# docker Run -tag 
- we use it when we want to specify a version of the container we want to run seperated by a " : " , this is called a tag ,if the tag is not defined its considered as to be "latest" 

# docker run -STDIN 
- to run a container that has an app that needs inputs  
- to make it interactive so we can add an input , we use the -i "input" argument and the -t "pseudo terminal" argument which the command became `docker run -it  [container]` , then it prints the prompt and waits for an input