"""Setup configuration for the Advanced Calculator package."""

from setuptools import setup, find_packages


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name="advanced-calculator",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A comprehensive mathematical calculator with support for various functions and operations.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/calculator",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Mathematics",
    ],
    python_requires=">=3.8",
    install_requires=[],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "pytest-cov>=3.0",
            "black>=22.0",
            "flake8>=4.0",
            "mypy>=0.950",
            "sphinx>=4.0",
        ],
    },
)
