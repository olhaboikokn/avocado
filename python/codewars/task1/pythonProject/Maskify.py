# Usually when you buy something, you're asked whether your credit card number,
# phone number or answer to your most secret question is still correct.
# However, since someone could look over your shoulder,
# you don't want that shown on your screen. Instead, we mask it.
# Your task is to write a function maskify, which changes all but the last four characters into '#'.

def maskify(cc):
    length = len(cc)
    if len(cc) <= 4:
        return cc
    masked_part = "#" * (length - 4)
    visible_part = cc[-4:]
    return masked_part + visible_part

if __name__ == "__main__":
    cc1 = "4556364607935616"
    cc2 = '54'
    print(maskify(cc1))