"""
    @Author Jay Lee
    A simple utility fo handling files that I am working on
    as needs occur. Code will be added depending on what kind of needs
    I come across during the course of projects and classes.
    Primarily also for a way for me to get used to Python.
"""


def read(file_name, write_row=None):
    """
        Simple function for reading a CSV and and adding to a list
        Can be modified to be a generator that yields each row
        :param file_name: The name of the file
        :return:
    """
    result = []
    with open(file_name, "r") as file:
        if not callable(write_row):
            write_row = lambda line: line.strip()
        for line in file:
          result.append(write_row(line))
    return result


def write(file_path, data, write_row=None):
    """
    Write to file: Can accept a raw string or an iterable object.
    :param file_path: The path of the file to write data to
    :param data: The data to write
    :return: Nothing. Just simply writes to the file.
    """
    with open(file_path, 'w') as file:
        try:
            iter(file)
        except TypeError:
            file.write(data)
        else:
            # assign custom method to do_write if it exists.
            # Otherwise, fallback to built-in write method
            do_write = file.write
            if callable(write_row):
                do_write = write_row
            for row in data:
                do_write(row)


def combine_files(file_name, import_file_names):
    """
        Quick and dirty approach for combining the data in the user-defined
        import files and outputting the combined data onto a single file.
        :param file_name: The name of the file that we are aiming to write
        :param import_file_names: The name of the files that we will be combining
        :return:
    """
    data = []
    # TODO: Add error handling later on. Let's just get this to work first
    for current_file in import_file_names:
        data.append(read(current_file))

    result = []
    # Maybe we can optimize this in the future as well.
    for csv_data in data:
        for row in csv_data:
            result.append(row)
        result.append('\n')

    # Remove trailing new line character
    del result[-1]
    # Lastly, write to file
    write(file_name, result)


def get_subfolders(root, nested=False):
    """
    :param root: The folder from which we will begin traversing.
    Remember that if this is not a folder, an error will be thrown
    :param nested: If true, will recursively grab all sub-folders. Otherwise,
    only retrieves direct children of current folder
    :raises OsError
    :return:
    """
    import os
    # Check if it is directory
    if not os.path.isdir(root):
        raise ValueError("The path: ", root, " is not a valid folder")

    # Change directory
    # Not sure if this is the best approach
    os.chdir(root)
    if nested:
        return os.walk(root)

    # Return direct sub-directory
    return next(os.walk('.'))[1]


# test functionality
if __name__ == "__main__":
    folders = get_subfolders("folder name")
    for folder in folders:
        print(folder)