# Q-learning in Home World game 

## The Game

For this project a game has been developed which mimic the environment of a typical house. The world consists of a few rooms, and each room contains a representative object that the player can interact with. For instance, the kitchen has an apple that the player can eat. The goal of the player is to finish some quest. An example of a quest given to the player in text is You are hungry now . To complete this quest, the player has to navigate through the house to reach the kitchen and eat the apple. In this game, the room is hidden from the player, who only receives a description of the underlying room. At each step, the player read the text describing the current room and the quest, and respond with some command (e.g., eat apple ). The player then receives some reward that depends on the state and his/her command.


## Learning models

In order to design an autonomous game player, we will employ a reinforcement learning framework to learn command policies using game rewards as feedback. Since the state observable to the player is described in text, we have to choose a mechanism that maps text descriptions into vector representations. A naive approach is to create a map that assigns a unique index for each text description. However, such approach becomes difficult to implement when the number of textual state descriptions are huge. An alternative method is to use a bag-of-words representation derived from the text description. This project is testing both approaches containing the following:

- A tabular Q-learning algorithm for a simple setting where each text description is associated with a unique index.
- A Q-learning algorithm with linear approximation architecture, using bag-of-words representation for textual state description.
- A deep Q-network using a neural network to update the Q values.
- Usage of the Q-learning algorithms on the Home World game.


### Executing
You can train, evaluate the models, see the progress of the average rewards obtained, plot the learning curves and print the evaluation metrics from the specific files for each approach.

- You can run the functionalities of the tabular Q-learning algorithm running:

```bash
python3 agent_tabular_ql.py
```

- You can run the functionalities of the linear Q-learning algorithm running:

```bash
python3 agent_linear.py
```

- You can run the functionalities of the deep Q-learning algorithm running:

```bash
python3 agent_dqn.py
```
