import miszka
from miszka import main, parse_args


def test_round_trip():
    main('--iterations 3 --park-delay 0.5 --jitter-delay 0.1')


def test_pargs_no_click():
    pargs = parse_args('miszka.py --no-click')
    assert not pargs.click

    pargs = parse_args('--no-click')
    assert not pargs.click

    pargs = parse_args(f'{miszka.__file__} --no-click')
    assert not pargs.click
