import io
import json
import pkgutil

import matplotlib.pyplot as plt


def load_data() -> dict:
    data = json.loads(
        pkgutil.get_data("packagename", "data/example.json").decode("utf-8")
    )
    return data


def show_lena():
    """Draw a pokemon sprite.

    Args:
        pokemon_name (str): A valid pokemon name.
        ax (matplotlib.axes.Axes or None, optional): Axis to draw the sprite on. Defaults to None.
            If None, create an axis in the top-right corner of the current figure.

    Returns:
        matplotlib.axes.Axes: The axis that contains the pokemon sprite.
    """
    path = f"data/images/lena.png"
    data = pkgutil.get_data("packagename", path)
    sprite_io = io.BytesIO(data)
    sprite = plt.imread(sprite_io)
    plt.imshow(sprite)
    plt.axis("off")
