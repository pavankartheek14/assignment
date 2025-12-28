import flwr as fl
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
from model import SimpleNet

X = torch.randn(100, 10)
y = torch.randn(100, 1)

model = SimpleNet()
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

def train():
    model.train()
    optimizer.zero_grad()
    outputs = model(X)
    loss = criterion(outputs, y)
    loss.backward()
    optimizer.step()
    return loss.item()

def get_parameters():
    return [val.cpu().numpy() for val in model.state_dict().values()]

def set_parameters(parameters):
    params_dict = zip(model.state_dict().keys(), parameters)
    state_dict = {k: torch.tensor(v) for k, v in params_dict}
    model.load_state_dict(state_dict, strict=True)

class FlowerClient(fl.client.NumPyClient):
    def get_parameters(self, config):
        return get_parameters()

    def fit(self, parameters, config):
        set_parameters(parameters)

        loss_before = train()
        loss_after = train()

        print(f"Client loss before training: {loss_before:.4f}")
        print(f"Client loss after training: {loss_after:.4f}")

        return get_parameters(), len(X), {}

    def evaluate(self, parameters, config):
        set_parameters(parameters)
        outputs = model(X)
        loss = criterion(outputs, y).item()
        return loss, len(X), {}

fl.client.start_numpy_client(
    server_address="127.0.0.1:8080",
    client=FlowerClient()
)
