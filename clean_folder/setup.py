from setuptools import setup, find_namespace_packages

setup(name='clean_folder',
    version='0.0.1',
    description='Sorting files be category',
    url='https://github.com/MaxKryvytskyi/clean_folder',
    author='Max Kryvytskyi',
    author_email='max.krivitskyh@gmail.com',
    license='MIT',
    classifiers=["Programming Language :: Python :: 3.11",
    "Development Status :: 5 - Production/Stable",
    "Operating System :: OS Independent",
    "Natural Language :: Ukrainian"],
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean_folder = clean_folder.clean:main']}
    )