import numpy as np
import kmeans
import common
import naive_em
import em

# Read toy data
X = np.loadtxt("toy_data.txt")

# Parameters
K = 1
seed = 1

for K in range(1,5):
    for seed in range(0,5):
        mixture, post = common.init(X, K, seed)

        mixture, post, cost = kmeans.run(X, mixture, post)
        print('K='+str(K)+' seed='+str(seed)+' cost='+str(cost))
        # common.plot(X, mixture, post, 'K='+str(K)+' seed='+str(seed))