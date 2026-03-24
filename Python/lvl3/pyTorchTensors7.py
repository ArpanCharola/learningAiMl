# Integrating PyTorch Tensors
# Question: Using PyTorch, create a tensor from a standard Python list and move that tensor to a GPU
# (if available) using the .to('cuda') command.

import torch

# creating tensor from py list
python_list = [1.0, 2.0, 3.0, 4.0, 5.0]
tensor_cpu = torch.tensor(python_list)
print(f"CPU tensor: {tensor_cpu}, device: {tensor_cpu.device}")

device = 'cuda' if torch.cuda.is_available() else 'cpu'
tensor_gpu = tensor_cpu.to(device)
print(f"GPU tensor: {tensor_gpu}, device: {tensor_gpu.device}")

# Why it matters: PyTorch is the "holy bible of AI" for writing GPU kernels and architectures