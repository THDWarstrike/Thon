import math
from fractions import Fraction

print(Fraction(10, 100).limit_denominator(100))
print(Fraction(0.5).limit_denominator(2))
print(Fraction(50, 10).denominator) 