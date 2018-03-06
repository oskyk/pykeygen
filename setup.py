from distutils.core import setup
from setuptools import find_packages

setup(name='pykeygen',
      version='0.0.1',
      packages=find_packages(),
      install_requires=['bip32utils', 'chainside-btcpy'],
      dependency_links=['git+https://github.com/oskyk/btcpy.git@altcoin-constants-filled'],
      description='Tool to generate keys and addresses',
      author='Oskar Hladky',
      author_email='oskyks1@gmail.com',
      url='https://github.com/oskyk/pykeygen',
      python_requires='>=3',
      download_url='https://github.com/oskyk/pykeygen/archive/0.0.1.tar.gz',
      scripts=['pykeygen'],
      keywords=['keygen', 'mnemonic', 'segwit', 'dash', 'litecoin', 'bitcoin']
)