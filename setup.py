import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="thumbnail",
    version="1.0",
    author="Anshul Kharb",
    author_email="hey@anshulkharb.com",
    description="Generate thumbnails for any file type.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/anshulkharb/thumbnail",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)