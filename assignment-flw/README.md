# Federated Learning with Flower 

## Overview
This project demonstrates a minimal federated learning setup using the Flower framework.  
It validates the understanding of local training and global model aggregation in a federated environment.

---

## How TO Run

### Requirements
- Python 3
- Flower 
- PyTorch
- NumPy

Install dependencies:
pip install flwr torch numpy

- Start the server in one terminal.
  python server.py

- Run the client apps in the other two terminals.
  python client.py
---

## Expaination

### Client Role
-Receives the global model from the server.

-Trains the model on local data for three rounds.

-Logs training loss before and after local training.

-Sends updated model weights to the server.

### Server Role
-Initializes the global model

-Coordinates training rounds

-Collects model updates from all clients

-Aggregates client updates into a new global model

### Aggregation
-The server averages model parameters received from clients

-The aggregated parameters form the updated global model

---

## Screen Shots of Execution

<img width="760" height="527" alt="Screenshot 2025-12-28 at 11 14 46 PM" src="https://github.com/user-attachments/assets/f13d0873-3b4d-4f0a-a288-a21592df1250" />

<img width="891" height="478" alt="Screenshot 2025-12-28 at 11 15 15 PM" src="https://github.com/user-attachments/assets/46f52c2a-ecf6-48ca-aabb-9b13523c1376" />

<img width="880" height="503" alt="Screenshot 2025-12-28 at 11 15 32 PM" src="https://github.com/user-attachments/assets/3f63cc7e-4ebc-4708-9608-fb327e85a15b" />
