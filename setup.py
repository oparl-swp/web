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
        'setuptools',
        'psycopg2==2.5.2',
        'django-admin-decorators==0.1',
        'Django==1.6.4',
        'django-extensions==1.3.3',
        'gunicorn==18.0',
        'South==0.8.4',
        'django-debug-toolbar==1.2',
        'requests==2.2.1',
        'python-memcached==1.53',
    ],
    zip_safe=False,
    entry_points={
        'console_scripts': []
    }
)
