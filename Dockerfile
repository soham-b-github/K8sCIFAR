# Dockerfile
FROM python:3.10-slim

RUN apt update && apt install -y git && pip install torch torchvision

COPY train_ddp.py /app/train_ddp.py

WORKDIR /app
CMD ["python", "train_ddp.py"]
