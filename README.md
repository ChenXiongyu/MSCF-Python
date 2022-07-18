# MSCF Python Programming Basics 2022

## Homework 1

I will just use quote mark # since I am using an IDE.

### 1. Fib Function

* Integer type of data has no upper limit in Python
* Pay attention to the robustness of the program.
* I use try and except to cope with the robustness problem.

### 2. Operators

* % can deal with floats.

### 3. Sum of Integers

* I use the sum formula to avoid loop.

### 4. Type Conversion

* int and float can cause errors when input type is str or None.
* str and bool are robust in some way.

### 5. IDE choice

* VSCode > Pycharm > Spyder > IDLE

## Homework 2

Maybe add some try except section to improve robustness of the program.

### 1. Formatted Output, File Input, and lists

#### b. Simple Statistics on a list

* In the format string '{:8.2f}', 8 always stands for the total length of the string, rather than the length of integral part.

### 2. list, tuple, set, and dict

#### c. subscript notation

* Watch the assignment order!

#### n. insert

* Pay attention to the arguments in insert function.

#### o. tuple

* Print tuple (4), only showing 4.

#### r. set

* The way to create an empty set is set().

## Homework 3

### 2. Collection Construction and Comprehension

#### d. tuple & sort

* I use list type of data to sort, and then convert it into tuple.

#### h. multiple assignment

* dict.keys(), dict.values()

### 3. Commodity Futures and Option Contracts

* Some hard codes.
* Add some annotations.

## Homework 4

### 1. Function Definitions and Recursion

#### c. get recursion limit

* It seems like in Jupyter Book, the recursion number is initially set to 3000, and I cannot enlarge the limit using set recursion limit.
* In the Python Terminal, it is 1000 in Windows 10 system, and it can be enlarged to at least 2000.
* How to present scientific counting method for such a large integer?
  Large integers cannot be converted to floats, so I used decimal module to deal with it.

#### h. nth prime number

* Call the previous first n prime numbers function.

### 2. NumPy

#### i. data type

* dtype or type() -- both work, but the result a little different for a ndarray.

#### p. square of matrix

* It is not elementwise.

#### q. determinants

* Some important matrix attribute functions are in linalg module in numpy.

### Python for Data Analysis

* Output can be different, int32 against int64 for example.
