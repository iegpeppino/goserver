# Use a lightweight debian os
# as the base image
FROM debian:stable-slim

# COPY source destination files
COPY main.py main.py
COPY books/ books/

# Excecute python main.py when image runs
CMD ["python", "main.py"]