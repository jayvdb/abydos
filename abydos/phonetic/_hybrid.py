# -*- coding: utf-8 -*-

# Copyright 2018 by Christopher C. Little.
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

"""abydos.phonetic._hybrid.

The phonetic._hybrid module implements hybrid phonetic algorithms:

    - Oxford Name Compression Algorithm (ONCA)
    - MetaSoundex
"""

from __future__ import unicode_literals

from ._es import PhoneticSpanish, SpanishMetaphone
from ._metaphone import Metaphone
from ._nysiis import NYSIIS
from ._phonetic import Phonetic
from ._soundex import Soundex

__all__ = ['MetaSoundex', 'ONCA', 'metasoundex', 'onca']


class ONCA(Phonetic):
    """Oxford Name Compression Algorithm (ONCA).

    This is the Oxford Name Compression Algorithm, based on :cite:`Gill:1997`.

    I can find no complete description of the "anglicised version of the NYSIIS
    method" identified as the first step in this algorithm, so this is likely
    not a precisely correct implementation, in that it employs the standard
    NYSIIS algorithm.
    """

    _nysiis = NYSIIS()
    _soundex = Soundex()

    def encode(self, word, max_length=4, zero_pad=True):
        """Return the Oxford Name Compression Algorithm (ONCA) code for a word.

        :param str word: the word to transform
        :param int max_length: the maximum length (default 5) of the code to
            return
        :param bool zero_pad: pad the end of the return value with 0s to
            achieve a max_length string
        :returns: the ONCA code
        :rtype: str

        >>> pe = ONCA()
        >>> pe.encode('Christopher')
        'C623'
        >>> pe.encode('Niall')
        'N400'
        >>> pe.encode('Smith')
        'S530'
        >>> pe.encode('Schmidt')
        'S530'
        """
        # In the most extreme case, 3 characters of NYSIIS input can be
        # compressed to one character of output, so give it triple the
        # max_length.
        return self._soundex.encode(
            self._nysiis.encode(word, max_length=max_length * 3),
            max_length,
            zero_pad=zero_pad,
        )


def onca(word, max_length=4, zero_pad=True):
    """Return the Oxford Name Compression Algorithm (ONCA) code for a word.

    This is a wrapper for :py:meth:`ONCA.encode`.

    :param str word: the word to transform
    :param int max_length: the maximum length (default 5) of the code to return
    :param bool zero_pad: pad the end of the return value with 0s to achieve a
        max_length string
    :returns: the ONCA code
    :rtype: str

    >>> onca('Christopher')
    'C623'
    >>> onca('Niall')
    'N400'
    >>> onca('Smith')
    'S530'
    >>> onca('Schmidt')
    'S530'
    """
    return ONCA().encode(word, max_length, zero_pad)


class MetaSoundex(Phonetic):
    """MetaSoundex.

    This is based on :cite:`Koneru:2017`. Only English ('en') and Spanish
    ('es') languages are supported, as in the original.
    """

    _trans = dict(
        zip(
            (ord(_) for _ in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'),
            '07430755015866075943077514',
        )
    )
    _phonetic_spanish = PhoneticSpanish()
    _spanish_metaphone = SpanishMetaphone()
    _metaphone = Metaphone()

    def metasoundex(self, word, lang='en'):
        """Return the MetaSoundex code for a word.

        :param str word: the word to transform
        :param str lang: either 'en' for English or 'es' for Spanish
        :returns: the MetaSoundex code
        :rtype: str

        >>> pe = MetaSoundex()
        >>> pe.encode('Smith')
        '4500'
        >>> pe.encode('Waters')
        '7362'
        >>> pe.encode('James')
        '1520'
        >>> pe.encode('Schmidt')
        '4530'
        >>> pe.encode('Ashcroft')
        '0261'
        >>> pe.encode('Perez', lang='es')
        '094'
        >>> pe.encode('Martinez', lang='es')
        '69364'
        >>> pe.encode('Gutierrez', lang='es')
        '83994'
        >>> pe.encode('Santiago', lang='es')
        '4638'
        >>> pe.encode('Nicolás', lang='es')
        '6754'
        """
        if lang == 'es':
            return self._phonetic_spanish.encode(
                self._spanish_metaphone.encode(word)
            )

        word = self._soundex.encode(self._metaphone.encode(word))
        word = word[0].translate(self._trans) + word[1:]
        return word


def metasoundex(word, lang='en'):
    """Return the MetaSoundex code for a word.

    This is a wrapper for :py:meth:`MetaSoundex.encode`.

    :param str word: the word to transform
    :param str lang: either 'en' for English or 'es' for Spanish
    :returns: the MetaSoundex code
    :rtype: str

    >>> metasoundex('Smith')
    '4500'
    >>> metasoundex('Waters')
    '7362'
    >>> metasoundex('James')
    '1520'
    >>> metasoundex('Schmidt')
    '4530'
    >>> metasoundex('Ashcroft')
    '0261'
    >>> metasoundex('Perez', lang='es')
    '094'
    >>> metasoundex('Martinez', lang='es')
    '69364'
    >>> metasoundex('Gutierrez', lang='es')
    '83994'
    >>> metasoundex('Santiago', lang='es')
    '4638'
    >>> metasoundex('Nicolás', lang='es')
    '6754'
    """
    return MetaSoundex().encode(word, lang)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
