from random import randrange
from PIL import Image, ImageDraw
from collections import OrderedDict

import simplejson
import json
import os


class RandomImageGenerator(object):
    def __init__(
        self,
        permutations,
        width,
        height,
        collection_input_path,
        collection_output_path
    ):
        self.permutations = permutations
        self.width = width
        self.height = height
        self.parts_path = collection_input_path

        self.parts_list = sorted(os.listdir(self.parts_path))
        self.parts_list = [part_title for part_title in self.parts_list if not part_title.startswith(".")]
        self.collection_output_path = collection_output_path

    def build_image_store(self):
        image_store = OrderedDict()
        for category in self.parts_list:
            image_store.setdefault(category, [])

            category_path = "{}/{}".format(self.parts_path, category)
            category_list = sorted(os.listdir(category_path))
            category_list = [category_title for category_title in category_list if not category_title.startswith(".")]

            for attribute in category_list:
                attribute_image_path = "{}/{}".format(category_path, attribute)
                attribute_image = Image.open(attribute_image_path)
                image_store[category].append(attribute_image)

        return image_store

    def image_name(self, image):
        return image.filename.split("/")[-1].split(".", 1)[0]

    def layer_attributes(self, image_store):
        for i in range(self.permutations + 1):
            canvas = (self.width, self.height)
            nft_image = Image.new('RGBA', canvas, (0, 0, 0, 0))

            for category, attributes in image_store.items():
                attribute_rng = randrange(len(attributes))
                attribute_image = attributes[attribute_rng]
                attribute_name = self.image_name(attribute_image)

                nft_image.paste(
                    attribute_image,
                    (0, 0),
                    mask=attribute_image
                )
            nft_image_path = "{}/{}.png".format(self.collection_output_path, i)
            nft_image.save(nft_image_path)

    def generate_collection(self):
        image_store = self.build_image_store()

        if not os.path.exists(self.collection_output_path):
            os.makedirs(self.collection_output_path)

        self.layer_attributes(image_store)

