import time


def get_current_time_ms():
    """
        Get current time in milliseconds
        :return:
    """
    return int(round(time.time() * 1000))


def time_method():
    """
        A Decorator for measuring the amount of time elapsed for a given function.

        :return:
    """
    pass

if __name__ == "__main__":
    start_time = get_current_time_ms()
    for i in range(1000000000):
        pass
    end_time = get_current_time_ms()
    print(f"Time elapsed: {end_time - start_time}")