import string
import itertools


def pw_guess(len_pw: int) -> object:
    all_char = "".join(
        [
            string.ascii_letters,
            str(string.punctuation.replace(">", "")).replace("<", ""),
            "0123456789",
        ]
    )

    res = itertools.permutations(all_char, len_pw)
    for guess in res:
        yield guess


def password(len_pw: int):

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    number = "0123456789"
    punc = string.punctuation.replace(">", "").replace("<", "")

    guess_generator = pw_guess(len_pw)

    for i in guess_generator:
        k = (
            set(i).intersection(lower)
            and set(i).intersection(upper)
            and set(i).intersection(number)
            and set(i).intersection(punc)
        )
        if bool(k):
            yield "".join(i)


if __name__ == "__main__":
    length_pw = int(input("password length ").strip())
    new_password = password(length_pw)
    print(next(new_password))
