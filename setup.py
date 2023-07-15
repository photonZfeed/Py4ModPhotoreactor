from distutils.core import setup

setup(
    name='Py4ModPhotoreactor',
    version='2.0.0',
    url='',
    license='',
    author='Daniel Kowalczyk, Dirk Ziegenbalg',
    author_email='dirk.ziegenbalg@uni-ulm.de',
    description='Package to control the modular reactor.',
    packages=['Py4ModPhotoreactor'],
    package_data={'Py4ModPhotoreactor': ['conf/*.conf']},
    zip_safe=False,
    install_requires=['tinkerforge',
                      'configparser',
                      'future',
                      'pyserial']
)
