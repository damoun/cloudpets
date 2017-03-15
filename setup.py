from setuptools import setup, find_packages

setup(
    name='cloudpets',
    version='0.0.1',
    description='Module to control you cloudpets',
    url='https://github.com/damoun/cloudpets',

    author='Damien Plenard',
    author_email='damien@plenard.me',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: System :: Hardware :: Hardware Drivers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='toy bluetooth',
    packages=find_packages(exclude=['exemples', 'tests']),
    install_requires=['pybluez[ble]']
)
