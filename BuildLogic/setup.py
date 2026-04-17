from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="buildconnect-logistics-pdc",
    version="1.0.0",
    author="Your Team Name",
    description="Parallel and Distributed Computing case study for BuildConnect Logistics",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "pandas>=1.3.0",
        "numpy>=1.21.0",
        "scikit-learn>=1.0.0",
        "dask[complete]>=2022.1.1",
        "pyspark>=3.2.0",
        "ray[tune]>=1.10.0",
        "matplotlib>=3.4.0",
        "plotly>=5.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.2.0",
            "pytest-cov>=2.12.0",
            "black>=21.9b0",
            "flake8>=3.9.0",
        ],
    },
)
