

class ChildClass:
    _persist_methods = ['class_name', 'attribute_calling_hidden_attribute']

    def __init__(self, persister):
        self._persister = persister

    def __getattr__(self, attr):
        if attr in self._persist_methods:
            return getattr(self._persister, attr)
