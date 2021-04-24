# Gaussian Mixture Models on Netflix data 

## The Data

For this project the following data file will be used:

- **toy_data.txt**: a 2D dataset that will be used to build simple clustering algorithms
- **netflix_incomplete.txt**: the netflix dataset with missing entries to be completed. It contains user entries with ratings to movies each user rated. It is missing the ratings to movies the user did not rate yet.
- **netflix_complete.txt**: the netflix dataset with missing entries completed. It contains user entries with ratings from each user to each movie. It is containing also estimations on the ratings to movies the user did not rate yet.
- **test_incomplete.txt**: a test dataset to test for you to test your code against the implementation
- **test_complete.txt**: a test dataset to test for you to test your code against the implementation
- **test_solutions.txt**: a test dataset to test for you to test your code against the implementation

## Clustering models

This project contains several approaches for unsupervised learning. Several clustering methods have been applied to the data described above. It is based on Kmeas and  Expectation–maximization algorithms for building the clustering models. More details on the approaches: 

- Kmeans
  - A Kmeans algorithm has been implemented. This approach will be tested as a standalone clustering method as long as a method to calculate mixture models that will be used on another approaches.
-  Expectation–maximization 
  - An EM algorithm has been implemented and tested as a clustering approach. 
    


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

### Testing
You can test your modifications using the part1/test.py tester script. Simply run:

```bash
python3 test.py
```

