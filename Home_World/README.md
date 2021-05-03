# Q-learning in Home World game 

## The Game

For this project a game has been developed which mimic the environment of a typical house. The world consists of a few rooms, and each room contains a representative object that the player can interact with. For instance, the kitchen has an apple that the player can eat. The goal of the player is to finish some quest. An example of a quest given to the player in text is You are hungry now . To complete this quest, the player has to navigate through the house to reach the kitchen and eat the apple. In this game, the room is hidden from the player, who only receives a description of the underlying room. At each step, the player read the text describing the current room and the quest, and respond with some command (e.g., eat apple ). The player then receives some reward that depends on the state and his/her command.


## Learning models

In order to design an autonomous game player, we will employ a reinforcement learning framework to learn command policies using game rewards as feedback. Since the state observable to the player is described in text, we have to choose a mechanism that maps text descriptions into vector representations. A naive approach is to create a map that assigns a unique index for each text description. However, such approach becomes difficult to implement when the number of textual state descriptions are huge. An alternative method is to use a bag-of-words representation derived from the text description. This project is testing both approaches containing the following:

- A tabular Q-learning algorithm for a simple setting where each text description is associated with a unique index.
- A Q-learning algorithm with linear approximation architecture, using bag-of-words representation for textual state description.
- A deep Q-network.
- Usage of the Q-learning algorithms on the Home World game.


### Executing
You can run the models, perform clustering, plot the clusters and print the evaluation metrics from the main.py file. Inside main.py you will find comment instructions and code for:
- Loading data and the training/test set.
- Clustering via Kmeans on toy data.
- Clustering via EM on toy data.
- Plotting and printing results, in order to evaluate the models.
- Preprocessing the data using the above described approaches.

You can run the functionalities using the proper snippet of the main.py script. Comment out not needed parts and uncomment needed. Then simply run:

```bash
python3 main.py
```

