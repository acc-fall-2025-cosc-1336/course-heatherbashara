import unittest
'''
the file in /tests/homework/b_in_proc_out/tests_in_proc_out
has the test functions
'''
from tests.homework.b_in_proc_out import test_in_proc_out

suite = unittest.TestLoader().loadTestsFromModule(test_in_proc_out)
unittest.TextTestRunner(verbosity=2).run(suite)
