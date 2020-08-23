from setuptools import setup

setup(
    name='example_python_patterns',
    version='',
    packages=['factory', 'factory.utils', 'iterator', 'singleton', 'composition', 'composition.utils', 'pytest',
              'pytest.factory', 'pytest.factory.utils', 'pytest.iterator', 'pytest.iterator.utils', 'pytest.singleton',
              'pytest.singleton.utils', 'pytest.composition', 'pytest.composition.utils', 'hypothesis',
              'hypothesis.factory', 'hypothesis.factory.utils', 'hypothesis.iterator', 'hypothesis.iterator.utils',
              'hypothesis.singleton', 'hypothesis.singleton.utils', 'hypothesis.composition',
              'hypothesis.composition.utils'],
    package_dir={'': 'src'},
    url='',
    license='',
    author='Matt',
    author_email='',
    description=''
)
