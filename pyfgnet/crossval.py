from functools import singledispatchmethod
from typing import Generator, Tuple, Union
import numpy as np
import pandas as pd


class LOPOCV:
    """Leave-One-Person-Out Cross Validation for scikit-learn.
    """

    def __init__(
        self, n_splits: int = None, shuffle=False, random_state=None
    ) -> None:
        self.n_splits = n_splits
        self.shuffle = shuffle
        self.random_state = random_state

    @singledispatchmethod
    def split(self, X, y=None, groups=None):
        raise TypeError('Parameters must be one of pandas.DataFrame or numpy.ndarray')

    @split.register
    def _(self, X: np.ndarray, y: np.ndarray = None, groups=None):
        ...

    @split.register
    def _(
        self, X: pd.DataFrame, y: Union[pd.DataFrame, pd.Series] = None, groups=None
    ) -> Generator[Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame], None, None]:
        if X and y:
            Xy = X.join(y)
        elif not X:
            Xy = y
        elif not y and 'ID' in X.columns:
            Xy = X
        else:
            raise Exception('Must give one of X or y')

        uid = Xy['ID'].unique()
        if self.shuffle:
            np.random.shuffle(uid)

        for id in Xy['ID'].unique():
            split, valset = Xy[Xy['ID'] != id], Xy[Xy['ID'] == id]
            yield split.index, valset.index
            # yield (
            #     split.loc[:, X.columns],
            #     valset.loc[:, X.columns],
            #     split.loc[:, y.columns],
            #     valset.loc[:, y.columns]
            # )

    def get_n_splits(
        self, X: pd.DataFrame, y: pd.DataFrame, groups=None
    ) -> int:
        return self.n_splits
