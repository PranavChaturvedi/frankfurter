import pathlib
import setuptools

setuptools.setup(
    name="frankfurter",
    version="1.0.0",
    description="A lightweight wrapper for the frankfurter API",
    long_description=pathlib.Path("README.md").read_text(encoding='utf-8'),
    long_description_content_type="text/markdown",
    url="https://www.frankfurter.app",
    author="Pranav Chaturvedi",
    author_email="pranavhfs1@gmail.com",
    maintainer="PranavChaturvedi",
    license="MIT",
    project_urls={
        "Homepage":"https://www.frankfurter.app",
        "Documentation":"https://github.com/PranavChaturvedi/frankfurter/blob/main/README.md",
        "Repository":"https://github.com/PranavChaturvedi/frankfurter",
    },
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
    python_requires=">=3.6",
    packages=setuptools.find_packages(),
    include_package_data=True
)