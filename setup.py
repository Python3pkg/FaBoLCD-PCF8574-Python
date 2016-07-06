from setuptools import setup, find_packages

classifiers = ['Development Status :: 4 - Beta',
               'Operating System :: POSIX :: Linux',
               'License :: MIT License',
               'Intended Audience :: Developers',
               'Programming Language :: Python :: 2.7',
               'Topic :: Software Development',
               'Topic :: System :: Hardware']

setup(
    name         = 'FaBoLCD_PCF8574',
    version      = '1.0.0',
    author       = 'FaBo',
    author_email = 'info@fabo.io',
    description  = "This is a library for the FaBo LCD I2C Brick.",
    url          = 'https://github.com/FaBoPlatform/FaBoLCD-PCF8574-Python',
    license      = 'MIT',
    classifiers  = classifiers,
    packages     = find_packages()
)