import pygame
from environment import PongEnvironment
from qlearning import QLearning

# Initialize Pygame
pygame.init()

# Set the screen size
screen = pygame.display.set_mode((800, 600))  # Assuming the width of the screen is 800

# Create environment
env = PongEnvironment(screen)

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

# Define the parameters for Q-learning
num_states = env.observation_space
num_actions = env.action_space
learning_rate = 0.5
discount_factor = 0.95
exploration_rate = 0.3

# Create the Q-learning object
q_learning = QLearning(num_states, num_actions, learning_rate, discount_factor, exploration_rate)

num_episodes = 1000  # number of games we want the agent to play

# Training loop
for episode in range(num_episodes):
    state = env.reset()
    done = False
    while not done:
        # Choose an action
        action = q_learning.get_action(state)
        # Take a step in the environment with the chosen action
        next_state, reward, done = env.step(action)
        # Update the q-values
        q_learning.update(state, action, reward, next_state)
        # Move on to the next state
        state = next_state

        env.render()  # update the screen with the game state
        clock.tick(60)  # maintain 60 fps

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

pygame.quit()