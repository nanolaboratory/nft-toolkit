# nft-toolkit

[![Build Status](https://circleci.com/gh/nanolaboratory/nft-toolkit/tree/main.svg?style=svg&circle-token=0aeb36b89a70ba3a1791586fce15947b7e3c7179)](https://circleci.com/gh/nanolaboratory/nft-toolkit/tree/main)
[![PyPI version](https://badge.fury.io/py/nft-toolkit.svg)](https://badge.fury.io/py/nft-toolkit)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/nanolaboratory/nft-toolkit/issues)

A tool to generate a randomized 2D-image NFT collection based on nft attribute layers

## About

`nft-toolkit` is a general purpose nft library to make generating thousands of nft's really easy

##### Made by <a href="https://nanolabs.dev">Nano Labs<a> in 2021

## Installation

### PIP

```bash
pip install nft-toolkit
```

## Documentation
To view documentation, after pip installation run the following commands in a python3 interactive shell.

```python
from nft.image import RandomImageGenerator
help(RandomImageGenerator)
```

## Examples

### Generate 100 Images:

#### Steps
1. Create a directory of attributes that you would like to layer on top of each other. Each attribute must be of the same image size so that the overlays will line up properly.

2. Create a script similar to below. RandomImageGenerator uses 3 parameters: Number of permutations to generate, filepath to attributes, and filepath to place the images generated.

```python
from nft.image import RandomImageGenerator
nft_collection = RandomImageGenerator(100, "./my-nft-project/nft_images", "./my-nft-project/collection")

nft_collection.generate_collection()
```

3. Your collection should be generated with each image's filename describing the attributes that are used.

## Contribute
Issues and pull requests are welcome. If you add functionality, then please add unit tests to cover it. Continuous Integration is handled by CircleCI.