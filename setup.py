from setuptools import setup, find_packages

setup(
    name="wadlstreet",
    version="0.1.0",
    description="A mock trading engine with an order book and market participants.",
    author="Wadi Moughanim",
    packages=find_packages(),
    install_requires=[
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "wadstreet-simulator=wadstreet.simulator:main",
        ],
    },
)
