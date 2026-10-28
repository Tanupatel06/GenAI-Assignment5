# Python Modules and Packages Assignment

## 📌 Project Overview

This project demonstrates the creation and use of Python modules and packages. It is part of **GenAI Assignment 5: Importing, Creating Modules & Packages**.

The main objective is to understand how to organize Python code into reusable modules, import functions from different modules, and create a package containing related Python files.

## 🎯 Objectives

* Create Python modules using `.py` files.
* Import complete modules and individual functions.
* Create and use Python packages.
* Understand the purpose of `__init__.py`.
* Perform mathematical and string operations.
* Implement basic discount and billing calculations.
* Test all functions using `main.py`.

## 📁 Project Structure

```text
modules_assignment/
│
├── main.py
├── math_utils.py
├── string_utils.py
│
└── shop_package/
    ├── __init__.py
    ├── discount.py
    └── billing.py
```

## 🧮 Task 1: Create a Simple Module

### File: `math_utils.py`

This module contains three mathematical functions.

**Functions:**

1. `add(a, b)` — Returns the sum of two numbers.
2. `subtract(a, b)` — Returns the difference between two numbers.
3. `square(n)` — Returns the square of a number.

**Example:**

```python
import math_utils
from math_utils import square

print(math_utils.add(10, 5))
print(math_utils.subtract(10, 5))
print(square(4))
```

**Output:**

```text
15
5
16
```

## 🔤 Task 2: Create Another Module

### File: `string_utils.py`

This module contains three string manipulation functions.

**Functions:**

1. `capitalize_words(text)` — Capitalizes the first letter of each word.
2. `reverse_string(text)` — Returns the reversed string.
3. `word_count(text)` — Returns the number of words in a string.

**Example:**

```python
import string_utils

print(string_utils.capitalize_words("hello python world"))
print(string_utils.reverse_string("python"))
print(string_utils.word_count("hello python world"))
```

**Output:**

```text
Hello Python World
nohtyp
3
```

## 🛍️ Task 3: Create a Python Package

### Package: `shop_package`

A package is a folder containing related Python modules.

This package contains three files:

* `__init__.py`
* `discount.py`
* `billing.py`

### File: `shop_package/discount.py`

This module contains discount calculation functions.

**Functions:**

1. `apply_discount(price, percent)` — Calculates the price after applying a percentage discount.
2. `flat_discount(price)` — Subtracts a flat discount of ₹50 from the given price.

**Example:**

```python
import shop_package.discount as disc

print(disc.apply_discount(1000, 10))
print(disc.flat_discount(1000))
```

**Output:**

```text
900.0
950
```

### File: `shop_package/billing.py`

This module contains billing functions.

**Functions:**

1. `calculate_total(prices)` — Returns the sum of all prices.
2. `apply_tax(amount)` — Adds 5% tax to the given amount.

**Example:**

```python
from shop_package.billing import calculate_total, apply_tax

print(calculate_total([100, 200, 300]))
print(apply_tax(600))
```

**Output:**

```text
600
630.0
```

### File: `shop_package/__init__.py`

This file initializes the package and allows selected functions to be imported directly from it.

```python
from .discount import apply_discount, flat_discount
from .billing import calculate_total, apply_tax
```

**Example:**

```python
from shop_package import flat_discount, apply_tax

print(flat_discount(1000))
print(apply_tax(600))
```

## 📥 Task 4: Importing the Package in `main.py`

The `main.py` file imports and tests functions from all modules and the package.

Different import methods used in this project include:

```python
import math_utils
from math_utils import square

import string_utils

import shop_package.discount as disc
from shop_package.billing import calculate_total

from shop_package import flat_discount, apply_tax
```

These statements demonstrate how to import complete modules, individual functions, and modules from a package.

## ▶️ How to Run the Project

Follow these steps to run the project:

1. Open the project folder in Visual Studio Code.
2. Ensure that all Python files are saved in the correct folders.
3. Open the VS Code terminal.
4. Navigate to the folder containing `main.py`.
5. Run the following command:

```bash
python main.py
```

On Windows, you can also try:

```bash
py main.py
```

## 📤 Expected Output

```text
Addition: 15
Subtraction: 5
Square: 16
Capitalized: Hello Python World
Reversed: nohtyp
Word Count: 3
Percentage Discount: 900.0
Flat Discount: 950
Total Bill: 600
Bill After Tax: 630.0
```

## 📚 Concepts Learned

* **Module:** A Python file containing reusable functions and code.
* **Package:** A folder used to organize related Python modules.
* **Importing a module:** Using `import module_name` to access its functions.
* **Importing a function:** Using `from module_name import function_name` to import a specific function.
* **Package initialization:** Using `__init__.py` to initialize a package and optionally expose functions.
* **Code reusability:** Writing functions once and importing them wherever needed.

## ⚙️ Technologies Used

* Python 3
* Visual Studio Code
* GitHub (for project hosting, if used)

No external libraries are required.

## 📌 Assignment Restrictions

This project follows the assignment requirements:

* No object-oriented programming (OOP).
* No exception handling.
* No file input/output operations beyond creating the required Python files.
* Simple function logic.
* Focus only on modules, imports, and packages.

## 👩‍💻 Author

**Tanu Patel**

## 📝 Conclusion

This assignment provides practical experience in creating Python modules, importing functions in different ways, and organizing related code into packages. It demonstrates how modular programming improves code organization, reusability, and maintainability.
