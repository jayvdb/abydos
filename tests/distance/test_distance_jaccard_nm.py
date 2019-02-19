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

"""abydos.tests.distance.test_distance_jaccard_nm.

This module contains unit tests for abydos.distance.JaccardNM
"""

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import unittest

from abydos.distance import JaccardNM


class JaccardNMTestCases(unittest.TestCase):
    """Test JaccardNM functions.

    abydos.distance.JaccardNM
    """

    cmp = JaccardNM()

    def test_jaccard_nm_sim(self):
        """Test abydos.distance.JaccardNM.sim."""
        # Base cases
        self.assertEqual(self.cmp.sim('', ''), float('nan'))
        self.assertEqual(self.cmp.sim('a', ''), float('nan'))
        self.assertEqual(self.cmp.sim('', 'a'), float('nan'))
        self.assertEqual(self.cmp.sim('abc', ''), float('nan'))
        self.assertEqual(self.cmp.sim('', 'abc'), float('nan'))
        self.assertEqual(self.cmp.sim('abc', 'abc'), float('nan'))
        self.assertEqual(self.cmp.sim('abcd', 'efgh'), float('nan'))

        self.assertAlmostEqual(self.cmp.sim('Nigel', 'Niall'), float('nan'))
        self.assertAlmostEqual(self.cmp.sim('Niall', 'Nigel'), float('nan'))
        self.assertAlmostEqual(self.cmp.sim('Colin', 'Coiln'), float('nan'))
        self.assertAlmostEqual(self.cmp.sim('Coiln', 'Colin'), float('nan'))
        self.assertAlmostEqual(
            self.cmp.sim('ATCAACGAGT', 'AACGATTAG'), float('nan')
        )

    def test_jaccard_nm_sim_score(self):
        """Test abydos.distance.JaccardNM.sim_score."""
        # Base cases
        self.assertEqual(self.cmp.sim_score('', ''), float('nan'))
        self.assertEqual(self.cmp.sim_score('a', ''), float('nan'))
        self.assertEqual(self.cmp.sim_score('', 'a'), float('nan'))
        self.assertEqual(self.cmp.sim_score('abc', ''), float('nan'))
        self.assertEqual(self.cmp.sim_score('', 'abc'), float('nan'))
        self.assertEqual(self.cmp.sim_score('abc', 'abc'), float('nan'))
        self.assertEqual(self.cmp.sim_score('abcd', 'efgh'), float('nan'))

        self.assertAlmostEqual(
            self.cmp.sim_score('Nigel', 'Niall'), float('nan')
        )
        self.assertAlmostEqual(
            self.cmp.sim_score('Niall', 'Nigel'), float('nan')
        )
        self.assertAlmostEqual(
            self.cmp.sim_score('Colin', 'Coiln'), float('nan')
        )
        self.assertAlmostEqual(
            self.cmp.sim_score('Coiln', 'Colin'), float('nan')
        )
        self.assertAlmostEqual(
            self.cmp.sim_score('ATCAACGAGT', 'AACGATTAG'), float('nan')
        )


if __name__ == '__main__':
    unittest.main()