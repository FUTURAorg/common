from setuptools import setup, find_packages

setup(
  name='futuracommon',
  version='0.0.1',
  author='Geogii Danilov',
  author_email='tiazkezo@gmail.com',
  description='Common components for FUTURA project',
  url='https://github.com/FUTURAorg',
  packages=find_packages(),
  install_requires=['grpcio', 'grpcio-tools', 'redis'],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  project_urls={
    'GitHub': 'https://github.com/FUTURAorg'
  },
  python_requires='>=3.6'
)