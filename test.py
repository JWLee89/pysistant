"""
TODO: Run a script that executes a list of given tests and ensures that they all pass
"""
from pysistant.util import command
import torch

if __name__ == "__main__":
    command.run_python_script("/home/jay/software/git_repositories/T-GCN/gcn.py", ['test', 'teemo'])
    print(torch.__version__)