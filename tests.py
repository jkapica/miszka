from win32api import GetCursorPos

import miszka
from miszka import main, parse_args


def test_round_trip():
    main('--iterations 3 --no-click --delay 0.1')


def test_pargs_no_click():
    pargs = parse_args('miszka.py')
    assert not pargs.click

    pargs = parse_args('--click')
    assert pargs.click

    pargs = parse_args(f'{miszka.__file__}')
    assert not pargs.click


def test_wondering():
    start_x, start_y = GetCursorPos()
    main('miszka.py --no-click --delay 0.01 -i 1000 --no-anchor')
    x, y = GetCursorPos()
    assert abs(x - start_x) <= 10
    assert abs(y - start_y) <= 10
    #  #
