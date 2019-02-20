'''
@author: sean
'''

from setuptools import setup, find_packages

setup(
    name='test_p',
    version="0.3.1",
    author='Mayuri',
    author_email='nikammayuri505@gmail.com',
    url='http://github.com/binstar/binstar_pypi',
    packages=find_packages(),
    description='Python Distribution Utilities',
    long_description='longer description of the package',
    install_requires=['requests>=2.0,<=3.0',
                      'pyyaml',
                      'python-dateutil',
                      'pytz'],

)


