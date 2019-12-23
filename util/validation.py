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


def issequence(target):
    """
        Check if item is a sequence. If it has "strip" method, it is a string and not a
        tuple or a list
        @credit to stevenha on stackoverflow and the following link for this method
        https://stackoverflow.com/questions/1835018/how-to-check-if-an-object-is-a-list-or-tuple-but-not-string
        :param target: The target to be evaluated
        :return: boolean indicating whether the target is a sequence
    """
    return (not hasattr(target, 'strip') and hasattr(target, "__getitem__")
            or hasattr(target, "__iter__"))


def srepr(target):
    """
        Get the string representation of the target
        @credit to stevenha on stackoverflow and the following link for this method
        https://stackoverflow.com/questions/1835018/how-to-check-if-an-object-is-a-list-or-tuple-but-not-string
        :param target:
        :return:
    """
    if issequence(target):
        return '<' + ", ".join(srepr(x) for x in target) + '>'
    return repr(target)