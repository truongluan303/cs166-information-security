#!/usr/bin/env python3

import sys

from typing import List


def calc_gk(sik: List[int], m: int , n: int) -> List[int]:
    return [(x * m) % n for x in sik]


def encrypt_message(ptext: str, gk: List[int], n: int) -> int:
    result = 0
    for i in range(len(ptext)):
        result += int(gk[i]) if ptext[i] == "1" else 0
    return result % n


def main() -> None:
    sik = [int(x) for x in input("SIK: ").replace(",", " ").split() if x]
    m = int(input("M: ").strip())
    n = int(input("N: ").strip())
    msg = input("[optional] Message to encrypt: ").strip()

    print("=============================")

    gk = calc_gk(sik, m, n)
    print("GK:", gk)

    encrypted_msg = encrypt_message(msg, gk, n)
    print("Encrypted Message [decimal]:", encrypted_msg)


if __name__ == "__main__":
    main()

