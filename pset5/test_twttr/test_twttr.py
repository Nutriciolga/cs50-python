# In a file called twttr.py, reimplement Setting up my twttr from Problem Set 2,
# restructuring your code per the below, wherein shorten expects a str as input and returns that same
# str but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.

# Then, in a file called test_twttr.py, implement one or more functions that collectively test your
# implementation of shorten thoroughly, each of whose names should begin with test_ so that you can
# execute your tests with:

# pytest test_twttr.py

from twttr import shorten


def test_digitals():
    assert shorten("444word") == "444wrd"
    assert shorten("444") == "444"


def test_signs():
    assert shorten("-.:?woord") == "-.:?wrd"
    

def test_letters():
    assert shorten("ALARM") == "LRM"
    assert shorten("alarm") == "lrm"
    assert shorten("AlArM") == "lrM"