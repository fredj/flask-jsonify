"""
flask-jsonify
-------------

Description goes here...

Links
`````

* `documentation <http://github.com/fredj/flask-jsonify/raw/master/README>`_

"""
from setuptools import setup


setup(
    name='flask-jsonify',
    version='0.1',
    url='http://github.com/fredj/flask-jsonify',
    license='BSD',
    author='Frederic Junod',
    author_email='frederic.junod@gmail.com',
    description='A small Flask decorator for returning json',
    long_description=__doc__,
    packages=['flaskext'],
    namespace_packages=['flaskext'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask',
        'simplejson' # FIXME: only for python < 2.6
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
