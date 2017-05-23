from unittest import TestCase


class TestFind_permutations(TestCase):
    def test_find_permutations(self):
        try:
            from build import find_permutations
        except ImportError:
            self.assertFalse("no function found")

        self.assertEqual(find_permutations(None), None)
        self.assertEqual(find_permutations(''), '')
        string = 'AABC'
        expected = [
            'AABC', 'AACB', 'ABAC', 'ABCA',
            'ACAB', 'ACBA', 'BAAC', 'BACA',
            'BCAA', 'CAAB', 'CABA', 'CBAA'
        ]
        self.assertEqual(find_permutations(string), expected)
