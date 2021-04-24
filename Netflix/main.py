import numpy as np
import kmeans
import common
import naive_em
import em

# Read toy data
X = np.loadtxt("toy_data.txt")
X_netflix_incomplete = np.loadtxt("netflix_incomplete.txt")
X_netflix_complete = np.loadtxt("netflix_complete.txt")

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

        # collect the max likelihood
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


# Testing the EM along K (number of clusters) with seed = 4 (random init) using the BIC metric
########################################################################
# Initialize max log likelihood per K array
max_bic = -np.inf
max_bic_K = 0
seed = 4

for K in range(1,5):
    mixture, post = common.init(X, K, seed)
    mixture, post, ll = naive_em.run(X, mixture, post)
    bic = common.bic(X, mixture, ll)
    # uncomment following line to print cost per K/seed
    # print('K='+str(K)+' seed='+str(seed)+' Log Likelihood='+str(ll))

    # collect the max bic
    if max_bic < bic:
        max_bic = bic
        max_bic_K = K

    # uncomment following line to plot the clusters
    # common.plot(X, mixture, post, 'K='+str(K)+' seed='+str(seed))
print('______________________________________________________________________')
print('EM results: Max BIC metric to select K (1-5) with seed=4')
print('MAX BIC: ', max_bic)
print('Selected number of clusters: ', max_bic_K)
########################################################################


# Testing the EM along K (number of clusters) for K=1 and K=12 and seed=[0,1,2,3,4] (random init)
########################################################################
# Initialize max log likelihood per K array
max_ll = np.zeros(2)
max_ll_seed = np.zeros(4)

i = 0
for K in (1, 12):
    for seed in range(0,5):
        mixture, post = common.init(X_netflix_incomplete, K, seed)
        mixture, post, ll = em.run(X_netflix_incomplete, mixture, post)

        # uncomment following line to print cost per K/seed
        # print('K='+str(K)+' seed='+str(seed)+' Log Likelihood='+str(ll))

        # collect the max likelihood
        if max_ll[i] < abs(ll):
            max_ll[i] = ll
            max_ll_seed[i] = seed

        # uncomment following line to plot the clusters
        # common.plot(X, mixture, post, 'K='+str(K)+' seed='+str(seed))
    i += 1

print('______________________________________________________________________')
print('EM results: Max abs Log Likelihood per K [1,12] and seed with this likelihood (0-4)')
print(max_ll)
print(max_ll_seed)
########################################################################


# Estimate the missing ratings and evaluate model with the Test set using the RMSE metric
# K = 12 (number of clusters and seed = 4 (random init)
########################################################################

# Parameters
K = 12
seed = 4

# Build the mixture models
mixture, post = common.init(X_netflix_incomplete, K, seed)
mixture, post, ll = em.run(X_netflix_incomplete, mixture, post)

X_pred = em.fill_matrix(X_netflix_incomplete, mixture)

rmse = common.rmse(X_netflix_complete, X_pred)

print(rmse)