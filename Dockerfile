# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory to /toyproject
WORKDIR /toyproject

#Copy the current directory contentes into the container at /toyproject
COPY . /toyproject

# Install any needed packages
RUN python3 setup.py develop

RUN chmod +x aiohttp_chat/main.py
# CMD [ "python", "-u", "main.py" ]
CMD ["python3", "-u", "aiohttp_chat/main.py"]

# Make port 8080 available to the world outside this container
EXPOSE 8080 