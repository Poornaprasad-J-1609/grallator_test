#!/usr/bin/env python3
import time
import pygame

def main():
    pygame.init()
    pygame.joystick.init()

    print("=" * 70)
    print("PYGAME JOYSTICK VIBRATION TEST")
    print("=" * 70)
    print("pygame version :", pygame.version.ver)
    print("SDL version    :", pygame.version.SDL)
    print("joystick count :", pygame.joystick.get_count())
    print("=" * 70)

    if pygame.joystick.get_count() == 0:
        print("ERROR: No joystick detected.")
        pygame.quit()
        return

    joy = pygame.joystick.Joystick(0)
    joy.init()

    print("Joystick name :", joy.get_name())
    print("Joystick GUID :", joy.get_guid())
    print("Axes          :", joy.get_numaxes())
    print("Buttons       :", joy.get_numbuttons())
    print("Hats          :", joy.get_numhats())
    print("=" * 70)

    print("Starting vibration...")
    print("Press Ctrl+C to stop.")
    print("=" * 70)

    try:
        while True:
            pygame.event.pump()

            ok = joy.rumble(1.0, 1.0, 1000)
            print("rumble returned:", ok, end="\r")

            if not ok:
                print("\nERROR: pygame detected joystick, but rumble is not supported by SDL.")
                print("For Logitech F710, switch to X mode, unplug/replug receiver, then run again.")
                break

            time.sleep(0.8)

    except KeyboardInterrupt:
        print("\nCtrl+C detected. Stopping vibration...")

    finally:
        try:
            joy.stop_rumble()
        except Exception:
            pass

        joy.quit()
        pygame.joystick.quit()
        pygame.quit()
        print("Stopped safely.")

if __name__ == "__main__":
    main()
