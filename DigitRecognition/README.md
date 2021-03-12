# Automatic Digit Recognizer

## The Data
The MNIST database contains binary images of handwritten digits commonly used to train image processing systems. The digits were collected from among Census Bureau employees and high school students. The database contains 60,000 training digits and 10,000 testing digits, all of which have been size-normalized and centered in a fixed-size image of 28 × 28 pixels. Many methods have been tested with this dataset and in this project, you will get a chance to experiment with the task of classifying these images into the correct digit using some of the methods you have learned so far.

## Translating photos to digits

These set contains the following models for classifying the photos:
- Linear regression
- SVM classifier 
- Logistic regression (Softmax regression)

---
---

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
