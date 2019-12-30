"""
    @Author Jay Lee
    All model helpers for Pytorch are included here.
"""

from pysistant.util import validation
import torch.nn as nn
import torch


class Model:
    """
        Abstract  Base Class for defining models
    """

    def __init__(self, layers, learning_rate=0.001, optimizer=torch.optim.Adam):
        self.layers = layers
        self.__init_layers()
        self.learning_rate = learning_rate
        self.optimizer = optimizer
        print("Model initialized")

    def __init_layers(self):
        """
            Initialize the layers.
            :return:
        """
        if validation.isiterable(self.layers):
            size = len(self.layers)
            # Must contain at least input and output layer
            # for this to be a valid network
            if size >= 1:
                for i in range(size - 1):
                    self.__init_layer(i,
                                      self.layers[i], self.layers[i + 1])
            else:
                raise ValueError("Must contain at least one layer.")
        else:
            raise ValueError("layers must be an iterable object")

    def __init_layer(self, index, input_size, output_size):
        """
            Logic for initializing a single layer
            :param index: The current index in layers
            :param input_size: The size of the input into this layer
            :param output_size: The dimensions of the output for current layer
            :return:
        """
        layer_sizes = [input_size, output_size]
        if validation.are_instances_of(layer_sizes, int):
            layer = Layer(input_size, output_size)
        elif isinstance(input_size, Layer):
            # Do nothing, since we already have a valid layer object
            layer = input_size
        else:
            raise ValueError("Please specify either a Layer object or an integer")
        self.layers[index] = layer

    def __repr__(self):
        """
            String representation of the model
            :return:
        """
        return "a custom model"

    def fit(self, *inputs, epochs=500, learning_rate=0.001):
        """
            In order to fit a neural network, we need to provide
            input data. Y is not provided initially, but upon definition
            of the actual Model.
            :param X: The input data
            :parm epochs: The number of epochs of training
            :return:
        """
        raise NotImplementedError

    def load(self, load_path):
        """
            Load model from a file.
            :param load_path: The path from where to load a model
            :return:
        """
        print("loading model")

    def save(self, save_path):
        """
            Save the model to a specified directory with a specific name
            :param save_path: The name and path of the target save file
            :return:
        """
        pass


class MLP(Model):
    """
        A simple implementation of the Multi-layer perceptron
    """

    def __init__(self, layers, **kwargs):
        super(MLP, self).__init__(layers, **kwargs)

    def fit(self, *args, **kwargs):
        print("test")

    def __repr__(self):
        result = f"MLP (lr: {self.learning_rate}, optimizer: {self.optimizer}): \n"
        for layer in self.layers:
            result += '\t'
            result += repr(layer)
        return result


class Layer:
    """
        A layer of a neural network
    """

    def __init__(self, input_size, output_size, layer=nn.Linear, activation=None):
        """
            :param input_size: The input size of a neural network layer
            :param output_size: The output size of a neural network layer
            :param activation: An activation function to be applied to the output
        """
        self.input_size = input_size
        self.output_size = output_size
        self.activation = activation
        self.layer = layer(input_size, output_size)

        # Initialize action e.g. nn.ReLU
        if self.activation is not None:
            self.activation = self.activation()

    def __repr__(self):
        """
            String representation of the layer
            :return:
        """
        return f"Dim: ({self.input_size} X {self.output_size}). Activation: {self.activation}." \
               f" Layer type: {self.layer}"

    def fit(self):
        pass


if __name__ == "__main__":
    model = MLP([Layer(784, 64, activation=nn.ReLU)])
    print(model)
    model.load("test")
