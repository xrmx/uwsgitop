from distutils.core import setup

setup(name='uwsgitop',
        version='0.6.2',
        description='uWSGI top-like interface',
        scripts=['uwsgitop'],
        install_requires = ['simplejson']
        )
