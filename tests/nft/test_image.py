from nft.image import RandomImageGenerator
from PIL import Image
from collections import OrderedDict
from shutil import rmtree

import os
import pytest


def get_image_data(image_path):
    with Image.open(image_path) as im:
        return list(im.getdata())


@pytest.fixture()
def random_image_generator():
    yield RandomImageGenerator(1, "./tests/nft/test_modules/", "./tests/nft/output")

    if os.path.isdir("./tests/nft/output/"):
        rmtree("./tests/nft/output")


def test_image_dimensions():
    height, width = RandomImageGenerator.image_dimensions(
        None, "./tests/nft/test_modules/1-bottom/maroon-orange-blue.png"
    )
    assert height == 20
    assert width == 15


def test_init_and_find_attributes(random_image_generator):
    # No exception raised means an attribute is found.
    assert random_image_generator is not None


def test_file_is_generated(random_image_generator):
    random_image_generator.generate_collection()
    assert os.path.isdir("./tests/nft/output/")
    assert os.path.exists("./tests/nft/output/maroon-orange-blue_neon-brown-teal.png")


def test_build_image_dict(random_image_generator):
    image_paths = random_image_generator.build_image_dict()
    assert image_paths == OrderedDict(
        [
            ("1-bottom", ["./tests/nft/test_modules//1-bottom/maroon-orange-blue.png"]),
            ("2-top", ["./tests/nft/test_modules//2-top/neon-brown-teal.png"]),
        ]
    )


def test_input_image_bottom():
    upper_left = [(64, 0, 0, 255)] * 3
    upper_right = [(0, 0, 0, 0)] * 3
    lower_left = [(238, 99, 48, 255)] * 3
    lower_right = [(0, 88, 255, 255)] * 3
    bottom_offset = 15 * 17

    pixdata = get_image_data("./tests/nft/test_modules/1-bottom/maroon-orange-blue.png")

    for row_idx in range(3):
        pix_index = row_idx * 15

        assert pixdata[pix_index : pix_index + 3] == upper_left
        assert pixdata[pix_index + 12 : pix_index + 15] == upper_right
        assert (
            pixdata[pix_index + bottom_offset : pix_index + bottom_offset + 3]
            == lower_left
        )
        assert (
            pixdata[pix_index + bottom_offset + 12 : pix_index + bottom_offset + 15]
            == lower_right
        )


def test_input_image_top():
    upper_left = [(204, 244, 15, 255)] * 3
    upper_right = [(68, 60, 20, 255)] * 3
    lower_left = [(0, 0, 0, 0)] * 3
    lower_right = [(48, 238, 114, 255)] * 3
    bottom_offset = 15 * 17

    pixdata = get_image_data("./tests/nft/test_modules/2-top/neon-brown-teal.png")

    for row_idx in range(3):
        pix_index = row_idx * 15

        assert pixdata[pix_index : pix_index + 3] == upper_left
        assert pixdata[pix_index + 12 : pix_index + 15] == upper_right
        assert (
            pixdata[pix_index + bottom_offset : pix_index + bottom_offset + 3]
            == lower_left
        )
        if row_idx < 2:
            assert (
                pixdata[pix_index + bottom_offset + 12 : pix_index + bottom_offset + 15]
                == lower_right
            )


def test_overlay(random_image_generator):
    random_image_generator.generate_collection()

    upper_left = [(204, 244, 15, 255)] * 3
    upper_right = [(68, 60, 20, 255)] * 3
    lower_left = [(238, 99, 48, 255)] * 3
    top_lower_right = [(48, 238, 114, 255)] * 3
    bottom_lower_right = [(0, 88, 255, 255)] * 3
    bottom_offset = 15 * 17

    pixdata = get_image_data(
        "./tests/nft/output/maroon-orange-blue_neon-brown-teal.png"
    )

    for row_idx in range(3):
        pix_index = row_idx * 15

        assert pixdata[pix_index : pix_index + 3] == upper_left
        assert pixdata[pix_index + 12 : pix_index + 15] == upper_right
        assert (
            pixdata[pix_index + bottom_offset : pix_index + bottom_offset + 3]
            == lower_left
        )

        if row_idx != 2:
            assert (
                pixdata[pix_index + bottom_offset + 12 : pix_index + bottom_offset + 15]
                == top_lower_right
            )
        else:
            assert (
                pixdata[pix_index + bottom_offset + 12 : pix_index + bottom_offset + 15]
                == bottom_lower_right
            )
