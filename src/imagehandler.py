from pathlib import Path
from typing import Tuple
from matplotlib.axes import Axes
from matplotlib.figure import Figure
from matplotlib.patches import Circle
import matplotlib.pyplot as plt
import numpy as np


class ImageHandler:
    """[summary]
    """

    def __init__(
        self,
        image_dir: Path = Path("data/FGNET/images"),
        points_dir: Path = Path("data/FGNET/points")
    ) -> None:
        self.image_dir: Path = image_dir
        self.points_dir: Path = points_dir

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
        points = np.round(self.read_pts(self.points_dir.joinpath(image_id)))

        ax.imshow(image)
        for (x, y) in points:
            ax.add_patch(Circle((x, y), 5))

        return ax
