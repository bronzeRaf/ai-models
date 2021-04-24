# Automatic Digit Recognizer

## The Data
The MNIST database contains binary images of handwritten digits commonly used to train image processing systems. The digits were collected from among Census Bureau employees and high school students. The database contains 60,000 training digits and 10,000 testing digits, all of which have been size-normalized and centered in a fixed-size image of 28 × 28 pixels. Many methods have been tested with this dataset and in this project, you will get a chance to experiment with the task of classifying these images into the correct digit using some famous methods.

## PART 1

This project contains several approaches for image classification, using the data described above. It is based on Regression, SVM and Softmax - Gradient Decent for building the classifier models. More details on the approaches in the subsection below. 

### Translating photos to digits

This set contains the following approaches for classifying the photos:
- Linear regression
  - A liner regression approach, based on the closed form solution. This model uses the raw pixel values of each image as features.
- SVM classifier 
  - Two models of this approach have been developed. An one versus rest and a multiclass SVM too.
- Logistic regression (Softmax regression using Gradient Descent)
  - This approach expands the single logistic regression model into a multinomial regression and solves it with gradient descent algorithm. It is based on a cost function, which evaluates the probabilities of data points to be classified into labels.
- Label Changing
  - This approach changes the labels of the data points, to classify the digits by their (mod 3) value. The model used in this case is also Logistic regression trained by Gradient Descent, but the new dataset could be used for any of the above models.
- Dimensionality Reduction Using PCA
  - This approach projects the data onto the principal components, reducing their dimensionality and explores the effects on performance. The new dataset could be used for any of the above models.
- Cubic feature mapping
  - This mapping could be used to compute the cubic features explicitly. Note that this could be extremely computationally inefficient, as the data points contain 784-dimensional raw pixel features. This method is supposed to work after PCA dimensionality reduction. The new dataset could be used for any of the above models.
- Kernel mapping
  - This approach is used to avoid an explicit feature mapping. Instead of real mapping, the inner product between two features after mapping is calculated, using either a Polynomial or a Gaussian RBF Kernel. This method is quite more efficient that the previous one. The new dataset could be used for any of the above models.

### Executing
You can train the models, make predictions on training, validation and test set and calculate the accuracy of the classifier using the proper snippet from the main.py file. Inside main.py you will find comment instructions and code for:
- Loading data and the training/test set.
- Calculating the theta and theta_0 values of the above described models.
- Calculating the accuracy of the above described models.
- Plotting and printing results, in order to evaluate the models.
- Preprocessing the data using the above described approaches.

You can run the functionalities using the proper snippet of the part1/main.py script. Comment out not needed parts and uncomment needed. Then simply run:

```bash
python3 main.py
```

### Testing
You can test your modifications using the part1/test.py tester script. Simply run:

```bash
python3 test.py
```


## PART 2 A

This project contains a set of Neural Network approaches for image classification, using the data described above. More detailed:

- A custom implemented Neural Network.
  - Input Layer (Dim 2) - Hidden Layer (Dim 3) with RELU activation and Bias - Output Layer (Dim 1).
  - This is a toy example of a NN using toy data for training and testing purposes.
- A Fully Connected Neural Network implemented using the PyTorch library.
  - Input Layer (Dim 784) - Hidden Layer (Dim 128) with RELU activation and Bias - Output Layer (Dim 10).
  - This NN is able to train and to predict in the MNIST dataset (Training accuracy = 0.991 | Testing accuracy = 0.977)
- A Convolutional Neural Network implemented using the PyTorch library.
  - Conv of 32 filters 3x3 - ReLU - MaxPooling - Conv of 64 filters 3x3 - ReLU - MaxPooling - Flatten - Linear with 128 neurons - Dropout - Linear with 10 neurons.
  - This NN is able to train and to predict in the MNIST dataset giving the probabilities of ten digits (0-9) for each input image (Training accuracy = 0.994091 | Testing accuracy = 0.9920873397435898)

### Executing
In order to train and use each of the above described models you can use the following instructions. For each of the approaches, the proper script contains code to train the model and print the measures of the model (accuracy and loss for both training and test sets).

- For the custom Neural Network use:

```bash
python3 part2-nn/neural_nets.py
```

- For the Fully Connected Neural Network use:

```bash
python3 part2-mnist/nnet_fc.py
```

- For the Convolutional Neural Network use:

```bash
python3  part2-mnist/nnet_cnn.py
```

## PART 2 B

This project contains two Neural Network approaches for image classification, using augmented the MNIST data described above. In this subproject each photo contains two handwritten digits (0-9) and our goal is to classify the digit combination correctly. We will use Neural Networks with split outputs, in order to predict separately each digit. More detailed:

- A Fully Connected Neural Network implemented using the PyTorch library.
  - Flatten Layer - Hidden Layer (Dim 64) - 2 similar Output Layers (Dim 10 each).
  - This NN is able to train and to predict in the augmented MNIST dataset the two digits of the given image (Training accuracy for (1st,2nd) digit = (0.924794, 0.916537) | Testing accuracy for (1st,2nd) digit = (0.892137, 0.894657) )
- A Convolutional Neural Network implemented using the PyTorch library.
  - Conv of 32 filters 3x3 - ReLU - MaxPooling - Conv of 64 filters 3x3 - ReLU - MaxPooling - Flatten - Fully connected Linear with 64 neurons - Dropout - 2 similar fully connected Linear outputs with 10 neurons each.
  - This NN is able to train and to predict in the augmented MNIST dataset the two digits of the given image (Training accuracy for (1st,2nd) digit = (0.991520, 0.989796) | Testing accuracy for (1st,2nd) digit = (0.982611, 0.977823) )

### Executing
In order to train and use each of the above described models you can use the following instructions. For each of the approaches, the proper script contains code to train the model and print the measures of the model (accuracy and loss for both training and test sets).

- For the Fully Connected Neural Network use:

```bash
python3 part2-twodigit/mlp.py
```

- For the Convolutional Neural Network use:

```bash
python3  part2-twodigit/conv.py
```