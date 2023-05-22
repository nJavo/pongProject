import numpy as np

class QLearning:
    def __init__(self, num_states, num_actions, learning_rate, discount_factor, exploration_rate):
        self.num_actions = num_actions
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate
        self.q_table = np.zeros((num_states, num_actions))

    def get_action(self, state):
        # Exploration vs exploitation
        if np.random.uniform(0, 1) < self.exploration_rate:
            # Exploration: choose a random action
            action = np.random.choice(self.num_actions)
        else:
            # Exploitation: choose the action with the highest q-value for this state
            action = np.argmax(self.q_table[state])
        return action

    def update(self, state, action, reward, next_state):
        # Calculate the new q-value for the state-action pair
        q_old = self.q_table[state][action]
        max_future_q = np.max(self.q_table[next_state])
        q_new = (1 - self.learning_rate) * q_old + self.learning_rate * (reward + self.discount_factor * max_future_q)
        # Update the q-value in the table
        self.q_table[state][action] = q_new