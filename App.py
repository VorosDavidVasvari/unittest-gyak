import unittest

def fibo(n: int) -> int:
    if n < 0: return -1
    elif n == 0: return 0

    a = 0
    b = 1

    for _ in range(n - 1):
        c = a + b
        a = b
        b = c

    return b


class FibonacciTest(unittest.TestCase):
    def test_0(self):
        self.assertEqual(fibo(0), 0)
    def test_1_2(self):
        self.assertListEqual([fibo(1), fibo(2)], [1, 1])
    def test_3(self):
        self.assertFalse(fibo(3) == 3)
    def test_10(self):
        self.assertLess(fibo(10), 56)
    def test_42(self):
        self.assertTrue(fibo(42) == 267914296)

if __name__ == "__main__":
    unittest.main()
