class ParentClass:

    @staticmethod
    def class_name():
        return 'Parent Class'

    @staticmethod
    def _hidden_attribute():
        return 'hidden attribute'

    @classmethod
    def attribute_calling_hidden_attribute(cls):
        # We can also have functions calling hidden functions that the rest of the code cannot access,
        # making them private
        return cls._hidden_attribute()

    @staticmethod
    def example_method():
        return 'example'
