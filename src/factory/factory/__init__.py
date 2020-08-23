from .instantiations import BackwardFactory, ForwardFactory


def factory(factory_type: str = 'forward'):
    if factory_type == 'forward':
        return ForwardFactory()
    elif factory_type == 'backward':
        return BackwardFactory()
    raise KeyError(f'Factory Type {factory_type} does not exist')
