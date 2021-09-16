"""Ben Haws 9/13/2021
   DATA51100 Fall 2021
   PROGRAMMING ASSIGNMENT #3"""

import numpy as np


def main():

    # Get training data and labels into ndarrays
    with open('iris-training-data.csv') as f:
        training_data = np.loadtxt(f, usecols = (0, 1, 2, 3), delimiter = ',')

    with open('iris-training-data.csv') as f:
        training_labels = np.loadtxt(f, usecols = 4, delimiter = ',', dtype = str)

    # Get test data and labels into ndarrays
    with open('iris-testing-data.csv') as f:
        testing_data = np.loadtxt(f, usecols = (0, 1, 2, 3), delimiter = ',')

    with open('iris-testing-data.csv') as f:
        testing_labels = np.loadtxt(f, usecols = 4, delimiter = ',', dtype = str)

    # create a distance matrix using np.linalg.norm (a built in function for
    # calculating norm/Euclidean distance). This assignment uses
    # broadcasting rules to vectorize the distance calculating
    # NOTE TO DR ABUOMAR: CAN WE PLEASE, PLEASE, PLEASE GO OVER BROADCASTING RULES??
    # WHAT I HAVE WORKS, BUT I HARDLY UNDERSTAND THE BROADCASTING PART

    # Modify test & train data for broadcasting by adding axes
    training_data2 = training_data[:, np.newaxis, :]
    testing_data2 = testing_data[np.newaxis, :, :]

    # Calculate distance matrix by calculating a vector of all distances
    # for each set of training data
    distance_matrix = np.linalg.norm(training_data2 - testing_data2, axis = -1)

    # use np.argmin() to return the indices of the minimum values on each row
    predictions = training_labels[np.argmin(distance_matrix, axis = 1)]

    # Compare predictions with ground truth labels
    correct = sum(predictions == testing_labels)
    accuracy = correct / len(testing_labels) * 100

    # Print predicted and actual values & accuracy
    print('#, True, Predicted')
    for x, y in enumerate(zip(testing_labels, predictions)):
        print(x + 1, ', ', ','.join(y))

    # Set precision for printing accuracy
    np.set_printoptions(precision = 4)
    print('Accuracy: ', "%.2f" % round(accuracy, 2), '%')

    return


if __name__ == '__main__':
    main()
