import numpy as np

class KNNReg:
    def __init__(self, k):
        self.k = k
        self.X = None
        self.Y = None

    def fit(self, X, Y):
        self.X = np.array(X)
        self.Y = np.array(Y)

    def Euclidean(self):
        # Euclidean
        distance = 0
        for i in range(len(self.X)):
            distance += (self.X[i] + self.Y[i])**2
        eu_dist = np.sqrt(distance)
        return eu_dist
    
    def predict(self, x):
        distances = np.sqrt(np.sum((self.X - x) ** 2, axis=1))
        sorted_indices = np.argsort(distances)
        k_nearest_neighbors = sorted_indices[:self.k]
        return np.mean(self.Y[k_nearest_neighbors])

def main():

    # Ask user for number of inputs
    N = int(input("Enter the number of positive integers: "))
    k = int(input("Enter the value of k for kNN: "))

    # Initialize kNN
    knn_reg = KNNReg(k)

    # Create array for X and Y
    X = []
    Y = []

    # Ask user for input for x and y
    for i in range(N):
        # Values in float and not int
        x_value = float(input(f"Enter x value for point {i + 1}: "))
        y_value = float(input(f"Enter y value for point {i + 1}: "))

        # Add user inputs to respective array
        X.append(x_value)
        Y.append(y_value)

    # Fit the model with the data
    knn_reg.fit(X, Y)

    # Input the value of X for prediction
    x_to_predict = float(input("Enter the value of X for prediction: "))

    # Predict Y using kNN Regression
    if k <= N:
        predicted_y = knn_reg.predict(np.array([x_to_predict]))
        print(f"The predicted Y for X = {x_to_predict} is: {predicted_y}")
    else:
        print("Error: k should be less than or equal to N for k-NN Regression.")

if __name__ == "__main__":
    main()