from __future__ import absolute_import, division, unicode_literals

from PIL import Image
from django.utils.six import BytesIO
from versatileimagefield.datastructures import SizedImage
from versatileimagefield.registry import versatileimagefield_registry


class FittedImage(SizedImage):
    """
    Puts an image into a bounding box.
    Suitable for images with white or transparent background.
    """

    filename_key = 'fitto'

    def process_image(self,
                      image, image_format, save_kwargs,
                      width, height):
        """
        Returns a BytesIO instance of `image` pasted to a box.
        Dimensions are `width`x`height`.
        """
        dimensions = (width, height)
        imagefile = BytesIO()
        bgfile = BytesIO()
        image.thumbnail(
            (width, height),
            Image.ANTIALIAS
        )
        image.save(
            imagefile,
            **save_kwargs
        )
        if image.mode == 'RGBA':
            bg = Image.new('RGBA', dimensions)
            bg.paste(image, ((width - image.width) // 2, (height - image.height) // 2), mask=image)
        else:
            bg = Image.new('RGB', dimensions, 'white')
            bg.paste(image, ((width - image.width) // 2, (height - image.height) // 2))
        bg.save(
            bgfile,
            **save_kwargs
        )
        return bgfile


versatileimagefield_registry.register_sizer('fitto', FittedImage)
