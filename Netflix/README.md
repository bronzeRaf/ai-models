# Gaussian Mixture Models on Netflix data 

## The Data

For this project the following data file will be used:

- **toy_data.txt**: a 2D dataset that will be used to build simple clustering algorithms
- **netflix_incomplete.txt**: the netflix dataset with missing entries to be completed. It contains user entries with ratings (1-5 stars) to movies each user rated. It is missing the ratings (labeled 0) to movies the user did not rate yet.
- **netflix_complete.txt**: the netflix dataset with missing entries completed. It contains user entries with ratings from each user to each movie. It is containing also estimations on the ratings to movies the user did not rate yet.
- **test_incomplete.txt**: a test dataset to test for you to test your code against the implementation
- **test_complete.txt**: a test dataset to test for you to test your code against the implementation
- **test_solutions.txt**: a test dataset to test for you to test your code against the implementation

## Clustering models

This project contains several approaches for unsupervised learning. Several clustering methods have been applied to the data described above. It is based on Kmeas and  Expectation–maximization algorithms for building the clustering models. More details on the approaches: 

- Kmeans
  - A Kmeans algorithm has been implemented. This approach will be tested as a standalone clustering method as long as a method to calculate mixture models that will be used on another approaches.
- Expectation–maximization 
  - An EM algorithm has been implemented and tested as a clustering approach for the toy data.
  - An EM algorithm respecting missing values has been implemented and tested as a clustering approach for the netflix data. This algorithm takes into account the big amount of missing ratings as long as the possibly small values in many calculations. It contains logic to protect from small points erratic results in the variance and mean in the Gaussian models, numerical underflow etc...
- An algorithm that completes the missing entries of the Netflix data. This algorithm runs the EM model to assign clusters to each user in order to estimate the missing ratings.  
- Bayesian Information Criterion
  - A BIC used as a criterion for model selection. It captures the tradeoff between the log-likelihood of the data, and the number of parameters that the model uses. It is used as a metric that helps to the selection of the number of clusters for our models.


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


