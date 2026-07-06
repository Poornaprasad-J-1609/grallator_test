#!/usr/bin/env python3

import time

from robstride_dynamics import RobstrideBus
from robstride_dynamics.bus import Motor


motors = {
    "motor_1": Motor(
        id=127,
        model="rs-04",  # Replace with your ACTUAL motor model
    )
}


bus = RobstrideBus(
    channel="slcan0",
    motors=motors,
    bitrate=1_000_000,
)

bus.connect(handshake=False)

#target_position = 2.0



