import unittest

a = int(input("Podaj dzielną: "))
b = int(input("Podaj dzielnik: "))


def NWD(a, b):
    if b != 0:
        print(str(a) + " = " + str(b) + " * " + str(int((a - (a % b)) / b)) + " + " + str(a%b))
        return NWD(b, a % b)
    return a

print("\nNWD wynosi: ", NWD(a, b))


class Test_Euklides(unittest.TestCase):
    def Test_Euklides(self):
        self.NWD = NWD(a, b)
        result = self.NWD(121, 114)
        expected = 1
        self.assertEqual(result, expected)


unittest.main(argv=[''], verbosity=2, exit=False)

