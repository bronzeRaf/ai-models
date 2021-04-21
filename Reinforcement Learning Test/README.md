# Reinforcement Leaning Toy Example

## Concept

Consider an one-dimensional grid of 5 states, where an agent starts from the leftmost grid location and the goal is to reach the rightmost grid location. This example considers this toy world as a Markovian chain and calculates the expected reward from each state after acting infinite step optimally.

## Transitions Probabilities and Rewards

At any given grid location the agent can choose to either stay at the location or move to an adjacent grid location. The transition action could either success or fail as:  

- If the agent chooses to stay at the location, such an action is successful with probability 1/2 and:
    - If the agent is at the leftmost or rightmost grid location it ends up at its neighboring grid location with probability 1/2. 
    - if the agent is at any of the inner grid locations it has a probability 1/4 each of ending up at either of the neighboring locations.
    
- If the agent chooses to move (either left or right) at any of the inner grid locations, such an action is successful with probability 1/3 and with probability 2/3 it fails to move, and:
    - if the agent chooses to move left at the leftmost grid location, then the action ends up exactly the same as choosing to stay, i.e., staying at the leftmost grid location with probability 1/2, and ends up at its neighboring grid location with probability 1/2,
    - if the agent chooses to move right at the rightmost grid location, then the action ends up exactly the same as choosing to stay, i.e., staying at the rightmost grid location with probability 1/2, and ends up at its neighboring grid location with probability 1/2.
    
The only location that is rewarded is the rightmost grid location with +1 reward.

## Implementation 

We initialize the expected reward for each state with zeros and we consider a discount factor of 0.5. The algorithm converges after 100 iterations.

## Run 

In order to run the example you will hae to install Numpy in your Python3. 

To do so, if you are using pip run:

```commandline
pip3 numpy
```

Or if you are using Conda environments run:
```commandline
# Best practice, use an environment rather than install in the base env
conda create -n my-env
conda activate my-env
# If you want to install from conda-forge
conda config --env --add channels conda-forge
# The actual install command
conda install numpy
```

Then you should be able to run from the example's directory:

```commandline
python3 main.py
```