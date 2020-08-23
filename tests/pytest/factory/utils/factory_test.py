from src.factory.factory import factory
import pytest
from src.factory.factory.instantiations import BackwardFactory, ForwardFactory


def test_calling_controller_with_forward_returns_forward_factory():
    assert type(factory('forward')) == ForwardFactory


def test_calling_controller_with_backward_returns_backward_factory():
    assert type(factory('backward')) == BackwardFactory


def test_calling_controller_without_argument_return_forward_factory():
    assert type(factory()) == ForwardFactory


def test_calling_controller_with_test_causes_error():
    with pytest.raises(KeyError):
        factory('test')
