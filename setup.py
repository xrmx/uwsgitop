from distutils.core import setup

setup(name='uwsgitop',
        version='0.8',
        description='uWSGI top-like interface',
        license='MIT',
        scripts=['uwsgitop'],
        install_requires = ['simplejson']
        )
