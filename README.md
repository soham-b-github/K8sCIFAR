# K8sCIFAR: Data Parallelism using Kubernetes - ResNet18 on CIFAR-10
This project demonstrates **distributed deep learning training** using **Data Parallelism** on a **two-node Kubernetes cluster**. We train a `ResNet18` model on the CIFAR-10 dataset using PyTorch and Docker, orchestrated with Kubernetes.
This was submitted as a part of '**Enhanced Techniques for Big Data Computing**' course of **M.Sc. Big Data Analytics programme at Ramakrishna Mission Vivekananda Educational and Research Institute**.

## Contributors: 
- [Darpan Bhattacharya](https://www.linkedin.com/in/darpanbhattacharya/)
- [Soham Bhattacharya](https://www.linkedin.com/in/bhattacharyasoham026/)


## Project Overview

- **Model**: ResNet18 (PyTorch)
- **Dataset**: CIFAR-10
- **Parallelism**: Data Parallelism with `DistributedDataParallel`
- **Cluster**: 2-node Kubernetes cluster (Master + Worker)
- **Containerization**: Docker
- **Orchestration**: Kubernetes

---

## Tech Stack

- Python 3.10+
- PyTorch
- Kubernetes (Minikube or kubeadm)
- Docker
- torchvision
- torch.distributed

---

## Plan of implementation

- **Step 1**: Set up Kubernetes cluster
  - Use `"kubeadm"`, `"k3s"` or `"minikube"` (multi-node) depending on preference.
  - One laptop/computer will be the master node, the other will be the worker node.
- **Step 2**: Data Parallelism
  - Use PyTorch `DataDistributedParallel` (DDP) or Tensorflow’s MultiWorkerMirroredStrategy.
  - Split the CIFAR-10 dataset across two nodes.
- **Step 3**: Containerize the Training Code
  - Write `DockerFile` that installs dependencies, mounts data & runs training.
  - Push to a container registry (local/private) or DockerHub.
- **Step 4**: Deploy Kubernetes
  - Define a StatefulSet or Deployment for each training process.
  - Use headless services + shared storage (NFS or object-store) if needed.
  - Set host networking or Service DNS for communication.
