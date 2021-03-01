# Automatic Review Analyzer

## The Data
The data consists of several reviews, each of which has been labeled with  −1  or  +1 , corresponding to a negative or positive review, respectively. The original data has been split into four files:

- reviews_train.tsv (4000 examples)
- reviews_validation.tsv (500 examples)
- reviews_test.tsv (500 examples)

## Translating reviews to feature vectors
We will convert review texts into feature vectors using a bag of words approach. We start by compiling all the words that appear in a training set of reviews into a dictionary, thereby producing a list of  𝑑  unique words.


We can then transform each of the reviews into a feature vector of length  𝑑  in two ways. 
- By setting the  𝑖th  coordinate of the feature vector to  1  if the  𝑖th  word in the dictionary appears in the review, or  0  otherwise. For instance, consider two simple documents “Mary loves apples" and “Red apples". In this case, the dictionary is the set  {Mary;loves;apples;red} , and the documents are represented as  (1;1;1;0)  and  (0;0;1;1). 
- By setting the  𝑖th  coordinate of the feature vector to  c where c is the number of times the  𝑖th  word in the dictionary appears in the review. For instance, consider two simple documents “Mary loves apples and especially red apples" and “Red apples". In this case, the dictionary is the set  {Mary;loves;apples;red} , and the documents are represented as  (1;1;2;1)  and  (0;0;1;1). 

We will use both approaches to compare their results. We will also exclude some words that may confuse the learning process and we will create a dictionary without them. We will compare the results using both dictionaries.


## Executing
You can train the models, make predictions on training, validation and test set and calculate the accuracy of the classifier using the proper snippet from the main.py file. Inside main.py you will find code for:
- Loading data to obtain the dictionary and the training/validation/test set.
- Calculating the optimal theta and theta_0 values of the perceptron, average perceptron and pegasos algorithms.
- Calculating the accuracy of the perceptron, average perceptron and pegasos algorithms.
- Tuning algorithms, finding best performing T and L parameters.
- Finding the most explanatory unigrams.
- Running either the simple or the implementation with the dictionary without the excluded words.

You can run the functionalities using the proper snippet of the main.py script. Comment out not needed parts and uncomment needed. Then simply run:

```bash
python3 main.py
```

## Testing
You can test your modifications using the test.py tester script. Simply run:

```bash
python3 test.py
```
