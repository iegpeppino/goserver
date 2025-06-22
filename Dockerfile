# This is a comment

# Use a lightweight debian os
# as the base image
FROM debian:stable-slim

# COPY source destination
COPY goserver /bin/goserver

# Set PORT
ENV PORT=8991

# execute the 'goserver' file
# when the container runs
CMD ["/bin/goserver"]