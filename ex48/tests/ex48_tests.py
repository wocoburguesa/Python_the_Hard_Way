from nose.tools import *
from lex import lexicon

def test_diections():
    lexic = lexicon()
    #interesante lo de aca abajo
    assert_equal(lexicon().scan("north"), [('direction', 'north')])
    result = lexic.scan("nortH south east")
    assert_equal(result, [('direction', 'north'),
                          ('direction', 'south'),
                          ('direction', 'east')])

def test_verbs():
    lexic = lexicon()
    assert_equal(lexic.scan("go"), [('verb', 'go')])
    result = lexic.scan("go kill eat")
    assert_equal(result, [('verb', 'go'),
                          ('verb', 'kill'),
                          ('verb', 'eat')])

def test_stops():
    lexic = lexicon()
    assert_equal(lexic.scan("the"), [('stop', 'the')])
    result = lexic.scan("the in of")
    assert_equal(result, [('stop', 'the'),
                          ('stop', 'in'),
                          ('stop', 'of')])

def test_nouns():
    lexic = lexicon()
    assert_equal(lexic.scan("bear"), [('noun', 'bear')])
    result = lexic.scan("bear princess")
    assert_equal(result, [('noun', 'bear'),
                          ('noun', 'princess')])

def test_numbers():
    lexic = lexicon()
    assert_equal(lexic.scan("1234"), [('number', 1234)])
    result = lexic.scan("3 91234")
    assert_equal(result, [('number', 3),
                          ('number', 91234)])

def test_errors():
    lexic = lexicon()
    assert_equal(lexic.scan("ASDFADFASDF"), [('error', 'asdfadfasdf')])
    result = lexic.scan("bear IAS princess")
    assert_equal(result, [('noun', 'bear'),
                          ('error', 'ias'),
                          ('noun', 'princess')])
