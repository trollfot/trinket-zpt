from os import path
from setuptools import setup, find_packages


def read(filename):
    with open(path.join(path.dirname(__file__), filename)) as f:
        return f.read()


install_requires = [
    "curio >= 0.9",
    "Chameleon >= 3.2"
    ]

tests_require = [
    "trinket >= 0.1.2",
    "pytest",
    ]

setup(name='trinket_zpt',
      version='0.1',
      description="Trinket webserver Zope Page Template templating utility",
      long_description="%s\n\n%s" % (
          read('README.rst'), read(path.join('docs', 'HISTORY.rst'))),
      keywords="Curio Trinket",
      author="",
      author_email="",
      license="BSD",
      packages=find_packages('src', exclude=['ez_setup']),
      package_dir={'': 'src'},
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      extras_require={'test': tests_require},
      )
