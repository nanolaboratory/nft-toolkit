from random import randrange
from PIL import Image
from collections import OrderedDict

import os


class RandomImageGenerator(object):
    """
    A class to generate a images based on modules specified by the user

    ...
    Attributes
    _________
    permutations : int
        number of permutations to generate
    modules_path : str
        file directory of where the parts are located
    modules_list : str[]
        list of sorted part directories

    Methods
    _______
    build_images_paths()
        goes through all the images and stores the infomrmation in memory
    image_name(image)
        returns the image name in a string
    layer_attributes(images_paths)
        layers the parts to create the image
    generate_collection()
        generates the images

    """

    def __init__(self, permutations, modules_path, collection_output_path):
        """
        Parameters
        __________
        permutations : int
            Number of permutations to generate
        modules_path : str
            Path of the directory that contain the input modules
        collection_output_path : str
            Path of where to store the output images
        """
        self.permutations = permutations
        self.collection_output_path = collection_output_path

        self.modules_path = modules_path
        self.modules_list = sorted(os.listdir(self.modules_path))
        self.modules_list = [
            module_title
            for module_title in self.modules_list
            if not module_title.startswith(".")
        ]

        if len(self.modules_list) == 0:
            raise AssertionError("No modules")

        # Find first image to determine dimensions
        first_attribute_path = self.find_first_attribute()
        self.height, self.width = self.image_dimensions(first_attribute_path)

    def find_first_attribute(self):
        """Finds the first attribute (image) in the directory containing the modules

        Raises
        __________
        Exception
            If no attributes/images are found

        """
        for module in self.modules_list:
            attribute_list = os.listdir("{}/{}".format(self.modules_path, module))

            for attribute in attribute_list:
                if not attribute.startswith("."):
                    attribute_path = "{}/{}/{}".format(
                        self.modules_path, self.modules_list[0], attribute
                    )
                    return attribute_path

        raise Exception("No attributes found.")

    def image_dimensions(self, image_path):
        """Returns the image dimensions

        Parameters
        __________
        image_path : str
            File location of the image

        Returns
        _______
        tuple
            (int,int) tuple of (height, width)
        """
        with Image.open(image_path) as im:
            return (im.height, im.width)

    def build_image_dict(self):
        """Builds a dictionary of image paths and organizes the dictionary by collection

        Each entry in the dictionary is categorized by the module. Each module is a list of attribute (image) paths

        Returns
        _______
        OrderedDict
            Dictionary of image paths
        """
        images_paths = OrderedDict()
        for module in self.modules_list:
            images_paths.setdefault(module, [])

            module_path = "{}/{}".format(self.modules_path, module)
            module_list = sorted(os.listdir(module_path))
            module_list = [
                module_title
                for module_title in module_list
                if not module_title.startswith(".")
            ]

            for attribute in module_list:
                attribute_image_path = "{}/{}".format(module_path, attribute)
                images_paths[module].append(attribute_image_path)

        return images_paths

    def image_name(self, image):
        """Finds the filename of the image that is opened

        Parameters
        __________
        PIL.Image
            Handle on the image that is opened

        Returns
        _______
        str
            Image filename as a string
        """

        return image.filename.split("/")[-1].split(".", 1)[0]

    def layer_attributes(self, images_paths):
        """Goes through the number of permutations specified and creates images by layering the modules on top of each other

        Each attribute is picked at random to use

        Parameters
        __________
        OrderedDict
            Dictionary of all the image paths

        Raises
        ______
        AssertionError
            If the height and/or width are not equal to the other images
        """
        for _ in range(self.permutations):
            canvas = (self.width, self.height)
            nft_image = Image.new("RGBA", canvas, (0, 0, 0, 0))

            attribute_name = ""
            for _, attributes in images_paths.items():
                attribute_rng = randrange(len(attributes))
                with Image.open(attributes[attribute_rng]) as attribute_image:
                    attribute_name += "{}_".format(self.image_name(attribute_image))

                    attribute_image_h = attribute_image.height
                    attribute_image_w = attribute_image.width

                    if (
                        attribute_image_h != self.height
                        and attribute_image_w != self.width
                    ):
                        raise AssertionError(
                            "Height and/or width does not match \
                            {0} != {1} and/or {2} != {3}.".format(
                                attribute_image_h,
                                self.height,
                                attribute_image_w,
                                self.width,
                            )
                        )

                    converted_image = attribute_image.convert("RGBA")
                    nft_image.paste(converted_image, (0, 0), mask=converted_image)
            nft_image_path = "{}/{}.png".format(
                self.collection_output_path, attribute_name[:-1]
            )
            nft_image.save(nft_image_path)

    def generate_collection(self):
        """Generates the collection of images

        First builds the dictionary of image paths and then layers the attributes to create the images for the number of permutations specified in the init
        """
        images_paths = self.build_image_dict()

        if not os.path.exists(self.collection_output_path):
            os.makedirs(self.collection_output_path)

        self.layer_attributes(images_paths)
