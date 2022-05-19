#!/usr/bin/env python

from sympy import init_printing, symbols
from sympy import sympify, pretty
from sympy import *

import re

init_printing(quiet=True)

# need to be defined afaict
forall = symbols("∀") # reserve Eta for this
exists = symbols("∃") # reserve Epsilon for this

user_request = input()
request = ""

if "forall" in user_request.lower() or "exists" in user_request.lower():
    
    tmp_request = user_request.replace("Exists", "exists").replace("Forall", "forall")

    request = tmp_request.replace("exists", "Epsilon+")
    request = request.replace("forall", "Eta+")

    request = pretty(sympify(request, evaluate=False), use_unicode=True)

    existMatch = str(pretty(Symbol("Epsilon")))
    forallMatch = str(pretty(Symbol("Eta")))

    tmp_request = request[:]
    if "+ " + existMatch in tmp_request:
        tmp = [x for x in request.split("+ " + existMatch) if x ]

        request = ""
        for t in tmp:
            request += str(exists) + " " + t
    
    tmp_request = request[:]
    if existMatch + " +" in request:
        request.replace(existMatch + " +", str(exists) + " ")

    tmp_request = request[:]
    if "+ " + forallMatch in tmp_request:
        tmp = [x for x in request.split("+ " + forallMatch) if x ]

        request = ""
        for t in tmp:
            request += str(forall) + " " + t
    
    tmp_request = request[:]
    if forallMatch + " +" in request:
        request.replace(forallMatch + " +", str(forall) + " ")

else:
    request = pretty(sympify(user_request), use_unicode=True)

print(request)
