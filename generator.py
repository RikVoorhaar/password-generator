# %%
from typing import List
from getpass import getpass
import argparse

SYMBOLS = "!@#$%^&*()_+{};:',.<>?/\|`~"


def _generate_hash(master_pass: str, key: str) -> int:
    import hashlib

    m = hashlib.sha256()
    m.update(master_pass.encode())
    m.update(key.encode())

    return int(m.hexdigest(), 16)


def _load_words() -> List[str]:
    words = []
    with open("wordlist.txt") as word_list:
        words = word_list.read()[:-1].split("\n")
    return words


def generate_password(master_pass: str, key: str, target_len: int = 20) -> str:
    words = _load_words()
    hash_int = _generate_hash(master_pass, key)

    password = ""
    while len(password) < target_len - 2:
        hash_int, index = divmod(hash_int, len(words))
        new_word = words[index]
        new_word = new_word[0].upper() + new_word[1:]
        password += new_word

    hash_int, index = divmod(hash_int, 10)
    password += str(index)
    hash_int, index = divmod(hash_int, len(SYMBOLS))
    password += SYMBOLS[index]
    return password


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("key", help="Key identifying this particular password.")
    parser.add_argument(
        "-l",
        "--length",
        help="Target length of the password",
        default=20,
        type=int,
    )
    args = parser.parse_args()

    master_pass = getpass("Master password:")

    password = generate_password(master_pass, args.key, args.length)
    print(password)


if __name__ == "__main__":
    main()
