"""
    @Authory Jay Lee
    Utility for working with files, hopefully making things easier
    and also reducing duplicate code when working with files.
"""
import os
import mmap

def read(file_name, write_row=None):
    """
        Simple function for reading a CSV and and adding to a list
        Can be modified to be a generator that yields each row
        :param file_name: The name of the file
        :return: A generator containing each line in the given data file
    """
    result = []
    with open(file_name, "r") as file:
        if not callable(write_row):
            write_row = lambda line: line.strip()
        for line in file:
            yield write_row(line)
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


def get_lines(file_path):
    """
        return an integer representing the number of lines
        in the given file
        :param file_path: Path to the given file
        :return: The number of lines in a file
    """
    with open(file_path, 'r+') as file:
        line_count = 0
        buffer = mmap.mmap(file.fileno(), 0)
        readline = buffer.readline
        while readline():
            line_count += 1
        return line_count


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


def _handle_file_traversal(current_path, current_file_name, caller,
                           is_recursive, traversal_handler, level):
    """
        Private function for handling the logic for getting subfiles (non-folders) recursively
        :param current_path: The current path
        :param current_file_name: Name of the file
        :param caller: The caller of this function
        :param is_recursive: Boolean flag specifying whether this call is a recursive call
        :param traversal_handler: The function that handles the actual traversal
        :param level: The current level from the root path. Starts from 1, which represents files in
        root directory
        :return::return:
    """
    if os.path.isdir(current_path):
        level += 1
        yield from caller(current_path, is_recursive=is_recursive, traversal_handler=traversal_handler, level=level)
    else:
        yield level, current_file_name


def get_files(root_path, is_recursive=False, traversal_handler=None, level=1):
    """
        Generic function for retrieving files from a given path
        :param root_path: The path of the folder from which we will begin traversing.
        Remember that if this is not a folder, an error will be thrown.
        :param is_recursive: If true, will retrieve contents by recursively
        iterating through sub-folders. Otherwise, only retrieves direct children of current folder
        :raises OsError
        :return: Generator: iterating over all the children files (string)
    """
    if not callable(traversal_handler):
        traversal_handler = _handle_file_traversal

    for file in os.listdir(root_path):
        current_path = os.path.join(root_path, file)
        yield from traversal_handler(current_path, file, get_files, is_recursive, traversal_handler, level)


def _handle_subfolder_get(current_path, current_file_name, caller,
                          is_recursive, traversal_handler, level):
    """
        Private function for handling the logic for getting subfolders recursively
        :param current_path: The current path
        :param current_file_name: Name of the file
        :param caller: The caller of this function
        :param is_recursive: Boolean flag specifying whether this call is a recursive call
        :param traversal_handler: The function that handles the actual traversal
        :param level: The current level from the root path. Starts from 1, which represents files in
        root directory
        :return:
    """
    if os.path.isdir(current_path):
        yield level, current_file_name
        level += 1
        yield from caller(current_path, is_recursive=is_recursive, traversal_handler=traversal_handler, level=level)


def get_subfolders(root_path, is_recursive=False):
    """
        :param root_path: The path of the folder from which we will begin traversing.
        Remember that if this is not a folder, an error will be thrown
        :param is_recursive: If true, will recursively grab all sub-folders. Otherwise,
        only retrieves direct children of current folder
        :raises OsError
        :return: List: containing all the sub-folder names (string)
    """
    return get_files(root_path, is_recursive=is_recursive, traversal_handler=_handle_subfolder_get, level=1)


def get_subfiles(root_path, is_recursive=False):
    """
        Returns all files (non-directory) in the given root_path.
        :param root_path: The path of the folder from which we will begin traversing.
        Remember that if this is not a folder, an error will be thrown.
        :param is_recursive: If true, will recursively grab all files (excluding folders). Otherwise,
        only retrieves direct children of current folder.
        :raises OsError
        :return: Generator: iterating over all the children files (string)
    """
    return get_files(root_path, is_recursive=is_recursive, level=1)


# test functionality
if __name__ == "__main__":
    from pathlib import Path
    home = str(Path.home())
    folders = get_subfolders(home + "/Videos", is_recursive=True)
    for folder in folders:
        print(folder)

    print("-" * 60)

    # Sorted according to hierarchy
    for file_name in sorted(get_subfiles(home + "/Videos", is_recursive=True)):
        print(file_name)