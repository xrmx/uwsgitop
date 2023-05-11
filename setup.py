from setuptools import setup
import os

VERSION = '0.11'

setup(
    maintainer='Riccardo Magliocchetti',
    maintainer_email='riccardo.magliocchetti@gmail.com',
    name='uwsgitop',
    version=VERSION,
    description='uWSGI top-like interface',
    url='https://github.com/xrmx/uwsgitop',
    license='MIT',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    scripts=['uwsgitop'],
    install_requires=[
        'argparse;python_version<"3"',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
    project_urls={
        "Source": "https://github.com/xrmx/uwsgitop",
        "Tracker": "https://github.com/xrmx/uwsgitop/issues",
    }
)
