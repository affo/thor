import unittest

from thor import execute_string, ThorException

class TestParser(unittest.TestCase):
    def exec(self, stmt):
        try:
            execute_string(stmt)
            return None
        except ThorException as e:
            return str(e)

    def test_ok(self):
        self.assertEqual(self.exec("5 + 5;"), None)

    def test_ko(self):
        self.assertEqual(self.exec("5 + 5"), "line 1:5 missing ';' at '<EOF>'")
