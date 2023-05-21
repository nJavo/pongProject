import torch
from torch import nn

class PongAgent(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(6, 64)  # Assuming the game state is a vector of 6 numbers: the x and y position of the paddles, the x and y velocity of the ball, and the x and y position of the ball
        self.fc2 = nn.Linear(64, 64)
        self.fc3 = nn.Linear(64, 2)  # There are two possible actions: move up or down

    def forward(self, x):
        x = torch.tanh(self.fc1(x))
        x = torch.tanh(self.fc2(x))
        x = self.fc3(x)
        return x