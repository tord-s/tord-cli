from setuptools import setup
setup(
    name = 'tord',
    version = '0.1.0',
    packages = ['tord'],
    entry_points = {
        'console_scripts': [
            'tord = tord.__main__:main'
        ]
    })