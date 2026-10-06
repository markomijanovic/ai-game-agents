import argparse
import unittest
from cli import parse_args, parse_bool


class CommandLineTests(unittest.TestCase):
    def test_false_strings(self):
        for value in ('False', 'FALSE', '0', 'no', 'off'):
            self.assertFalse(parse_bool(value))

    def test_true_strings(self):
        for value in ('true', 'TRUE', '1', 'yes', 'on'):
            self.assertTrue(parse_bool(value))

    def test_invalid_boolean(self):
        with self.assertRaises(argparse.ArgumentTypeError):
            parse_bool('maybe')

    def test_original_positional_interface(self):
        args = parse_args(['RandomAgent', 'example_map.txt', '5', '0', '3', 'false'])
        self.assertEqual((args.rounds, args.elapsed, args.depth, args.debug), (5, 0, 3, False))


if __name__ == '__main__':
    unittest.main()
