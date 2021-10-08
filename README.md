# nft-toolkit
[![Build Status](https://circleci.com/gh/nanolaboratory/nft-toolkit/tree/main.svg?style=svg&circle-token=0aeb36b89a70ba3a1791586fce15947b7e3c7179)](https://circleci.com/gh/nanolaboratory/nft-toolkit/tree/main)
[![PyPI version](https://badge.fury.io/py/nft-toolkit.svg)](https://badge.fury.io/py/nft-toolkit)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/dwyl/esta/issues)

A tool to generate a randomized 2D-image NFT collection based on nft attribute layers

## About

`nft-toolkit` is a general purpose nft library to make generating thousands of nft's really easy

##### Made by <a href="https://nanolabs.dev">Nano Labs<a> in 2021

## Installation

### PIP

```bash
pip install nft-toolkit
```

## Examples

### Generate 100 Images:

```python
from nft.image import RandomImageGenerator
nft_collection = RandomImageGenerator(100, "./my-nft-project/nft_images", "./my-nft-project/collection")

nft_collection.generate_collection()
```
