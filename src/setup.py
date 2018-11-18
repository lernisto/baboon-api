from setuptools import setup

setup(
    name='baboon',
    version='0.1',
    py_packages=['baboon'],
    install_requires=[
        'Click',
        'Jinja2',
        'Flask',
        'Redis',
    ],
    entry_points='''
        [console_scripts]
        newsite=baboon.cli:newsite
        newpost=baboon.cli:newpost
        wsgi=baboon.wsgi:run
    ''',
)
