from os import listdir
from pathlib import Path
from typing import Dict, List
from matplotlib.axes import Axes
from matplotlib.patches import Circle
import matplotlib.pyplot as plt
import numpy as np


def read_pts(file: Path, round: bool = False) -> np.ndarray:
    """Reads set of (x, y) coordinates from a .pts file

    Parameters
    ----------
    file : Path
        Path to .pts file
    round : bool
        If True, rounds each coordinate to the nearest int

    Returns
    -------
    np.ndarray
        Array of (x,y) coordinates, one per point
    """
    # 68 points => 68 (x,y)-pairs
    pts = np.zeros((68, 2))
    # open the file in read mode
    with open(file, 'r') as f:
        # skip the first three lines and the last line
        for (i, line) in enumerate(f.readlines()[3:-1]):
            # split the line on the space and strip any extra whitespace
            x, y = map(lambda p: p.strip(), line.split(' '))
            # put it in our array, rounding if desired
            pts[i, 0], pts[i, 1] = x, y if not round else round(x), round(y)
    return pts


def read_pts_dir(dir: Path) -> Dict[str, np.ndarray]:
    """Reads an entire directory of .pts files

    Parameters
    ----------
    dir : Path
        Path to points directory

    Returns
    -------
    Dict[str, np.ndarray]
        Maps image/point ID to array of landmark (x,y) points for that image
    """
    return {
        file.split('/')[-1].split('.')[0]: read_pts(file)
        for file in listdir(dir)
    }


def label_image(image: np.ndarray, landmarks: np.ndarray, ax: Axes) -> Axes:
    """Displays landmark points on an image.

    Parameters
    ----------
    image : np.ndarray
        [description]
    landmarks : np.ndarray
        [description]
    ax : Axes
        [description]

    Returns
    -------
    Axes
        [description]
    """
    ax.imshow(image)
    for (x, y) in landmarks:
        ax.add_patch(Circle((x, y), 5))

    return ax
