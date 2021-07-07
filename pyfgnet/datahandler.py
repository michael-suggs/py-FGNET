"""Module handling landmark loading and use.
"""
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Optional, Tuple
from matplotlib.axes import Axes
from matplotlib.figure import Figure
from matplotlib.patches import Circle
import matplotlib.pyplot as plt
import numpy as np


@dataclass
class ImageLandmarkPair:
    """Holds an image array and its associated landmark points array.

    Attributes
    ----------
    image : np.ndarray
        Image array, imported via matplotlib
    points : np.ndarray
        2D array (68x2) of (x,y)-points (landmark feature points)
    """
    image: np.ndarray
    landmarks: np.ndarray


class DataHandler:
    """Handles loading and storage of image and landmark data.

    Attributes
    ----------
    image_dir : Path
        Relative path to directory containing the images
    point_dir : Path
        Relative path to directory containing landmark points for those images
    data : Dict[str, ImageLandmarkPair], default None
        Maps ID to dataclass containing image array and array of its
        associated landmark points

    Methods
    -------
    """

    def __init__(
        self,
        image_dir: Path = Path("data/FGNET/images"),
        point_dir: Path = Path("data/FGNET/points")
    ) -> None:
        self.image_dir: Path = image_dir
        self.point_dir: Path = point_dir
        self.data: Optional[Dict[str, ImageLandmarkPair]] = None

    @staticmethod
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

    def label_image(self, image_id: str, ax: Axes) -> Axes:
        """Displays points from a .pts file on its respective image

        Parameters
        ----------
        image_id : str
            Name of image to label

        Returns
        -------
        Tuple[Figure, Axes]
            pyplot components of labeled image, ready for display
        """
        image = plt.imread(self.image_dir.joinpath(image_id))
        points = np.round(self.read_pts(self.point_dir.joinpath(image_id)))

        ax.imshow(image)
        for (x, y) in points:
            ax.add_patch(Circle((x, y), 5))

        return ax
