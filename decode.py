def decode(s):
    """Decode a string."""
    new_string = ""
    for num in range(len(s)):
        if s[num].isdigit():
            skip = int(s[num])
            keep = num + skip + 1
            new_string += s[keep]
    print new_string


decode("0h1ae2bcy")