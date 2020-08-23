from src.singleton.utils import Singleton
import pytest


class ResetAddedSingleton(Singleton):
    @staticmethod
    def reset():
        _instance = None


def test_singleton_initialisation_once_passes():
    ResetAddedSingleton.reset()
    assert ResetAddedSingleton()


def test_singleton_initialisation_twice_fails():
    ResetAddedSingleton.reset()
    ResetAddedSingleton()
    with pytest.raises(Exception):
        ResetAddedSingleton()


def test_singleton_id_changes_between_instances():
    ResetAddedSingleton.reset()
    s1 = ResetAddedSingleton.get_instance()
    s2 = ResetAddedSingleton.get_instance()
    s1.id = 'test'
    assert s2.id == 'test'


def test_singleton_id_does_not_start_as_test():
    ResetAddedSingleton.reset()
    s1 = ResetAddedSingleton.get_instance()
    assert s1.id != 'test'
