"""
    @Author Jay Lee
    A simple utility fo handling files that I am working on
    as needs occur. Code will be added depending on what kind of needs
    I come across during the course of projects and classes.
    Primarily also for a way for me to get used to Python.
"""

def read(file_name):
    """
        Simple function for reading a CSV and and adding to a list
        Can be modified to be a generator that yields each row
        :param file_name: The name of the file
        :return:
    """
    result = []
    with open(file_name, "r") as file:
        for line in file:
            result.append(line)
    return result


def write(file_path, data, handle_write=None):
    """
    Write to file: Can accept a raw string or an iterable object.
    :param file_path:
    :param data:
    :return:
    """
    with open(file_path, 'w') as file:
        try:
            file_iter = iter(file)
        except TypeError:
            # Cannot iterate
            file.write(data)
        else:
            # Iterable item. Check if handle_write is defined
            # TODO: Refactor this so that duplicate data is not included
            if callable(handle_write):
                for row in data:
                    handle_write(row)
            else:
                for row in data:
                    file.write(row)


def combine_file_instances(file_name, import_file_names):
    """
        Quick and dirty approach for writing to a file
        :param file_name: The name of the file that we are aiming to write
        :param import_file_names: The name of the files that we will be importing
        :return:
    """
    data = []
    # TODO: Add error handling later on. Let's just get this to work first
    for file_name in import_file_names:
        data.append(read(file_name))

    result = []
    for csv_data in data:
        for row in csv_data:
            result.append(row)
        result.append('\n')

    # Remove trailing new line character
    del result[-1]
    write(file_name, result)