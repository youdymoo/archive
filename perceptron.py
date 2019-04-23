from algorithms.matrix import multiply

class Perceptron(object):

    def __init__(self, num_inputs, threshold=100, learning_rate=0.01):
        self.threshold = threshold
        self.learning_rate = learning_rate
        self.weights = []
        for i in range(num_inputs + 1)
            self.weights.append(0.0)

    def predict(self, inputs):
        sum = multiply.multiply(inputs, self.weights[1:]) + self.weights[0]
        if sum > 0: activation = 1
        else: activation = 0
        return activation

    def train(self, training_inputs, labels):
        for _ in range(self.threshold):
            for inputs, label in zip(training_inputs, labels):
                prediction = self.predict(inputs)
                self.weights[1:] += self.learning_rate * (label - prediction) * inputs
                self.weights[0] += self.learning_rate * (label - prediction)
