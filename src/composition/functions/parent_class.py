class ParentClass:

    @staticmethod
    def class_name():
        return 'Parent Class'

    @staticmethod
    def _hidden_attribute():
        return 'hidden attribute'

    @classmethod
    def attribute_calling_hidden_attribute(cls):
        return cls._hidden_attribute()
