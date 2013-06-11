from algorithm import kmp, bm
import unittest


class TestKMP(unittest.TestCase):
    def test_notin(self):
        text = 'annbcdanacadsannannabnna'
        pattern = 'annacanna'
        self.assertEqual(text.find(pattern),
                kmp(text, pattern)
                )

    def test_in(self):
        text = 'annbcdanacadsannannabnna'
        pattern = 'annann'
        self.assertEqual(text.find(pattern),
                kmp(text, pattern)
                )

class TestBM(unittest.TestCase):
    def test_notin(self):
        text = 'annbcdanacadsannannabnna'
        pattern = 'annacanna'
        self.assertEqual(text.find(pattern),
                bm(text, pattern)
                )

    def test_in(self):
        text = 'annbcdanacadsannannabnna'
        pattern = 'annann'
        self.assertEqual(text.find(pattern),
                kmp(text, pattern)
                )

        text = 'abcabcabcabcabcdabcacabcabcacb'
        pattern = 'dabc'
        self.assertEqual(text.find(pattern),
                kmp(text, pattern)
                )



if __name__ == '__main__':
    unittest.main()
