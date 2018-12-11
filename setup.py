import setuptools
import os

VERSION = '0.11'

py2_extras = ["argparse", "simplejson"]
extras_require = {":python_version<'3'": py2_extras}

setuptools.setup(
    maintainer='Riccardo Magliocchetti',
    maintainer_email='riccardo.magliocchetti@gmail.com',
    name='uwsgitop',
    version=VERSION,
    description='uWSGI top-like interface',
    license='MIT',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    scripts=['uwsgitop'],
    extras_require=extras_require,
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ]
)
