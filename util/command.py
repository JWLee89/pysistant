"""
    @Author Jay Lee
    This file will contain some utility functions for commands
    that will be useful for automating tasks via the command line.
"""
import argparse
from pysistant.io.file import read
from pathlib import Path
from pysistant.util.validation import *
import subprocess


def shell(cmd):
    """
        Simple function for calling the shell
        :param cmd:
        :return:
    """
    subprocess.call(cmd, shell=True)


def run_from_file(file_path):
    """
        Run Python script from a file. E.g. Let's say we have the following text
            python test.py --num 1
            python test.py --num 2
            python test.py --num 3
            python test.py --num 4
            python test.py --num 5
        :param file_path: The path of the file to read
        :return:
    """
    for script_line in read(file_path):
        shell(script_line)


def run_python_script(script_path, arguments):
    """
        Run python script programmatically. Very useful for performing experiments
        by setting a variety of hyperparameters.

        Use cases:
        - deep learning model training or testing assuming that we are able to pass
       arguments to control hyperparameters

        :param script_path: The name of the script file that we want to run
        :param arguments: A list of arguments to be passed to the python script
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
            get_argparser(argument)
    elif isinstance(arguments, str):
        get_argparser(arguments)
    else:
        raise TypeError("Arguments must either be a string or a iterable object of strings E.g. list or tuple")


def parse_arg_string():
    """
    Parse the string into an appropriate data structure for us to process
    e.g. -a --argument default 10 help 'this is a sample argument'
    :return:
    """
    pass


def get_argparser(command_line_args, argparser=None, description='Generic command line arguments'):
    """
        Create a new argparser object with dynamically added command line args
        :param command_line_args: Should be an iterable item that contains a dictionary
        filled with options for the argparse API
        :param argparser: the argparse object to add arguments to. If not defined, a new argparse
        instance will be created
        :param description: description Description of the argument parser
        :return:
    """
    # Lazy load argument parser. Or otherwise, continue to add arguments
    # onto existing parser
    if not isinstance(argparser, argparse.ArgumentParser):
        argparser = argparse.ArgumentParser(description=description)

    if isinstance(command_line_args, str):
        # TODO: Handle logic for processing string
        pass
    # Iterable object
    elif issequence(command_line_args):
        # Add all the necessary command_line arguments
        for i, argument in enumerate(command_line_args):
            arg_size = len(argument)
            # argument => (-shortcut, --command_name, kwargs)
            if arg_size == 3:
                argparser.add_argument(argument[0], argument[1], **argument[2])
            elif arg_size == 2:
                argparser.add_argument(argument[0], **argument[1])
            else:
                raise ValueError("Invalid argument passed at index: ", i, ". Object: ", argument)
    else:
        raise ValueError("Input type: ", type(command_line_args), ". Please pass in a sequence or a string")
    return argparser


if __name__ == "__main__":
    run_python_script("/home/jay/software/git_repositories/T-GCN/gcn.py", ['test', 'teemo'])
    argparse = get_argparser([
        ['-lr', '--learning_rate', {
            'default': 0.001
        }]
    ])
    args = vars(argparse.parse_args())
    print(args)