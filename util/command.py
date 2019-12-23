"""
    @Author Jay Lee
    This file will contain some utility functions for commands
    that will be useful for automating tasks via the command line.
"""
import runpy
import os
import sys
from pathlib import Path
from pysistant.util.validation import isiterable, ispython
argparse_module_name = 'argparse'


def run_python_script(script_path, arguments, do_async=False):
    """
        Run python script programmatically. Very useful for performing experiments
        by setting a variety of hyperparameters.

        Use cases:
        - deep learning model training or testing assuming that we are able to pass
       arguments to control hyperparameters

        :param script_path: The name of the script file that we want to run
        :param arguments: A list of arguments to be passed to the python script
        :param do_async: Perform the execution of the script asynchronously.
        Useful if the script is not dependant upon the main program's outputs.
        :return:
    """

    # Sanity check for file
    if os.path.isfile(script_path) and ispython(script_path):
        # cd to specified directory where script is located
        parent_directory = Path(script_path).resolve().parent
        os.chdir(parent_directory)
    else:
        raise ValueError("The path: ", script_path, " is not a valid python file or is a directory. "
                                                    "Please check the spelling and path specified.")

    # File must be iterable
    if isiterable(arguments):
        for argument in arguments:
            add_command_line_args(argument)
    elif isinstance(arguments, str):
        add_command_line_args(arguments)
    else:
        raise TypeError("Arguments must either be a string or a iterable object of strings E.g. list or tuple")


def create_sh():
    """
        TODO: Utility function for creating shell scripts on the fly.
        :return:
    """


def add_command_line_args(command_line_args, description='Generic command line arguments'):
    """
        :param command_line_args Should be an iterable item that contains a dictionary
        filled with options for the argparse API
        :param description Description of the argument parser

        Raises Value Error if argument is not found
    """
    # Import argparse if needed. Otherwise, don't import
    if argparse_module_name not in sys.modules:
          import argparse
    else:
        argparse = sys.modules['argparse']

    parser = argparse.ArgumentParser(description=description)

    # Add all the necessary command_line arguments
    for i, argument in enumerate(command_line_args):
        arg_size = len(argument)
        # argument => (-shortcut, --command_name, kwargs)
        if arg_size == 3:
            parser.add_argument(argument[0], argument[1], **argument[2])
        elif arg_size == 2:
            parser.add_argument(argument[0], **argument[1])
        else:
            raise ValueError("Invalid argument passed at index: ", i, ". Object: ", argument)
    return parser


if __name__ == "__main__":
    run_python_script("/home/jay/software/git_repositories/T-GCN/gcn.py", ['test', 'teemo'])

    argparse = add_command_line_args([
        ['-lr', '--learning_rate', {
            'default': 0.001
        }]
    ])
    args = vars(argparse.parse_args())
    print(args)