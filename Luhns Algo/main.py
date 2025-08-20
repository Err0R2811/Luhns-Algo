def luhn_check(card_no: str) -> bool:
    if card_no is None:
        return False

    s = card_no.replace(" ", "").replace("-", "")
    if not s.isdigit():
        return False

    total = 0
    rev = s[::-1]
    for i, ch in enumerate(rev):
        d = int(ch)
        if i % 2 == 1: 
            d *= 2
            if d > 9:
                d -= 9
        total += d
    return total % 10 == 0


def check_algo(card_no: str) -> bool:
    return luhn_check(card_no)


if __name__ == "__main__":
    card_no = input("Enter card number: ").strip()
    is_valid = luhn_check(card_no)
    print("Valid  number" if is_valid else "Invalid  number")