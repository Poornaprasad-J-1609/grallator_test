#!/usr/bin/env python3
import os
import time

os.environ.setdefault("SDL_VIDEODRIVER", "dummy")

import pygame as pg


def main():
    pg.display.init()
    pg.joystick.init()

    joystick_count = pg.joystick.get_count()
    print(f"Found {joystick_count} joystick(s)")

    joysticks = []
    for index in range(joystick_count):
        joystick = pg.joystick.Joystick(index)
        joystick.init()
        joysticks.append(joystick)
        print(
            f"[{index}] {joystick.get_name()} "
            f"axes={joystick.get_numaxes()} "
            f"buttons={joystick.get_numbuttons()} "
            f"hats={joystick.get_numhats()}"
        )

    print("Listening for joystick events. Press Ctrl+C to stop.")

    try:
        while True:
            for event in pg.event.get():
                print(event)
            time.sleep(0.01)
    except KeyboardInterrupt:
        print("\nStopped.")
    finally:
        for joystick in joysticks:
            joystick.quit()
        pg.joystick.quit()
        pg.display.quit()


if __name__ == "__main__":
    main()
