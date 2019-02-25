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

"""abydos.tests.distance.test_distance_kent_foster_i.

This module contains unit tests for abydos.distance.KentFosterI
"""

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import unittest

from abydos.distance import KentFosterI


class KentFosterITestCases(unittest.TestCase):
    """Test KentFosterI functions.

    abydos.distance.KentFosterI
    """

    cmp = KentFosterI()
    cmp_no_d = KentFosterI(alphabet=0)

    def test_kent_foster_i_sim(self):
        """Test abydos.distance.KentFosterI.sim."""
        # Base cases
        self.assertEqual(self.cmp.sim('', ''), float('nan'))
        self.assertEqual(self.cmp.sim('a', ''), 0.0)
        self.assertEqual(self.cmp.sim('', 'a'), 0.0)
        self.assertEqual(self.cmp.sim('abc', ''), 0.0)
        self.assertEqual(self.cmp.sim('', 'abc'), 0.0)
        self.assertEqual(self.cmp.sim('abc', 'abc'), float('nan'))
        self.assertEqual(self.cmp.sim('abcd', 'efgh'), -0.3333333333333333)

        self.assertAlmostEqual(self.cmp.sim('Nigel', 'Niall'), -0.2)
        self.assertAlmostEqual(self.cmp.sim('Niall', 'Nigel'), -0.2)
        self.assertAlmostEqual(self.cmp.sim('Colin', 'Coiln'), -0.2)
        self.assertAlmostEqual(self.cmp.sim('Coiln', 'Colin'), -0.2)
        self.assertAlmostEqual(
            self.cmp.sim('ATCAACGAGT', 'AACGATTAG'), -0.1395348837
        )

    def test_kent_foster_i_dist(self):
        """Test abydos.distance.KentFosterI.dist."""
        # Base cases
        self.assertEqual(self.cmp.dist('', ''), float('nan'))
        self.assertEqual(self.cmp.dist('a', ''), 1.0)
        self.assertEqual(self.cmp.dist('', 'a'), 1.0)
        self.assertEqual(self.cmp.dist('abc', ''), 1.0)
        self.assertEqual(self.cmp.dist('', 'abc'), 1.0)
        self.assertEqual(self.cmp.dist('abc', 'abc'), float('nan'))
        self.assertEqual(self.cmp.dist('abcd', 'efgh'), 1.3333333333333333)

        self.assertAlmostEqual(self.cmp.dist('Nigel', 'Niall'), 1.2)
        self.assertAlmostEqual(self.cmp.dist('Niall', 'Nigel'), 1.2)
        self.assertAlmostEqual(self.cmp.dist('Colin', 'Coiln'), 1.2)
        self.assertAlmostEqual(self.cmp.dist('Coiln', 'Colin'), 1.2)
        self.assertAlmostEqual(
            self.cmp.dist('ATCAACGAGT', 'AACGATTAG'), 1.1395348837
        )


if __name__ == '__main__':
    unittest.main()
