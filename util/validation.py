"""
    @Author Jay Lee
    Set of utility functions for handling sanity check
"""
import os


def isiterable(target):
    """
        Check if target object is iterable
        :param target:
        :return: true if target is iterable. Otherwise, return false
    """
    try:
        iter(target)
    except:
        return False
    else:
        return True


def hasextension(path, extension):
    """
       Check to see if file has a certain extension.
       e.g. isextension('hello.txt', '.txt') => True
       :param path: The path / name of the file.
       :return:
    """
    _, file_extension = os.path.splitext(path)
    return file_extension == extension


def ispython(script_path):
    """
    Check to see if file is a python script file by extension
    :param script_path:
    :return:
    """
    return hasextension(script_path, ".py")