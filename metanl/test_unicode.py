# -*- coding: utf-8 -*-
from ftfy import fix_bad_encoding, WINDOWS_1252_GREMLINS
import unicodedata

def test_all_bmp_characters():
    for index in xrange(0xa0, 0xfffd):
        if unicodedata.category(unichr(index)) not in ('Co', 'Cn'):
            garble = unichr(index).encode('utf-8').decode('latin-1')
            if index not in WINDOWS_1252_GREMLINS:
                assert fix_bad_encoding(garble) == unichr(index)

phrases = [
    u"\u201CI'm not such a fan of Charlotte Brontë\u2026\u201D",
    u"\u201CI'm not such a fan of Charlotte Brontë\u2026\u201D",
    u"\u2039ALLÍ ESTÁ\u203A",
    u"\u2014ALLÍ ESTÁ\u2014",
    u"AHÅ™, the new sofa from IKEA®",
    #u"\u2014a radius of 10 Å\u2014",
]
def test_valid_phrases():
    for phrase in phrases:
        print phrase
        yield check_phrase, phrase
        # make it not just confirm based on the opening punctuation
        yield check_phrase, phrase[1:]

def check_phrase(text):
    assert fix_bad_encoding(text) == text, text


