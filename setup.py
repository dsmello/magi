import os
from setuptools import setup,find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='magi',
      version='0.1.0',
      description='Simple CLI to consume a YAML||JSON and made REST calls. Like a Deploy of K8s but for a REST.S',
      long_description=read('README.md'),
      long_description_content_type='text/markdown',
      url='local',
      author='Davi Mello',
      author_email='dsmello.9@gmail.com',
      license='GPL',
      packages=find_packages(),
      zip_safe=False,
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ])