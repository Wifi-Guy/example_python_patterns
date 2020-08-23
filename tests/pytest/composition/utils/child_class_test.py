from src.composition.utils import ChildClass
import pytest


class FakeParentClass:
    @staticmethod
    def test_1():
        return 'test 1'

    @staticmethod
    def test_2():
        return 'test 2'


def test_child_class_can_read_test_1_when_test_1_given():
    assert ChildClass(FakeParentClass, ['test_1']).test_1() == 'test 1'


def test_child_class_cannot_read_test_2_when_test_1_given():
    with pytest.raises(TypeError):
        ChildClass(FakeParentClass, ['test_1']).test_2()
