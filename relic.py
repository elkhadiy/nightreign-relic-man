import cv2
import numpy as np
import tesserocr
import yaml

from dataclasses import dataclass, asdict
from PIL import Image

from utils import TextZone


TESSDATA_PATH='ressources/tesserocr/tessdata-4.1.0'


@dataclass
class Relic:
    name: str
    color: str
    effects: tuple[str]

    @classmethod
    def from_screenshot(cls, screenshot: Image.Image):
        """Constructs a Relic by extracting information from a game screenshot.

        Args:
            screenshot: expected to be a PIL.Image.Image
        """
        # Processing the image a bit so that the OCR returns an empty string for all cases
        # when nothing is there instead of hallucinating characters
        image = screenshot.resize((screenshot.width * 10, screenshot.height * 10))
        image = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2GRAY)
        _, image = cv2.threshold(image, 75, 255, cv2.THRESH_BINARY)
        image = Image.fromarray(image)

        # Process the relic name first,
        # if nothing was found it means the slot was empty
        # so we return None
        relic_name_rect = TextZone(
            0 / 846, 15 / 306,
            846 / 846, 45 / 306,
            image.width, image.height
        )
        relic_name_im = image.crop(relic_name_rect.pil_crop())
        relic_name = cls.image2text(relic_name_im)

        if not relic_name:
            return None
        
        # We know the relic color from the name
        color = cls.name2color(relic_name)

        # Lastly let's collect our effects in a list
        effects = []

        first_effect_rect = TextZone(
            68 / 846, 61 / 306,
            781 / 846, 80 / 306,
            image.width, image.height
        )

        second_effect_rect = TextZone(
            68 / 846, 141 / 306,
            781 / 846, 80 / 306,
            image.width, image.height
        )

        third_effect_rect = TextZone(
            68 / 846, 221 / 306,
            781 / 846, 80 / 306,
            image.width, image.height
        )
        
        first_effect_im = image.crop(first_effect_rect.pil_crop())
        second_effect_im = image.crop(second_effect_rect.pil_crop())
        third_effect_im = image.crop(third_effect_rect.pil_crop())

        first_effect = cls.image2text(first_effect_im)
        second_effect = cls.image2text(second_effect_im)
        third_effect = cls.image2text(third_effect_im)

        if first_effect:
            effects.append(first_effect)
        if second_effect:
            effects.append(second_effect)
        if third_effect:
            effects.append(third_effect)

        return cls(relic_name, color, effects)

    @staticmethod
    def image2text(image):
        return tesserocr.image_to_text(image, path=TESSDATA_PATH, psm=6) \
                        .translate(str.maketrans({'\n': ' ', "’": "'"})) \
                        .strip()

    @staticmethod
    def name2color(name):
        """Converts the fancy schmancy LORE color name into a normal one."""
        if 'Burning' in name:
            return 'Red'
        if 'Tranquil' in name:
            return 'Green'
        if 'Drizzly' in name:
            return 'Blue'
        if 'Luminous' in name:
            return 'Yellow'
        
        # If we are still here we're dealing with a unique relic,
        # let's find out which one and return it
        with open("unique_relics.yml", "r") as f:
            unique_relics = yaml.safe_load(f)
        
        for color, list_of_names in unique_relics.items():
            if name in list_of_names:
                return color


    def __hash__(self):
        """My assumption is that we can have two identical relics with the same effects and color.
        They should be considered to be different by collections that use hashing.
        """
        return id(self)


if __name__ == "__main__":

    # Quick and dirty way to build my full relic_inventory.yml

    inventory = []

    for i in range(14*8):
        image = Image.open(f"relics/{i}.png")
        relic = Relic.from_screenshot(image)
        if relic:
            inventory.append(asdict(relic))

    with open('relic_inventory.yml', 'w') as f:
        f.write(yaml.dump(inventory))
