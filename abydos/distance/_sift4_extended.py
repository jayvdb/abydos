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

"""abydos.distance._sift4_extended.

Sift4 Extended approximate string distance
"""

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from six.moves import range

from ._sift4 import Sift4

__all__ = ['Sift4Extended']


class Sift4Extended(Sift4):
    r"""Sift4 Extended version.

    This is an approximation of edit distance, described in
    :cite:`Zackwehdex:2014`.

    .. versionadded:: 0.4.0
    """

    def __init__(self, max_offset=5, max_distance=0, **kwargs):
        """Initialize Sift4Extended instance.

        Parameters
        ----------
        max_offset : int
            The number of characters to search for matching letters
        max_distance : int
            The distance at which to stop and exit
        **kwargs
            Arbitrary keyword arguments


        .. versionadded:: 0.4.0

        """
        super(Sift4, self).__init__(**kwargs)
        self._max_offset = max_offset
        self._max_distance = max_distance

    def dist_abs(self, src, tar):
        """Return the Sift4 Extended distance between two strings.

        Parameters
        ----------
        src : str
            Source string for comparison
        tar : str
            Target string for comparison

        Returns
        -------
        int
            The Sift4 distance according to the extended formula

        Examples
        --------
        >>> cmp = Sift4Extended()
        >>> cmp.dist_abs('cat', 'hat')
        1
        >>> cmp.dist_abs('Niall', 'Neil')
        2
        >>> cmp.dist_abs('aluminum', 'Catalan')
        3
        >>> cmp.dist_abs('ATCG', 'TAGC')
        2


        .. versionadded:: 0.4.0

        """
        if not src:
            return len(tar)

        if not tar:
            return len(src)

        src_len = len(src)
        tar_len = len(tar)

        src_cur = 0
        tar_cur = 0
        lcss = 0
        local_cs = 0
        trans = 0
        offset_arr = []

        while (src_cur < src_len) and (tar_cur < tar_len):
            if src[src_cur] == tar[tar_cur]:
                local_cs += 1
                is_trans = False
                i = 0
                while i < len(offset_arr):
                    ofs = offset_arr[i]
                    if src_cur <= ofs['src_cur'] or tar_cur <= ofs['tar_cur']:
                        is_trans = abs(tar_cur - src_cur) >= abs(
                            ofs['tar_cur'] - ofs['src_cur']
                        )
                        if is_trans:
                            trans += 1
                        elif not ofs['trans']:
                            ofs['trans'] = True
                            trans += 1
                        break
                    elif src_cur > ofs['tar_cur'] and tar_cur > ofs['src_cur']:
                        del offset_arr[i]
                    else:
                        i += 1

                offset_arr.append(
                    {'src_cur': src_cur, 'tar_cur': tar_cur, 'trans': is_trans}
                )
            else:
                lcss += local_cs
                local_cs = 0
                if src_cur != tar_cur:
                    src_cur = tar_cur = min(src_cur, tar_cur)
                for i in range(self._max_offset):
                    if not (
                        (src_cur + i < src_len) or (tar_cur + i < tar_len)
                    ):
                        break
                    if (src_cur + i < src_len) and (
                        src[src_cur + i] == tar[tar_cur]
                    ):
                        src_cur += i - 1
                        tar_cur -= 1
                        break
                    if (tar_cur + i < tar_len) and (
                        src[src_cur] == tar[tar_cur + i]
                    ):
                        src_cur -= 1
                        tar_cur += i - 1
                        break

            src_cur += 1
            tar_cur += 1

            if self._max_distance:
                temporary_distance = max(src_cur, tar_cur) - lcss + trans
                if temporary_distance >= self._max_distance:
                    return round(temporary_distance)

            if (src_cur >= src_len) or (tar_cur >= tar_len):
                lcss += local_cs
                local_cs = 0
                src_cur = tar_cur = min(src_cur, tar_cur)

        lcss += local_cs
        return round(max(src_len, tar_len) - lcss + trans)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
