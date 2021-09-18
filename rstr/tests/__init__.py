import unittest
from rstr.tests import test_rstr, test_xeger, test_package_level_access


def suite():
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(test_rstr)
    suite.addTests(loader.loadTestsFromModule(test_xeger))
    suite.addTests(loader.loadTestsFromModule(test_package_level_access))
    return suite
