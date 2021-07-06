from os import listdir
from pathlib import Path
from typing import Dict, List
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
    pts = np.zeros((68, 2))
    with open(file, 'r') as f:
        lines = f.readlines()[3:-1]
        for (i, line) in enumerate(lines):
            x, y = map(lambda p: p.strip(), line.split(' '))
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
    return {file.split('/')[-1]: read_pts(file) for file in listdir(dir)}
