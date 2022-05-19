#!/usr/bin/env python

def squareFib(n: int) -> int:

    x = 0
    i = 0
    y = 1
    k = 0
    while i != n:
        x,y,k = y, x + k + y, k + y + y
        i += 1

    return x


if __name__ == "__main__":

    print("nth Fibonacci number squared:")
    while True:
        n = input("> ")
        print(f"The {n}th Fibonacci number squared is: {squareFib(int(n))}")
        print("again!")