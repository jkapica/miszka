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
        '--click',
        dest='click',
        action='store_true',
        default=False
    )
    ap.add_argument(
        '--delay', '-d',
        type=float,
        default=120,
        help='Delay between checks/moves',
    )
    ap.add_argument(
        '--iterations', '-i',
        type=int,
        default=2*30,
        help='How many checks/move to run',
    )
    ap.add_argument(
        '--no-anchor',
        action='store_false',
        dest='anchor',
        default=True,
        help='How many checks/move to run',
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

    anchor = prev = GetCursorPos()
    delay = pargs.delay

    counter = count(pargs.iterations, -1)
    while next(counter) > 0:
        sleep(delay)
        if GetCursorPos() == prev:  # No user action detected - make a move
            base = anchor if pargs.anchor else prev
            SetCursorPos([i + randint(-5, 5) for i in base])
            if pargs.click:
                mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0)
                sleep(0.2)
                mouse_event(MOUSEEVENTF_LEFTUP, 0, 0)
        else:  # Moved since last check - reset the anchor
            delay = 10
            anchor = GetCursorPos()
        delay = pargs.delay
        prev = GetCursorPos()


if __name__ == '__main__':
    sys.exit(main(sys.argv))
