import setuptools


setuptools.setup(
    name="nft-toolkit",
    version="0.1.1",
    author="Nano Labs LLC",
    author_email="hello@nanolabs.dev",
    description="A tool to generate a randomized 2D-image \
        NFT collection based on nft attribute layers",
    url="https://github.com/nanolaboratory/nft-toolkit",
    project_urls={
        "Bug Tracker": "https://github.com/nanolaboratory/nft-toolkit/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=["nft"],
    python_requires=">=3.6",
    install_requires=["Pillow==8.3.2", "simplejson"],
)
