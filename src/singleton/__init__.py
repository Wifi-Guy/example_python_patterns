from src.singleton.utils import Singleton

if __name__ == '__main__':
    s1 = Singleton.get_instance()

    s2 = Singleton.get_instance()

    print(s2.id)
    s1.id = 'test'
    print(s2.id)
