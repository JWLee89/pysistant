import matplotlib.pyplot as plt
import numpy as np
import runpy


def image(data, figure=None, axes=None, figsize=(5, 3)):
    """
        Use object oriented programming approach to create Matplotlib
        objects that will be used to plot images.
        :param data The data that we want to visualize as an image.
        Will generally be a 2 or 3 dimensional array of values between 0 and 255.
        E.g.
            [
                [col1, col2, col3],
                [col1, col2, col3]
            ]
    """
    # Convert data to numpy array
    if not isinstance(data, np.ndarray):
        # Pixels are integers between 0 and 255
        data = np.array(data, dtype=np.uint8)

    if figure is None:
        # Create figure object, the container for all plots
        figure, axes = plt.subplots(figsize=figsize)

    print(type(figure))



    # for key in kwargs.keys():
    #     print(f"Key: {key}. Value: {kwargs[key]}")


if __name__ == "__main__":
    runpy.run_path("../util/data.py")