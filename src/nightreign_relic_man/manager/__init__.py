import yaml

from dataclasses import asdict
from pathlib import Path
from PIL import Image

from nightreign_relic_man.manager.relic import Relic


def build_inventory_from_screenshots() -> None:
    # Quick and dirty way to build my full relic_inventory.yml

    inventory = []

    for image_file_name in Path('relics').iterdir():
        image = Image.open(image_file_name)
        relic = Relic.from_screenshot(image)
        if relic:
            inventory.append(asdict(relic))

    with open('relic_inventory.yml', 'w') as f:
        f.write(yaml.dump(inventory))
