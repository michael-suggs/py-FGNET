from dataclasses import dataclass
from typing import Dict, List, Tuple, Union
import numpy as np
import pandas as pd
from sklearn.base import ClassifierMixin, RegressorMixin, TransformerMixin
from sklearn.model_selection import train_test_split

DataFrame = pd.DataFrame
ArrayLike = Union[pd.DataFrame, np.ndarray]


class DataTierHandler:

    def __init__(
        self, X: DataFrame, y: DataFrame, tier_splits: List[str]
    ) -> None:
        self.X, self.y = tier_splits(X, y, tier_splits)

    def split_tiers(
        self, X: pd.DataFrame, y: pd.DataFrame, tier_splits: List[str]
    ) -> Tuple[pd.DataFrame, pd.DataFrame]:
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2)
        self.splits = {
            '0':
                {
                    'X_train': X_train,
                    'X_test': X_test,
                    'y_train': y_train,
                    'y_test': y_test
                }
        }

        for split in splits:
            Xs0, Xs1 = X[X[split] < .5]
            X_train, X_test, y_train, y_test = train_test_split()


@dataclass
class ModelParams:
    model: Union[ClassifierMixin, RegressorMixin]
    params: dict
    preprocessing: TransformerMixin = None


class HierarchicalConfig:

    def __init__(self, age_clf: ModelParams, age_reg0: ModelParams, age_reg1: ModelParams, gender_clf: ModelParams) -> None:
        self.age_clf = age_clf
        self.age_reg0 = age_reg0
        self.age_reg1 = age_reg1
        self.gender_clf = gender_clf


class HierarchicalFGNET:

    def __init__(
        self,
        age_clf: List[ModelParams],
        age_reg0: List[ModelParams],
        age_reg1: List[ModelParams],
        gender_clf: List[ModelParams],
        X: DataFrame,
        y: DataFrame,
        col_age: str = "age",
        col_age_class: str = "age_class",
        col_gender: str = "Gender_0M_1F",
        test_size: float = .2,
    ) -> None:
        self.age_clf = age_clf
        self.age_reg0 = age_reg0
        self.age_reg1 = age_reg1
        self.gender_clf = gender_clf

        self.X = X
        self.y = y
        self.y_age = y[col_age]
        self.y_age_class = y[col_age_class]
        self.y_gender = y[col_gender]


    def fit(
        self,
        X,
        y,
        col_age: str = "age",
        col_age_class: str = "age_class",
        col_gender: str = "Gender_0M_1F"
    ) -> None:
        pass

    def predict(
        self,
        X,
        y,
        col_age: str = "age",
        col_age_class: str = "age_class",
        col_gender: str = "Gender_0M_1F"
    ) -> None:
        pass
