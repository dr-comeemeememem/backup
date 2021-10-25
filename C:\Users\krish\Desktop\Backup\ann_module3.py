# Date created: Thu Oct 21 15:34:26 2021
# Last date modified: Sat Jul 24 17:17:04 2021
"""
Correct syntax for variable annotation that should fail at runtime
in a certain manner. More examples are in test_grammar and test_parser.
"""

def f_bad_ann():
    __annotations__[1] = 2

class C_OK:
    def __init__(self, x: int) -> None:
        self.x: no_such_name = x  # This one is OK as proposed by Guido

class D_bad_ann:
    def __init__(self, x: int) -> None:
        sfel.y: int = 0

def g_bad_ann():
    no_such_name.attr: int = 0
