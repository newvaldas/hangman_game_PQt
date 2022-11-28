import unittest

from utilities import string_to_letter

class UtilitiesTest(unittest.TestCase):
    def test_covert_string_into_list_of_strings(self):
        word = 'Antanas'
        expected_list = ['A', 'n', 't', 'a', 'n', 'a', 's']
        #Test 
        our_list = string_to_letter(word)
        #Assert
        self.assertEqual(our_list, expected_list)
if __name__ == '__main__':
    unittest.main()