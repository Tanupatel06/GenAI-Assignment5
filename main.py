import math_utils
from math_utils import square

import string_utils

import shop_package.discount as disc
from shop_package.billing import calculate_total

from shop_package import flat_discount, apply_tax

# Task 1: Testing math_utils
print("Addition:", math_utils.add(10, 5))
print("Subtraction:", math_utils.sub(10, 5))
print("Square:", square(4))

# Task 2: Testing string_utils
print("Capitalized:", string_utils.capitalize_words("hello python world"))
print("Reversed:", string_utils.reverse_string("python"))
print("Word Count:", string_utils.word_count("hello python world"))

# Task 3 and 4: Testing shop_package
print("Percentage Discount:", disc.apply_discount(1000, 10))
print("Flat Discount:", disc.flat_discount(1000))
print("Total Bill:", calculate_total([100, 200, 300]))
print("Bill After Tax:", apply_tax(600))