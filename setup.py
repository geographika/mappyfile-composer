import re
from setuptools import setup
from io import open

__version__, = re.findall('__version__ = "(.*)"',
                          open('mappyfile_composer/__init__.py').read())


def readme():
    with open('README.rst', "r", encoding="utf-8") as f:
        return f.read()


setup(name='mappyfile-composer',
      version=__version__,
      description='A mappyfile plugin to help working with large Mapfiles',
      long_description=readme(),
      classifiers=[
          # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Intended Audience :: Developers',
          'Topic :: Software Development :: Build Tools'
      ],
      url='http://github.com/geographika/mappyfile-composer',
      author='Seth Girvin',
      author_email='sethg@geographika.co.uk',
      license='MIT',
      py_modules=['mappyfile_composer'],
      install_requires=['mappyfile'],
      entry_points={'mappyfile.plugins': 'mappyfile_composer = mappyfile_composer'},
      zip_safe=False)
