from setuptools import find_packages, setup

setup(
    name="gnarly",
    packages=find_packages(),
    version="0.0.1",
    test_suite="tests",
    extras_require={
        "dev": [
            "pytest-spark==0.6.0",
            "pytest-cov==2.8.1",
            "pytest==5.4.2",
            "pdbpp==0.10.2",
        ]
    },
    install_requires=[
        "pyspark>=2.4.5",
    ],
)
