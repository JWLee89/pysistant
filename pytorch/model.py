"""
    @Author Jay Lee
    All model helpers for Pytorch are included here.
"""

from pysistant.util import validation
import torch.nn as nn
from abc import ABC, abstractmethod


class Model(ABC):
    """
        Abstract  Base Class for defining models
    """
    def __init__(self, layers):
        self.layers = layers
        self.__init_layer()

    def __init_layer(self):
        if validation.isiterable(self.layers):
            for layer in self.layers:
                pass
        else:
            raise ValueError("layers must be an iterable object")

    def __repr__(self):
        """
            String representation of the model
            :return:
        """
        return "a custom model"

    @abstractmethod
    def fit(self, X):
        """
            In order to fit a neural network, we need to provide
            input data. Y is not provided initially, but upon definition
            of the actual Model.
            :param X: The input data
            :return:
        """
        def do_fit():
            """
            Fit the model according
            :return:
            """

    def load(self, load_path):
        """
            Load model from a file.
            :param load_path: The path from where to load a model
            :return:
        """
        pass

    def save(self, save_path):
        """
            Save the model to a specified directory with a specific name
            :param save_path: The name and path of the target save file
            :return:
        """
        pass



class Layer:
    """
        A layer of a neural network
    """
    def __init__(self, input_size, output_size, layer_type=nn.Linear, activation=None):
        """
            :param input_size: The input size of a neural network layer
            :param output_size: The output size of a neural network layer
            :param activation: An activation function to be applied to the output
        """
        self.input_size = input_size
        self.output_size = output_size
        self.activation = activation
        self.layer_type = layer_type

    def __repr__(self):
        """
            String representation of the layer
            :return:
        """
        return f"Dim: ({self.input_size} X {self.output_size}). Activation: {self.activation}." \
               f" Layer type: {self.layer_type}"


if __name__ == "__main__":
    model = Model([Layer(128, 64, activation=nn.ReLU)])
    print(model)