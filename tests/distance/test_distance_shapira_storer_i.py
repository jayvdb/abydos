# -*- coding: utf-8 -*-

# Copyright 2019 by Christopher C. Little.
# This file is part of Abydos.
#
# Abydos is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Abydos is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Abydos. If not, see <http://www.gnu.org/licenses/>.

"""abydos.tests.distance.test_distance_shapira_storer_i.

This module contains unit tests for abydos.distance.ShapiraStorerI
"""

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import unittest

from abydos.distance import ShapiraStorerI


class ShapiraStorerITestCases(unittest.TestCase):
    """Test ShapiraStorerI functions.

    abydos.distance.ShapiraStorerI
    """

    cmp = ShapiraStorerI()

    def test_shapira_storer_i_dist(self):
        """Test abydos.distance.ShapiraStorerI.dist."""
        # Base cases
        self.assertEqual(self.cmp.dist('', ''), 0.0)
        self.assertEqual(self.cmp.dist('a', ''), 1.0)
        self.assertEqual(self.cmp.dist('', 'a'), 1.0)
        self.assertEqual(self.cmp.dist('abc', ''), 1.0)
        self.assertEqual(self.cmp.dist('', 'abc'), 1.0)
        self.assertEqual(self.cmp.dist('abc', 'abc'), 0.0)
        self.assertEqual(self.cmp.dist('abcd', 'efgh'), 2.0)

        self.assertAlmostEqual(self.cmp.dist('Nigel', 'Niall'), 0.8)
        self.assertAlmostEqual(self.cmp.dist('Niall', 'Nigel'), 0.8)
        self.assertAlmostEqual(self.cmp.dist('Colin', 'Coiln'), 0.2)
        self.assertAlmostEqual(self.cmp.dist('Coiln', 'Colin'), 0.2)
        self.assertAlmostEqual(self.cmp.dist('ATCAACGAGT', 'AACGATTAG'), 0.4)

    def test_shapira_storer_i_sim(self):
        """Test abydos.distance.ShapiraStorerI.sim."""
        # Base cases
        self.assertEqual(self.cmp.sim('', ''), 1.0)
        self.assertEqual(self.cmp.sim('a', ''), 0.0)
        self.assertEqual(self.cmp.sim('', 'a'), 0.0)
        self.assertEqual(self.cmp.sim('abc', ''), 0.0)
        self.assertEqual(self.cmp.sim('', 'abc'), 0.0)
        self.assertEqual(self.cmp.sim('abc', 'abc'), 1.0)
        self.assertEqual(self.cmp.sim('abcd', 'efgh'), -1.0)

        self.assertAlmostEqual(self.cmp.sim('Nigel', 'Niall'), 0.2)
        self.assertAlmostEqual(self.cmp.sim('Niall', 'Nigel'), 0.2)
        self.assertAlmostEqual(self.cmp.sim('Colin', 'Coiln'), 0.8)
        self.assertAlmostEqual(self.cmp.sim('Coiln', 'Colin'), 0.8)
        self.assertAlmostEqual(self.cmp.sim('ATCAACGAGT', 'AACGATTAG'), 0.6)

    def test_shapira_storer_i_dist_abs(self):
        """Test abydos.distance.ShapiraStorerI.dist_abs."""
        # Base cases
        self.assertEqual(self.cmp.dist_abs('', ''), 0)
        self.assertEqual(self.cmp.dist_abs('a', ''), 1)
        self.assertEqual(self.cmp.dist_abs('', 'a'), 1)
        self.assertEqual(self.cmp.dist_abs('abc', ''), 3)
        self.assertEqual(self.cmp.dist_abs('', 'abc'), 3)
        self.assertEqual(self.cmp.dist_abs('abc', 'abc'), 0)
        self.assertEqual(self.cmp.dist_abs('abcd', 'efgh'), 8)

        self.assertAlmostEqual(self.cmp.dist_abs('Nigel', 'Niall'), 4)
        self.assertAlmostEqual(self.cmp.dist_abs('Niall', 'Nigel'), 4)
        self.assertAlmostEqual(self.cmp.dist_abs('Colin', 'Coiln'), 1)
        self.assertAlmostEqual(self.cmp.dist_abs('Coiln', 'Colin'), 1)
        self.assertAlmostEqual(self.cmp.dist_abs('ATCAACGAGT', 'AACGATTAG'), 4)


if __name__ == '__main__':
    unittest.main()