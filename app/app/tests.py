from django.test import SimpleTestCase
from . import calc

class CalculateTest(SimpleTestCase):
    
    def test_add_case(self):
        res = calc.add(5,6)
        self.assertEqual(res,11)