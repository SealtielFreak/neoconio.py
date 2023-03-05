from setuptools import setup, find_packages

setup(
    name='neoconio',
    version='0.1',
    packages=find_packages(),
    author='SealtielFreak',
    install_requires=[
        # Agrega aquí las dependencias del paquete
    ],
    extras_require={
        'dev': [

        ]
    },
    package_data={
        'neoconio': [
            'neoconio/*',
            'examples/*'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3.8'
    ]
)
