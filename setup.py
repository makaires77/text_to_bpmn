from setuptools import setup, find_packages

setup(
    name='text_to_bpmn',
    version='0.1',
    packages=find_packages(),
    description='A module to convert structured text to BPMN diagrams',
    long_description=open('README.md').read(),
    install_requires=[
        'bpmn_python',
        'lxml',
        'nltk'
    ]
)
