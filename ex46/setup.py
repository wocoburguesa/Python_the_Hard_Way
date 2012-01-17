try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
    
config = {
    'description': 'ex46',
    'name': 'Marco Flores',
    'url': 'www.www.com',
    'download_url': 'url.url.com',
    'author_email': 'wocoburguesa@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex46'],
    'scripts': [],
    'name': 'oz'
    }
    
setup(**config)
