from src.composition.utils import ParentClass, ChildClass


if __name__ == '__main__':
    child_class = ChildClass(ParentClass, persist_methods=['class_name', 'attribute_calling_hidden_attribute'])
    # We can pass default methods to be shown
    print(child_class.class_name())
    print(child_class.attribute_calling_hidden_attribute())
    try:
        print(child_class._hidden_attribute())
    except BaseException as exc:
        print(f'Exception: {type(exc)}: {exc}')

    try:
        print(child_class.example_method_2())
    except BaseException as exc:
        print(f'Exception: {type(exc)}: {exc}')

    child_class_2 = ChildClass(ParentClass,
                               persist_methods=['class_name', 'attribute_calling_hidden_attribute', 'example_method'])
    print(child_class_2.class_name())
    print(child_class_2.attribute_calling_hidden_attribute())
    print(child_class_2.example_method())
    try:
        print(child_class_2._hidden_attribute())
    except BaseException as exc:
        print(f'Exception: {type(exc)}: {exc}')
