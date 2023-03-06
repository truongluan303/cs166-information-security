import sys

from collections import defaultdict
from typing import Dict


def count_letter_freq(ciphertext: str) -> Dict[str, int]:
    res = defaultdict(lambda: 0)
    for ch in ciphertext:
        res[ch] += 1
    return dict(res)


def get_ciphertext_input() -> str:
    return sys.argv[1].strip() if len(sys.argv) == 2 else input("Enter the cipther text: ").strip()


def main() -> None:
    ciphertext = get_ciphertext_input()


if __name__ == "__main__":
    main()
