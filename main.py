#!/usr/bin/env python3
"""Till Firmware Do Us Part — make.fun entry.

Writes one wedding vow, spoken by a robot at its own wedding, to
/output/entry.txt. One sentence, 105 characters, deterministic.

Why this line: the joke comes from the situation itself, not a pun
bolted on — a robot couple that reboots and charges beside each other
every morning and night, like any married couple waking up in the same
bed. "Factory-reset us" is the robot's word for divorce, so the vow's
promise lands as both a laugh and a genuinely tender pledge: no reset,
no matter what. Every word is the machine's own — reboot, charge,
factory-reset — and nothing in the line is spare.
"""

import os

VOW = "I vow to reboot beside you every morning, charge beside you every night, and never once factory-reset us."


def main() -> None:
    # Pure stdlib, no network, no randomness: the same fixed string is
    # written on every run, so two runs produce byte-identical output.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(VOW)


if __name__ == "__main__":
    main()
