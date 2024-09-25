import unittest
from givememoneypastaga.main import give_me_money_pastaga

class MyTestCase(unittest.TestCase):
    def test_something(self):
        compte_en_banque = give_me_money_pastaga(8, 10)
        self.assertEqual(compte_en_banque, 18)
        
if __name__ == '__main__':
    unittest.main()
