import unittest
import rand_num_generator


class RandTest(unittest.TestCase):

    def test1(self):
        rn = 12
        val = 12
        result = rand_num_generator.random_guess(rn, val)
        self.assertEqual(result, True)

    def test2(self):
        rn = 10
        val = 12
        result = rand_num_generator.random_guess(rn, val)
        self.assertEqual(result, False)

    def test3(self):
        rn = 10
        val = 10
        result = rand_num_generator.random_guess(rn, val)
        self.assertEqual(result, True)


if __name__ == "__main__":
    unittest.main()
