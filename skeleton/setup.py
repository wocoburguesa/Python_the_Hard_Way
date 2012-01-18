try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'PROYECTO',
    'author': 'Marco Flores',
    'url': 'com.www.org',
    'download_url': 'pe.ru.ch',
    'author_email': 'wocoburguesa@gmail.com',
    'version': 'X.X',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
