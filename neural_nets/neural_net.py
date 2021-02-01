import numpy as np


def initialize_network(num_inputs, num_hidden_layers, num_nodes_hidden, num_nodes_output):
    num_nodes_previous = num_inputs  # number of nodes in the previous layer

    network = {}

    # loop through each layer and randomly initialize the weights and biases associated with each layer
    for layer in range(num_hidden_layers + 1):

        if layer == num_hidden_layers:
            layer_name = 'output'  # name last layer in the network output
            num_nodes = num_nodes_output
        else:
            layer_name = 'layer_{}'.format(layer + 1)  # otherwise give the layer a number
            num_nodes = num_nodes_hidden[layer]

            # initialize weights and bias for each node
        network[layer_name] = {}
        for node in range(num_nodes):
            node_name = 'node_{}'.format(node + 1)
            network[layer_name][node_name] = {
                'weights': np.around(np.random.uniform(size=num_nodes_previous), decimals=2),
                'bias': np.around(np.random.uniform(size=1), decimals=2),
            }

        num_nodes_previous = num_nodes

    return network  # return the network


def compute_weighted_sum(inputs, weights, bias):
    return np.sum(inputs * weights) + bias


def node_activation(weighted_sum):
    return 1.0 / (1.0 + np.exp(-1 * weighted_sum))


small_network = initialize_network(5, 3, [3, 2, 3], 1)

np.random.seed(12)
inputs_ = np.around(np.random.uniform(size=5), decimals=2)

print('The inputs to the network are {}'.format(inputs_))

node_weights = small_network['layer_1']['node_1']['weights']
node_bias = small_network['layer_1']['node_1']['bias']

weighted_sum_ = compute_weighted_sum(inputs_, node_weights, node_bias)
print('The weighted sum at the first node in the hidden layer is {}'.format(np.around(weighted_sum_[0], decimals=4)))

node_output  = node_activation(weighted_sum_)
print('The output of the first node in the hidden layer is {}'.format(np.around(node_output[0], decimals=4)))