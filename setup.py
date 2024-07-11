from setuptools import find_packages, setup

setup(
    name='src',
    packages=find_packages(),
    version='0.1.0',
    description="Conduct sentiment analysis with pre-trained transformer model (BERT tokenizer)",
    author='Lily Ren',
    license='MIT',
    install_requires=['pandas','numpy','mlcroissant','tensorflow_datasets','scikit-learn','argparse','matplotlib','seaborn','transformers[torch]','datasets']
)