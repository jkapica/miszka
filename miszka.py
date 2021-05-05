import shlex
import sys
from argparse import ArgumentParser
from itertools import count
from random import randint
from time import sleep
from win32api import GetCursorPos, SetCursorPos, mouse_event
from win32con import MOUSEEVENTF_LEFTUP, MOUSEEVENTF_LEFTDOWN


def parse_args(argv=None):
    ap = ArgumentParser()
    ap.add_argument(
        '--no-click',
        dest='click',
        action='store_false',
        default=True
    )
    ap.add_argument(
        '--park-delay',
        type=float,
        default=60
    )
    ap.add_argument(
        '--jitter-delay',
        type=float,
        default=120
    )
    ap.add_argument(
        '--iterations',
        type=int,
        default=2*30
    )

    if argv is None:
        argv = sys.argv
    elif isinstance(argv, str):
        argv = shlex.split(argv, posix=False)

    if argv[0] in __file__ and not argv[0].startswith('-'):
        argv = argv[1:]
    return ap.parse_args(argv)


def main(argv=None):
    pargs = parse_args(argv)

    start = prev = GetCursorPos()
    sleep(pargs.park_delay)

    counter = count(pargs.iterations, -1)
    while next(counter) > 0:
        sleep(pargs.jitter_delay)
        if GetCursorPos() == prev:  # No user action - run around parking spot
            SetCursorPos([i + randint(-5, 5) for i in start])
            if pargs.click:
                mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0)
                sleep(0.2)
                mouse_event(MOUSEEVENTF_LEFTUP, 0, 0)
        else:  # Moved since last check - reset parking spot
            start = GetCursorPos()
        prev = GetCursorPos()


if __name__ == '__main__':
    sys.exit(main(sys.argv))
