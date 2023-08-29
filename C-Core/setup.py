# This file is part of the ChitAkasha Project

from setuptools import setup, find_packages

setup(
    name='ChitAkasha_CCore',
    version='0.1.0',
    description='Classical Core Modules for the ChitAkasha Project',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/chitakasha/code',
    packages=find_packages(),
    install_requires=[
        'numpy==1.21.2',
        'pandas==1.3.3',
        'scipy==1.7.1',
        'scikit-learn==0.24.2',
        'tensorflow==2.6.0',
        'requests==2.26.0'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
    ],
)
