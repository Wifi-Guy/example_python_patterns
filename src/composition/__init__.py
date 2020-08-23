from composition.functions import ParentClass, ChildClass


if __name__ == '__main__':
    child_class = ChildClass(ParentClass)
    # 1. We can create a class with the default methods and hide additional from it
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

    child_class_2 = ChildClass(ParentClass, persist_methods=['example_method'])
    # 2. or we can add additional methods that can be accessed
    print(child_class_2.class_name())
    print(child_class_2.attribute_calling_hidden_attribute())
    print(child_class_2.example_method())
    try:
        print(child_class_2._hidden_attribute())  # 3. either way we can create a 'private' class object
    except BaseException as exc:
        print(f'Exception: {type(exc)}: {exc}')
