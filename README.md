# Assignment-1-Big-Data


## Notes to run the image

1. run docker build -t {image_name} . ---> to build the docker image, run this command inside the git main repo when you clone it
2. docker run -it {image_name} ---> runs the container and opens a bash shell inside the container
3. (in the container shell) ---> make sure you're on the /home/doc-bd-a1 directory 
4. ls to check if the dataset is copied into the container directory
5. To make sure that the container is running, open another terminal and run docker ps

**I just finished the shell script and it copies the directory with the path /home/doc-bd-a1/service_results to the working directory in the main git repo**

- [ ] create a directory in the container with the path specified to hold all the text files and visualizations generated from the python files 
