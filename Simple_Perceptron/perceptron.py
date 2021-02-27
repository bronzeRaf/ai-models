import numpy as np


def main():
    x = np.array([
        [-1, 0],
        [0, 1],
    ])

    y = np.array([1, 1])


    perceptron(x, y)


def perceptron(x, y):
    print('hi')
    w = np.zeros(len(x[0]))
    #w= np.array([18, 23])
    #w0 = 0
    eta = 1
    epochs = 10

    for t in range(epochs):
        for i, xx in enumerate(x):
            if ((np.dot(x[i], w) )* y[i]) <= 0:
                w = w + eta * x[i] * y[i]
                #w0 = w0 + y[i]
                print(w)
                #print(w0)

    return w

if __name__ == "__main__":
    main()
