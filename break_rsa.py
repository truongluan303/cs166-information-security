import sys

from typing import Dict, Optional


def find_smallest_d(p, q, e) -> int:
    pass


def find_gcd(a, b) -> int:
    while True:
        temp = a % b
        if temp == 0:
            return b
        a = b
        b = temp


def get_input() -> Optional[Dict[str, int]]:
    if len(sys.argv) == 1:
        return {
            "p": int(input("Enter p: ")),
            "q": int(input("Enter q: ")),
            "e": int(input("Enter e: "))
        }
    elif len(sys.argv) == 4:
        return {var: val for var, val in zip(("p", "q", "e"), sys.argv[1:])}
    else:
        return None


def main() -> None:
    try:
        userinput = get_input()
    except TypeError:
        print("Error! Input is not integer.")
        exit(1)
    if not userinput:
        print("Invalid number of arguments!\n")
        print("Usage: break_rsa.py [p] [q] [e]\n   or: break_rsa.py")
        exit(1)
    
    print(find_smallest_d(**userinput))


if __name__ == "__main__":
    main()
