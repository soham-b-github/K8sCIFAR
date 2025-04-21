# train_ddp.py
import os
import torch
import torch.distributed as dist
import torch.nn as nn
import torch.optim as optim
from torch.nn.parallel import DistributedDataParallel as DDP
from torchvision import datasets, transforms, models
from torch.utils.data import DataLoader, DistributedSampler

def setup():
    dist.init_process_group(
        backend='gloo',
        init_method='env://',
        world_size=int(os.environ['WORLD_SIZE']),
        # ~ rank=int(os.environ['RANK'])
        rank = int(os.environ['RANK'].split('-')[-1])  # Extracts numeric rank from 'ddp-trainer-0'

    )

def cleanup():
    dist.destroy_process_group()

def main():
    setup()

    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.5,), (0.5,))
    ])

    
    dataset = datasets.CIFAR10(root='/srv/nfs/cifar10', train=True, download=True, transform=transform)
    print("DONE1")
    sampler = DistributedSampler(dataset)
    print("DONE2")

    dataloader = DataLoader(dataset, sampler=sampler, batch_size=256)
    print("DONE3")

    model = models.resnet18(num_classes=10)
    print("DONE4")

    model = DDP(model)
    print("DONE5")

    loss_fn = nn.CrossEntropyLoss()
    print("DONE6")

    optimizer = optim.Adam(model.parameters(), lr=0.001)
    print("DONE7")

    for epoch in range(3):
        print("epoch", epoch)
        ctr = 0
        for images, labels in dataloader:
            ctr = ctr + 1
            print("hello123", ctr)
            outputs = model(images)
            loss = loss_fn(outputs, labels)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            if ctr % 10 == 0:
                print(f"[RANK {os.environ['RANK']}] Epoch {epoch}, Step {ctr}, Loss: {loss.item():.4f}")
        print(f"[RANK {os.environ['RANK']}] Epoch {epoch} complete")

    cleanup()

if __name__ == "__main__":
    main()
