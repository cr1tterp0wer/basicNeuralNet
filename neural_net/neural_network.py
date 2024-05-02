import numpy
import scipy.special

class NeuralNetwork:
    """
    Neural Network class
    """

    def __init__(self, input_nodes, hidden_nodes, output_nodes, learning_rate):
        # The number of nodes per each layer (input, hidden, output)
        self.inodes = input_nodes
        self.hnodes = hidden_nodes
        self.onodes = output_nodes

        self.weights_i_h = self.random_matrix(self.inodes, self.hnodes)
        self.weights_h_o = self.random_matrix(self.hnodes, self.onodes)

        # Learning Rate
        self.learn_rate = learning_rate
        self.activation_function = lambda x: scipy.special.expit(x)

    def train(self):
        """
        Train the model
            Calculate output
            Backpropagate Errors
        """

    def query(self, inputs_list):
        """
        Query the model
        Dot Product both Input matrix and hidden weights
        Sigmoid the result
            X_hidden = W_i,h * I
            O_hidden = sigmoid(X_hidden)
        """
        # Convert inputs into 2D array
        inputs = numpy.array(inputs_list, ndmin=2).T

        # X_hidden = W_i,h * I
        hidden_inputs = numpy.dot(self.weights_i_h, inputs)
        # O_hidden = sigmoid(X_hidden)
        hidden_outputs = self.activation_function(hidden_inputs)

        # Calculate signals into Output Layer
        final_inputs = numpy.dot(self.weights_h_o, hidden_outputs)
        # Calculate signals emerging from Output Layer
        final_outputs = self.activation_function(final_inputs)

        return final_outputs

    def random_matrix(self, inodes, onodes):
        """
        Set weights using rands between -0.5...0.5
        @inodes: number of input nodes
        @onodes: number of output nodes
        """
        ih_size = (onodes, inodes)
        return numpy.random.uniform(-0.5, 0.5, ih_size)

    def random_distribution_matrix(self, inodes, onodes):
        """
        Set weights using a more sophisticated approach
        Use a normal distribution.
        Center = 0
        Standard deviation = 1/sqrt(num_incoming_links)
        """
        ih_size = (onodes, inodes)
        return numpy.random.normal(0.0, pow(self.onodes, -0.5), ih_size)

    def set_weights(self, use_distribution=True):
        """
        Set weights
        """
        if use_distribution:
            self.weights_i_h = self.random_distribution_matrix(self.inodes, self.hnodes)
            self.weights_h_o = self.random_distribution_matrix(self.hnodes, self.onodes)
            return
        self.weights_i_h = self.random_matrix(self.inodes, self.hnodes)
        self.weights_h_o = self.random_matrix(self.hnodes, self.onodes)

    def to_string(self):
        """
        Describe Member values
        """
        print(f"\nInput Layer Node count: {self.inodes}")
        print(f"Hidden Layer Node count: {self.hnodes}")
        print(f"Output Layer Node count: {self.onodes}")
        print(f"Learning Rate: {self.learn_rate}\n")
        print(f"Weights, INPUT -> HIDDEN: \n{self.weights_i_h}\n")
        print(f"Weights, HIDDEN -> OUTPUT: \n{self.weights_h_o}\n")
