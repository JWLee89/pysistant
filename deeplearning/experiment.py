"""
    @Author Jay Lee
    Utility function for running experiments
    TODO
"""
def run_experiments(hyperparameters, save_dir):
    """
        Run experiments using the specified parameters
        :param hyperparameters:
        :param save_dir:
        :return:
    """
    for hyperparameter_set in hyperparameters:
        # For each specific experiment instance
        for parameter_key in hyperparameter_set.keys():
            pass



def do_hyperparameter_search(hyperparameters, save_dir, do_count=1000):
    """
        Conduct an exhaustive hyperparameter search for all the given
        parameters.

        until we have conducted the experiment {do_count} times for each parameter:
            run experiment(current_parameters)
            update parameters

        :param hyperparameters: The set of hyperparameters to search_by
        :param save_dir:
        :return:
    """
    

