# gcd function
def gcd(m, n):
    while m % n != 0:
        old_m = m
        old_n = n
        m = old_n
        n = old_m % old_n
    return n

# Fraction class
# Implements: addition and equality
# To do: multiplication, division, subtraction and comparison operators (< , >)
class Fraction:
    def __init__(self, top, bottom):
        if (isinstance(top, int) and isinstance(bottom, int)):
            if (top > 0 and bottom < 0 ) or (top < 0 and bottom < 0):
                top = 0 - top
                bottom = 0 - bottom
            common = gcd(top, bottom)
            self.num = top//common
            self.den = bottom//common
        else:
            raise ValueError("Please make sure the parameters are integer !")

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __repr__(self):
        return "Fraction("+str(self.num)+","+str(self.den)+")"

    def show(self):
        print(self.num, "/", self.den)

    def __add__(self, other_fraction):
        new_num = self.num * other_fraction.den + \
                  self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        return Fraction(new_num , new_den)

    def __eq__(self, other):
        first_num = self.num * other.den
        second_num = other.num * self.den
        return first_num == second_num

    def __gt__(self, other):
        first_num = self.num * other.den
        second_num = other.num * self.den
        return first_num > second_num

    def __ge__(self, other):
        first_num = self.num * other.den
        second_num = other.num * self.den
        return first_num >= second_num

    def __lt__(self, other):
        first_num = self.num * other.den
        second_num = other.num * self.den
        return first_num < second_num

    def __le__(self, other):
        first_num = self.num * other.den
        second_num = other.num * self.den
        return first_num <= second_num

    def __ne__(self, other):
        first_num = self.num * other.den
        second_num = other.num * self.den
        return first_num != second_num

    def get_num(self):
        return self.num

    def get_den(self):
        return self.den

    def __sub__(self, other):
        new_num = self.num * other.den - self.den * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __mul__(self, other):
        new_num=self.num * other.num
        new_den=self.den * other.den
        return Fraction(new_num, new_den)

    def __truediv__(self, other):
        new_num = self.num * other.den
        new_den = self.den * other.num
        return Fraction(new_num, new_den)

    def __radd__(self, other):
        return Fraction(self.num + other * self.den, self.den)

    def __iadd__(self, other):
        self.num = self.num * other.den + \
                self.den * other.num
        self.den = self.den * other.den
        return self

(1 + Fraction(-1, -2))

x = Fraction(-1, 2)
y = Fraction(-3, 5)

x += y
repr(x)
print(x)

(Fraction(1, -2) + Fraction(3, 0.5)).show()
