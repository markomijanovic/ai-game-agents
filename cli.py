"""Command-line parsing independent of the graphical environment."""
import argparse

def parse_bool(value):
    normalized = value.lower()
    if normalized in ('true', '1', 'yes', 'on'):
        return True
    if normalized in ('false', '0', 'no', 'off'):
        return False
    raise argparse.ArgumentTypeError('debug must be true or false')

def positive(value):
    number = int(value)
    if number <= 0:
        raise argparse.ArgumentTypeError('value must be positive')
    return number

def nonnegative(value):
    number = int(value)
    if number < 0:
        raise argparse.ArgumentTypeError('value must be nonnegative')
    return number

def parse_args(argv=None):
    parser = argparse.ArgumentParser(description='Compare adversarial game agents.')
    parser.add_argument('agents', nargs='?', default='RandomAgent')
    parser.add_argument('map', nargs='?', default='example_map.txt')
    parser.add_argument('rounds', nargs='?', type=positive, default=5)
    parser.add_argument('elapsed', nargs='?', type=nonnegative, default=0)
    parser.add_argument('depth', nargs='?', type=positive, default=5)
    parser.add_argument('debug', nargs='?', type=parse_bool, default=True)
    return parser.parse_args(argv)
