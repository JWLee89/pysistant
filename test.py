"""
TODO: Run a script that executes a list of given tests and ensures that they all pass
"""
from pysistant.util import command

if __name__ == "__main__":
    # command.run_python_script("/home/script.py", ['test', 'teemo'])
    command.shell("tmux new-session")