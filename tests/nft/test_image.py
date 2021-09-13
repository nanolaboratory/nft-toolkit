from nft.image import RandomImageGenerator
from pathlib import Path

import os
import pytest


def remove_path(path: Path):
    if path.is_file() or path.is_symlink():
        path.unlink()
        return
    for p in path.iterdir():
        remove_path(p)
    path.rmdir()


@pytest.fixture()
def random_image_generator():
    os.mkdir("/tmp/parts/")
    yield RandomImageGenerator
    os.rmdir("/tmp/parts/")
    remove_path(Path("/tmp/example/"))


class TestRandomImageGenerator:
    def test_if_directory_exists(self, random_image_generator):
        collection = random_image_generator(10, 50, 50, '/tmp/parts/', '/tmp/example/')
        collection.generate_collection()
        assert os.path.isdir("/tmp/example/")
