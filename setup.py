import os
from setuptools import find_packages, setup
import setuptools

with open(os.path.join(os.path.dirname(__file__), "README.md")) as readme:
    README = readme.read()

setuptools.setup(
    name="HaloCheck",
    version="0.0.1",
    author="Mohamed Elaraby",
    author_email="mse30@pitt.edu",
    description="An easy to use BlackBox package to estimate hallucination severity in LLMs",
    long_description="An easy to use entailment based BlackBox package to estimate hallucination severity in LLMs",
    long_description_content_type="text/markdown",
    url="https://github.com/EngSalem/HaLo",
    license='MIT',
    python_requires='>=3.8',
    install_requires=['summac']
)