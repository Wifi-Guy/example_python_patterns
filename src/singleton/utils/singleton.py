class Singleton:
    _instance = None

    @staticmethod
    def get_instance():
        return Singleton._instance or Singleton()

    def __init__(self):
        self.id = '---'
        if Singleton._instance is not None:
            raise BaseException('Singleton Already Created')
        else:
            Singleton._instance = self
