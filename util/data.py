import sys
import importlib
argparse_module_name = 'argparse'


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

    ap = argparse.ArgumentParser(description=description)

    # Add all the necessary command_line arguments
    for i, argument in enumerate(command_line_args):
        arg_size = len(argument)
        # argument => (-shortcut, --command_name, kwargs)
        if arg_size == 3:
            ap.add_argument(argument[0], argument[1], **argument[2])
        elif arg_size == 2:
            ap.add_argument(argument[0], **argument[1])
        else:
            raise ValueError("Invalid argument passed at index: ", i, ". Object: ", argument)
    return ap


def _generate_experiment_commands(experiment_count):
    command_line_args = []
    for experiment_no in range(experiment_count):
        command_line_args.append('')


if __name__ == "__main__":
    # argparse = add_command_line_args([
    #     '-a, --test, required=True, default=10'
    # ])
    argparse = add_command_line_args([
        ['-lr', '--learning_rate', {
            'default': 0.001
        }]
    ])
    args = vars(argparse.parse_args())
    print(args)