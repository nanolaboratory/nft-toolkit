from random import randrange
from PIL import Image, ImageDraw
from collections import OrderedDict

import simplejson
import json
import os


class RandomImageGenerator(object):
    """
    A class to generate a images based on parts specified by the user.

    ...
    Attributes
    _________
    permutations : int
        number of permutations to generate
    parts_path : str
        file directory of where the parts are located
    parts_list : str[]
        list of sorted part directories

    Methods
    _______
    build_image_store()
        goes through all the images and stores the infomrmation in memory
    image_name(image)
        returns the image name in a string
    layer_attributes(image_store)
        layers the parts to create the image
    generate_collection()
        generates the images

    """
    def __init__(
        self,
        permutations,
        collection_input_path,
        collection_output_path
    ):
        self.permutations = permutations
        self.collection_output_path = collection_output_path

        self.parts_path = collection_input_path
        self.parts_list = sorted(os.listdir(self.parts_path))
        self.parts_list = [part_title for part_title in self.parts_list if not part_title.startswith(".")]

        # Find random image to determine dimensions
        image_list = os.listdir("{}/{}".format(self.parts_path, self.parts_list[0]))
        image_path = None
        for image in image_list:
            if not image.startswith("."):
                image_path = "{}/{}/{}".format(self.parts_path, self.parts_list[0], image)
                break

        self.width, self.height = self.image_dimensions(image_path)


    def image_dimensions(self, image_path):
        im = Image.open(image_path)
        im.close()
        return im.size

    def build_image_dict(self):
        image_store = OrderedDict()
        for category in self.parts_list:
            image_store.setdefault(category, [])

            category_path = "{}/{}".format(self.parts_path, category)
            category_list = sorted(os.listdir(category_path))
            category_list = [category_title for category_title in category_list if not category_title.startswith(".")]

            for attribute in category_list:
                attribute_image_path = "{}/{}".format(category_path, attribute)
                image_store[category].append(attribute_image_path)

        return image_store

    def image_name(self, image):
        return image.filename.split("/")[-1].split(".", 1)[0]

    def layer_attributes(self, image_store):
        for _ in range(self.permutations + 1):
            canvas = (self.width, self.height)
            nft_image = Image.new("RGBA", canvas, (0, 0, 0, 0))

            attribute_name = ""
            for _, attributes in image_store.items():
                attribute_rng = randrange(len(attributes))
                attribute_image = Image.open(attributes[attribute_rng])
                attribute_name += "{}_".format(self.image_name(attribute_image))

                attribute_image_h, attribute_image_w = attribute_image.size
                if attribute_image_h != self.height and attribute_image_w != self.width:
                    raise AssertionError("Height and/or width does not match \
                        {0} != {1} and/or {2} != {3}.".format(attribute_image_h, \
                            self.height, attribute_image_w, self.width))

                nft_image.paste(
                    attribute_image,
                    (0, 0),
                    mask=attribute_image
                )
            nft_image_path = "{}/{}.png".format(self.collection_output_path, attribute_name[:-1])
            nft_image.save(nft_image_path)

    def generate_collection(self):
        image_store = self.build_image_dict()

        if not os.path.exists(self.collection_output_path):
            os.makedirs(self.collection_output_path)

        self.layer_attributes(image_store)

