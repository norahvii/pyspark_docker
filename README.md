To build the container:
```bash
docker-compose up --build
```

To completely kill/remove the container:
```bash
docker-compose down
```

Then later, from the same directory, just:
```bash
docker-compose up
```

The container is essentially disposable - you can create and destroy it at will without affecting your work because:
1. All your notebooks/files live in your local directory
2. The mount means the container is just providing the PySpark/Jupyter environment
3. Any pip installations or environment changes you make inside the container will be lost when you kill it - if you need those to persist, add them to the Dockerfile

Think of the container like a running instance of your IDE/environment - your code and data are safe on your computer, and the container is just the tool you use to work with them.

To enter the container in shell, just:
```ps1
docker exec -it e8290bc42b4a bash
```

To get the Docker container do this (I use cuda 12.0):
```bash
docker pull nvidia/cuda:12.0.0-cudnn8-devel-ubuntu20.04
docker run --rm --gpus all nvidia/cuda:12.0.0-cudnn8-devel-ubuntu20.04 nvidia-smi
```
