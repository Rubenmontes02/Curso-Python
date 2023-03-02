from setuptools import setup, find_packages

setup(
    name='Mensajes-RubenMts',
    version='4.0',
    description='Un paquete para saludar y despedir',
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author='Ruben Montes Gonzalez',
    author_email='montesgonzalez@gmail.com',
    url='https://github.com/Rubenmontes02',
    license_files=['LICENSE'],
    packages=find_packages(),
    scripts=[],
    test_suite='tests',
    install_requires=[paquete.strip() for paquete in open("requirements.txt").readlines()],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.9']

)

