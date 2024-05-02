import numpy
# Driver Program
from neural_network import NeuralNetwork as network

INPUT_NODES  = 3
HIDDEN_NODES = 3
OUTPUT_NODES = 3

LEARNING_RATE = 0.3

net = network(INPUT_NODES, HIDDEN_NODES, OUTPUT_NODES, LEARNING_RATE)
net.set_weights() # Use Standard Deviation Approach
net.to_string()

input_data = (1.0, 0.5, -1.5)
print(f'Input Data: {input_data}')
query = net.query(input_data)
print(f'Query Results:\n{query}')


# Generate random matrix[x]; {x| x<1; x>0}
# print(numpy.random.rand(3,3))

# Generate random matrix[size(x)]; {x| x>-1; x<1}
# size = (3,3)
# print(numpy.random.uniform(-0.5, 0.5, size))
