from src.factory.factory import factory


if __name__ == '__main__':
    forward_factory = factory('forward')  # In actual code wed use hidden logic for this to switch objects
    backward_factory = factory('backward')

    print(forward_factory.func_1())
    print(forward_factory.func_2())
    print(backward_factory.func_1())
    print(backward_factory.func_2())

    try:
        factory('sideways')
    except BaseException as exc:
        print(f'{type(exc)}: {exc}')
