from setuptools import setup, find_packages

setup(
    name='neoconio',
    version='0.1',
    description='Paquete de Python para neoconio',
    author='Tu nombre',
    packages=find_packages(include=["neoconio", "neoconio.*"]),
    python_requires='>=3.8',
    install_requires=[
        # Agrega las dependencias necesarias aquí
    ],
)
