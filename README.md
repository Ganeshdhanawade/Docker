# Docker Cheat Sheet 🐳

## Docker Images 🖼️

| Command | Description |
|---|---|
| 📄 `docker images` | List all available Docker images on the local machine |
| 🚀 `docker pull <image-name>` | Download an image from a Docker registry |
| 🛠️ `docker build -t <image-name> <directory>` | Build an image from a Dockerfile located in the specified path |
| 🗑️ `docker rmi <image-name>` | Remove a Docker image |

## Docker Containers 🚢

| Command | Description |
|---|---|
| 📋 `docker ps` | List all running Docker containers |
| 📋 `docker ps -a` | List all Docker containers (including stopped ones) |
| 🚀 `docker run <image-name>` | Create and start a new container from a Docker image |
| 🔄 `docker start <container-name>` | Start a stopped container |
| ⏹️ `docker stop <container-name>` | Stop a running container |
| 🔄 `docker restart <container-name>` | Restart a running container |
| 🗑️ `docker rm <container-name>` | Remove a Docker container |
| 🖥️ `docker exec -it <container-name> <command>` | Execute a command within a running container |
| 📃 `docker logs <container-name>` | View the logs of a running container |
| 📂 `docker cp <container-name>:<path> <local>` | Copy files or directories between the host and a container |
| 📦 `docker commit <container-name> <image-name>` | Create a new image from a container's changes |
| 🔍 `docker inspect <container-name>` | Display detailed information about a container |

## Docker Volumes 🗂️

| Command | Description |
|---|---|
| 📋 `docker volume ls` | List all Docker volumes |
| 🎉 `docker volume create <volume-name>` | Create a new Docker volume |
| 🔍 `docker volume inspect <volume-name>` | Display detailed information about a Docker volume |
| 🗑️ `docker volume rm <volume-name>` | Remove a Docker volume |
| 🚀 `docker run -v <volume-name>:<container-path>` | Mount a Docker volume to a specific path within a container |

## Docker Networks 🌐

| Command | Description |
|---|---|
| 📋 `docker network ls` | List all Docker networks |
| 🎉 `docker network create <network-name>` | Create a new Docker network |
| 🔍 `docker network inspect <network-name>` | Display detailed information about a Docker network |
| 🗑️ `docker network rm <network-name>` | Remove a Docker network |
| 🔗 `docker network connect <network> <container>` | Connect a container to a Docker network |
| 🔗 `docker network disconnect <network> <container>` | Disconnect a container from a Docker network |

## Docker Compose 🎵

| Command | Description |
|---|---|
| 🚀 `docker-compose up` | Create and start containers defined in a Compose file |
| 🛑 `docker-compose down` | Stop and remove containers, networks, and volumes |
| 📋 `docker-compose ps` | List containers created by `docker-compose up` |
| 📃 `docker-compose logs` | View the logs of containers created by `docker-compose up` |




🐳 **Docker Concepts**

1.  **Images**: 🖼️
    
    -   An image is a read-only template that contains instructions to create a Docker container. 🏗️
    -   Images are pulled from registries or built locally using a Dockerfile. 📥
    -   They are portable and can be shared, allowing easy distribution of applications and their dependencies. 🚀
2.  **Containers**: 📦
    
    -   Containers are isolated and lightweight instances of Docker images. 🚀
    -   They provide an environment where applications can run with their dependencies. 🌐
    -   Containers offer consistent behavior regardless of the host environment, making them highly portable. 📤
    -   They are ephemeral by default, meaning they can be stopped, started, or destroyed without affecting the underlying host or other containers. ⏳
3.  **Registries**: 📦🔒
    
    -   Registries are repositories for Docker images. They can be public or private. 🏢
    -   Docker Hub is the default public registry, hosting a vast collection of images contributed by the community. 🌍
    -   Private registries enable organizations to securely store and distribute their proprietary images within their infrastructure. 🔒
4.  **Dockerfile**: 📝
    
    -   A Dockerfile is a text file that defines the build process for a Docker image. 🛠️
    -   It specifies the base image, dependencies, environment variables, and commands required to create the image. ⚙️
    -   Dockerfiles provide a declarative approach to define reproducible and automated image builds, reducing the chance of inconsistencies. 🔄
5.  **Volumes**: 💾
    
    -   Volumes provide persistent storage for data shared between containers and the host. 📂
    -   They decouple data from the container, allowing it to be preserved even if the container is removed. 💡
    -   Volumes can be managed by Docker, ensuring data integrity and facilitating easy backup and restore processes. 💪
6.  **Networks**: 🌐
    
    -   Docker networks enable communication between containers running on the same or different hosts. 🔗
    -   They provide isolated network environments for containers, allowing secure inter-container communication. 🔒
    -   Docker networks support different types of drivers and offer fine-grained control over network connectivity and routing. 🛣️
7.  **Docker Compose**: 🎵
    
    -   Docker Compose simplifies managing multi-container applications using a YAML file. 🎼
    -   It allows defining and running a complete application stack with multiple interconnected services. 📋
    -   Docker Compose provides a convenient way to orchestrate complex environments and manage their lifecycle as a single unit. 🔄
8.  **Orchestration**: ⚙️🕺
    
    -   Orchestration tools like Docker Swarm and Kubernetes manage containers at scale. 🔄
    -   They enable deploying, scaling, and managing containerized applications across a cluster of machines. 🚀
    -   Orchestration tools automate tasks such as load balancing, service discovery, rolling updates, and high availability. 🔄

## commonly used commands in Dockerfile:

```
# Dockerfile Cheat Sheet

# Set base image
FROM <base_image>

# Set the working directory
WORKDIR /path/to/directory

# Copy files from host to container
COPY <source> <destination>

# Copy files from host to container, respecting symbolic links
COPY --chown=<user>:<group> <source> <destination>

# Set environment variable
ENV <key>=<value>

# Run a command during build
RUN <command>

# Add metadata to an image
LABEL <key>=<value>

# Expose a port
EXPOSE <port>

# Set the entry point for the container
ENTRYPOINT ["<command>", "<arg1>", "<arg2>", ...]

# Set the default command for the container
CMD ["<command>", "<arg1>", "<arg2>", ...]

# Set the default command for the container as a string
CMD "<command> <arg1> <arg2> ..."

# Add a volume to the container
VOLUME /path/to/volume

# Specify the user for the container
USER <username>

# Specify the health check for the container
HEALTHCHECK --interval=<interval> --timeout=<timeout> --retries=<retries> --start-period=<start_period> CMD <command>

# Set a custom name for the container
# Note: This command is specific to Docker Compose
container_name: <name>

# Build an image using a Dockerfile
docker build -t <image_name> .

# Run a container from an image
docker run -d --name <container_name> -p <host_port>:<container_port> <image_name>

# Start a stopped container
docker start <container_name>

# Stop a running container
docker stop <container_name>

# Remove a container
docker rm <container_name>

# List running containers
docker ps

# List all containers (including stopped containers)
docker ps -a

# List Docker images
docker images

# Remove an image
docker rmi <image_name>

```

### reference

- (Dockerfile reference)[https://docs.docker.com/reference/dockerfile/]
