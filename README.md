
You can use the following commands to set up a virtual environment and install the necessary packages:

```sh
# Create a virtual environment (optional but recommended)
python -m venv venv

# Activate the virtual environment
# On Windows (Command Prompt)
venv\Scripts\activate
# On Windows (PowerShell)
venv\Scripts\Activate.ps1
# On macOS/Linux
source venv/bin/activate

# Install dependencies from requirements.txt
pip install -r requirements.txt
```

To exit (deactivate) the virtual environment, simply run:

```sh
deactivate
```


# Contents of each file

![ソースコードサイズ](https://img.shields.io/github/languages/code-size/yakinoki/test_codes)

## [math/calculation.py](https://github.com/yakinoki/test_codes/blob/develop/python/math/calculation.py)

Call the Gauss_Jordan function from Gauss_Jordan.py in the src folder to solve the simultaneous equations.

<br>

## math/geodesic.py

Given the coordinates of two points on a sphere of origin center and radius r, find the length of the shortest geodesic between them.

<br>

## math/prime_numbers.py

A code to check that when the interval from n to n^2 is divided by an interval of length n, there is a prime number in each interval.

This code was used for verification purposes when writing the following article.

https://www.chart.co.jp/subject/sugaku/suken_tsushin/91/91-5.pdf

<br>

## math/square_numbers.py

Code for experimenting to see if the product of five consecutive integers can be a square number.

This code was used for verification purposes when writing the following article.

https://www.chart.co.jp/subject/sugaku/suken_tsushin/94/94-11.pdf

This conjecture was later proven.

https://mathlog.info/articles/5qPoXSlvkzpEFBrg1nbb

<br>

## others/sql_lite.py

CURSOR Practice.

<br>

## others/star_sun_moon.py

Practice for creating rock-paper-scissors games.
