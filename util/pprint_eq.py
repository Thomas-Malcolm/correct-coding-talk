#!/usr/bin/env python

from sympy import init_printing, symbols, sympify, pretty
import re

init_printing(quiet=True)

user_request = input()

nice = sympify(user_request, evaluate=False)
print(pretty(nice, use_unicode=True))
