<h1 align="center">K8sCIFAR</h1>
<h3 align="center">Distributed Data Parallelism on CIFAR-10 using Kubernetes</h3>

___

## About
This project demonstrates **distributed deep learning training** using **Data Parallelism** on a **two-node Kubernetes cluster**. We train a `ResNet18` model on the CIFAR-10 dataset using PyTorch and Docker, orchestrated with Kubernetes.
This was submitted as a part of '**Enhanced Techniques for Big Data Computing**' course of **M.Sc. Big Data Analytics programme at Ramakrishna Mission Vivekananda Educational and Research Institute**.


## Course Project Details
This repository contains the report, slides, and jupyter notebook and related code files for the <b>final course project</b> of the <b>Enhanced Techniques for Big Data Computing</b> offered at 
<b>Ramakrishna Mission Vivekananda Educational and Research Institute, Belur</b> as a part of the <b>Master of Science in Big Data Analytics</b> program. <br>

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
- Kubernetes (k3s or Minikube or kubeadm)
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

## Contributors
This project was done by the team "<b>Bhattacharya Brothers </b>", whose team members are: <br>
- [Darpan Bhattacharya](https://www.linkedin.com/in/darpanbhattacharya/)
- [Soham Bhattacharya](https://www.linkedin.com/in/bhattacharyasoham026/)


-- Bhattacharya Brothers<br>
    &nbsp;&nbsp;&nbsp;April 22, 2025
<br>

<p>
  <img src="logo.png" alt="ChessLens Logo" width="50"/>
</p>
