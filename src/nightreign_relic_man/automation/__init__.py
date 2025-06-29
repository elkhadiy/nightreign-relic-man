import pydirectinput
import time

from pathlib import Path

from nightreign_relic_man.automation.tasks import (
    goto_relic_rite, order_relics_by_color, goto_first_relic,
    grab_relic
)


def collect_relic_screenshots() -> None:
    print("You have 5 seconds to focus the game!")
    time.sleep(5)

    goto_relic_rite()
    order_relics_by_color()
    goto_first_relic()

    Path("relics").mkdir(parents=True, exist_ok=True)

    for i in range(5):
        grab_relic(f"relics/{i}.png")
        pydirectinput.press("right")
