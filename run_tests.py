import unittest
'''
the file in /tests/homework/b_in_proc_out/tests_in_proc_out
has the test functions
'''

from tests.homework.b_in_proc_out import test_in_proc_out
from tests.examples.a_example import tests_devprocess

suite = unittest.TestLoader().loadTestsFromModule(test_in_proc_out)
suite.addTests(unittest.TestLoader().loadTestsFromModule(tests_devprocess))

unittest.TextTestRunner(verbosity=2).run(suite)
