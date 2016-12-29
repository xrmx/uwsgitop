from setuptools import setup
import os

VERSION = '0.10'

setup(
    maintainer='Riccardo Magliocchetti',
    maintainer_email='riccardo.magliocchetti@gmail.com',
    name='uwsgitop',
    version=VERSION,
    description='uWSGI top-like interface',
    license='MIT',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    scripts=['uwsgitop'],
    install_requires = [
        'simplejson',
        'argparse',
    ]
)
