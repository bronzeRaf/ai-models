# Automatic Review Analyzer

## The Data
The data consists of several reviews, each of which has been labeled with  −1  or  +1 , corresponding to a negative or positive review, respectively. The original data has been split into four files:

- reviews_train.tsv (4000 examples)
- reviews_validation.tsv (500 examples)
- reviews_test.tsv (500 examples)

## Translating reviews to feature vectors
We will convert review texts into feature vectors using a bag of words approach. We start by compiling all the words that appear in a training set of reviews into a dictionary, thereby producing a list of  𝑑  unique words.


We can then transform each of the reviews into a feature vector of length  𝑑  by setting the  𝑖th  coordinate of the feature vector to  1  if the  𝑖th  word in the dictionary appears in the review, or  0  otherwise. For instance, consider two simple documents “Mary loves apples" and “Red apples". In this case, the dictionary is the set  {Mary;loves;apples;red} , and the documents are represented as  (1;1;1;0)  and  (0;0;1;1) .

A bag of words model can be easily expanded to include phrases of length  𝑚. A unigram model is the case for which  𝑚=1. In the example, the unigram dictionary would be  (Mary;loves;apples;red). In the bigram case,  𝑚=2, the dictionary is  (Mary loves;loves apples;Red apples), and representations for each sample are  (1;1;0),(0;0;1). In this section, you will only use the unigram word features. These functions are already implemented in the bag of words function.
