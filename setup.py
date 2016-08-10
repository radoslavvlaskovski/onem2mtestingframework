from setuptools import setup, find_packages


setup(name='onem2mtesting',
      version='1.0',
      description='A Framework designed to test Applications Compliant with the oneM2M standard',
      author='Radoslav Vlaskovski',
      author_email='radoslav.vlaskovsky@gmail.com',
      url='',
      packages=find_packages(),
      install_requires=[
          'xmltodict',
          'paho-mqtt',
          'requests'
      ]
     )

