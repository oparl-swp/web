#!/usr/bin/env python
from setuptools import setup
setup(
    name='oparlgui',
    version='0.0.1',
    author='OParl Consortium',
    include_package_data=True,
    extras_require=dict(
        test=[],
    ),
    install_requires=[
        'oparlvalidator',
        'flask==0.10.1',
        'requests==2.2.1',
    ],
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'flask = oparlgui.app:run',
        ]
    }
)
