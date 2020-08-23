from composition.functions import ParentClass, ChildClass


if __name__ == '__main__':
    child_class = ChildClass(ParentClass)
    print(child_class.class_name())
    print(child_class.attribute_calling_hidden_attribute())
    try:
        print(child_class._hidden_attribute())
    except BaseException as exc:
        print(f'Exception: {type(exc)}: {exc}')
