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

# Testing the Kmeans along K (number of clusters) and seed (random init)
########################################################################
# Initialize min cost per K array
min_cost = np.ones(4)*np.inf
min_cost_seed = np.zeros(4)

for K in range(1,5):
    for seed in range(0,5):
        mixture, post = common.init(X, K, seed)
        mixture, post, cost = kmeans.run(X, mixture, post)

        # uncomment following line to print cost per K/seed
        # print('K='+str(K)+' seed='+str(seed)+' cost='+str(cost))

        # collect the min cost
        if min_cost[K-1] > cost:
            min_cost[K-1] = cost
            min_cost_seed[K-1] = seed

        # uncomment following line to plot the clusters
        # common.plot(X, mixture, post, 'K='+str(K)+' seed='+str(seed))
print('______________________________________________________________________')
print('Kmeans results: Min cost per K (1-5) and seed with this min cost (0-4)')
print(min_cost)
print(min_cost_seed)
########################################################################


# Testing the EM along K (number of clusters) and seed (random init)
########################################################################
# Initialize max log likelihood per K array
max_ll = np.zeros(4)
max_ll_seed = np.zeros(4)

for K in range(1,5):
    for seed in range(0,5):
        mixture, post = common.init(X, K, seed)
        mixture, post, ll = naive_em.run(X, mixture, post)

        # uncomment following line to print cost per K/seed
        # print('K='+str(K)+' seed='+str(seed)+' Log Likelihood='+str(ll))

        # collect the min cost
        if max_ll[K-1] < abs(ll):
            max_ll[K-1] = ll
            max_ll_seed[K-1] = seed

        # uncomment following line to plot the clusters
        # common.plot(X, mixture, post, 'K='+str(K)+' seed='+str(seed))
print('______________________________________________________________________')
print('EM results: Max abs Log Likelihood per K (1-5) and seed with this likelihood (0-4)')
print(max_ll)
print(max_ll_seed)
########################################################################