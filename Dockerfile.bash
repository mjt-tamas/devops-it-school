# Dockerfile.bash

# 1. Base Image
FROM ubuntu:22.04

# 2. Update and Install Dependencies
# 'procps' is necessary for 'top' and 'free' commands used in bash_monitor.sh
RUN apt-get update && \
    apt-get install -y procps && \
    rm -rf /var/lib/apt/lists/*

# 3. Set Working Directory
WORKDIR /app

# 4. Copy the script and make it executable
COPY bash_monitor.sh /app/
RUN chmod +x /app/bash_monitor.sh

# 5. Define the command to run the script when the container starts
CMD ["/app/bash_monitor.sh"]