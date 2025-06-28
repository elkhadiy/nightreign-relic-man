import pyautogui
import pydirectinput
import time
import uuid


def goto_relic_rite():
    GOTO_RELIC_RITE_SEQUENCE = ["m", "down", "down", "down", "f"]
    pydirectinput.write(GOTO_RELIC_RITE_SEQUENCE, interval=0.2)
    time.sleep(1)


def order_relics_by_color():
    ORDER_BY_COLOR_SEQUENCE = ["4", "f2", "f", "down", "down", "f", "q"]
    pydirectinput.write(ORDER_BY_COLOR_SEQUENCE, interval=0.2)
    time.sleep(1)


def goto_first_relic():
    pydirectinput.press("d", interval=0.2)
    # Move mouse onto the first relic
    screen_size = pyautogui.size()
    first_relic_x_rel = 1295 / 2560
    first_relic_y_rel = 340 / 1440
    pydirectinput.moveTo(
        int(screen_size.width * first_relic_x_rel),
        int(screen_size.height * first_relic_y_rel)
    )
    time.sleep(1)


def grab_relic(filename = f"{uuid.uuid4()}.png"):
    screen_size = pyautogui.size()

    left_rel = 1410 / 2560
    top_rel = 1024 / 1440
    width_rel = 846 / 2560
    height_rel = 306 / 1440

    im = pyautogui.screenshot(region=(
        int(screen_size.width * left_rel), int(screen_size.height * top_rel),
        int(screen_size.width * width_rel), int(screen_size.height * height_rel)
    ))

    im.save(filename)


if __name__ == "__main__":
    
    print("You have 3 seconds to focus the game!")
    time.sleep(2)

    goto_relic_rite()
    order_relics_by_color()
    goto_first_relic()

    for i in range(5):
        grab_relic(f"relics/{i}.png")
        pydirectinput.press("right")
