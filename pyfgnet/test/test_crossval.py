import unittest as ut
from ..crossval import LOPOCV


class TestLOPOCV(ut.TestCase):

    def setUp(self) -> None:
        self.lopocv = LOPOCV()

    def test_split(self):
        ...

    def test_get_n_splits(self):
        ...


if __name__ == '__main__':
    ut.main()
