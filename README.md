# nft-toolkit

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
