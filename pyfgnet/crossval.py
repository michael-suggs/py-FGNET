from functools import singledispatchmethod
from typing import Generator, Tuple, Union
import numpy as np
import pandas as pd


class LOPOCV:

    def __init__(self, n_splits: int) -> None:
        pass

    @singledispatchmethod
    def split(self, X, y, groups=None):
        raise Exception(
            'Both X and y must be either a numpy array or DataFrame.'
        )

    @split.register
    def _(self, X: np.ndarray, y: np.ndarray, groups=None):
        ...

    @split.register
    def _(
        self, X: pd.DataFrame, y: Union[pd.DataFrame, pd.Series], groups=None
    ) -> Generator[Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame], None, None]:
        Xy = X.join(y)

        for id in y['ID'].unique():
            split, valset = Xy[Xy['ID'] != id], Xy[Xy['ID'] == id]
            yield (
                split.loc[:, X.columns],
                split.loc[:, y.columns],
                valset.loc[:, X.columns],
                valset.loc[:, y.columns]
            )
