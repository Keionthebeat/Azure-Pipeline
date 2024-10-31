from setuptools import setup, find_packages

setup(
    name='iot_device_management',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'Flask==2.0.1',
        # Add other dependencies here
    ],
)