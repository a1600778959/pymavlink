#!/usr/bin/env python

"""Unit tests for MAVLink utility mode mappings."""

import unittest

from pymavlink import mavutil


class MAVUtilModeMappingTest(unittest.TestCase):

    def test_rover_recent_modes_have_unique_mappings(self):
        """Rover initialization, AOA follow and patrol keep distinct IDs."""
        expected_modes = {
            16: 'INITIALISING',
            17: 'AOAFOLLOW',
            18: 'PATROL',
        }

        actual_modes = {
            mode_id: mavutil.mode_mapping_rover.get(mode_id)
            for mode_id in expected_modes
        }
        self.assertEqual(actual_modes, expected_modes)


if __name__ == '__main__':
    unittest.main()
