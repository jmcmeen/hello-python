import hashlib

def md5hash(input_text):
    return hashlib.md5(input_text.encode()).hexdigest()
    