FROM ubuntu:latest


#install python
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y python3
# RUN apt-get install python3-pip
#making a new directory in docker container


#install pip
FROM python:3.8
RUN -m pip install --upgrade pip

#installing needed libraries
RUN pip install pandas
RUN pip install -U scikit-learn
RUN pip install scipy
RUN pip install matplotlib
RUN pip install seaborn

#Copying dataset file
RUN mkdir -p home/doc-bd-a1
COPY bd-a1/StudentsPerformance.csv home/doc-bd-a1

RUN echo "HI"