import re
#remove all special (non-alphanumeric) characters from a string.

def characters(s):
    return re.sub(r'[^a-zA-Z0-9]', '',)



