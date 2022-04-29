from setuptools import find_packages, setup
from dotenv import load_dotenv

setup(
    name='datacakes',
    packages=find_packages(),
    version='0.1.0',
    description='the data cake code repo for presentation',
    author='Sam Fowler',
    license='MIT',
    install_requires=[
            'sphinx'
        ],
    
    tests_require=[
        'pytest',
        'pytest-runner',
        'pytest-cov',
        'coverage'
    ],
    classifiers = [
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development",
    ]
    
)

load_dotenv()