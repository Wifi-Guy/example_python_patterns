from typing import List


class ChildClass:
    _persist_methods = ['class_name', 'attribute_calling_hidden_attribute']  # Methods that the subclass can access

    def __init__(self, persister: object, persist_methods: List = None):
        if persist_methods is None:
            persist_methods = []
        self._persister = persister
        self._persist_methods += persist_methods

    def __getattr__(self, attr):
        if attr in self._persist_methods:
            return getattr(self._persister, attr)
