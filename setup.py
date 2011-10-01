from distutils.core import setup

setup(name='uwsgitop',
        version='0.3',
        description='uWSGI top-like interface',
        scripts=['uwsgitop'],
        install_requires = ['simplejson']
        )
