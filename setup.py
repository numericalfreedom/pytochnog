import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pytochnog",
    version="0.0.1",
    author="Numerical Freedom Foundation",
    author_email="numericalfreedom@googlemail.com",
    description="A python tool to the Tochnog Professional geotechnical FEM analysis programme",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/numericalfreedom/pytochnog",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

