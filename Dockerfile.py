# Use a lightweight debian os
# as the base image
FROM debian:stable-slim

# Update apt
RUN apt update
RUN apt upgrade -y

# Install build tooling
RUN apt install -y build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev

# Download Python interpreter code and unpack it
RUN wget https://www.python.org/ftp/python/3.10.8/Python-3.10.8.tgz
RUN tar -xf Python-3.10.*.tgz

# Build Python interpreter
RUN cd Python-3.10.8 && ./configure --enable-optimizations && make && make altinstall

# COPY code into the image
COPY main.py main.py

# Copy data dependencies
COPY books/ books/

# Excecute python main.py when image runs
CMD ["python3.10", "main.py"]