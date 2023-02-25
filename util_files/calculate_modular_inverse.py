#!/usr/bin/env python3

import sys

def get_mod_inverse(m: int, n: int) -> int:
    for x in range(1, n):
        if (((m % n) * (x % n)) % n == 1):
            return x
    return -1

def main() -> None:
    if len(sys.argv) != 3:
        print("Usage: calculate_modular_inverse.py m n")
        return
    m, n  = int(sys.argv[1]), int(sys.argv[2])
    print(get_mod_inverse(m, n))

if __name__ == "__main__":
    main()

