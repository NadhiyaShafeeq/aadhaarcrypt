from Crypto.Hash import SHA256
from Crypto.Cipher import AES

class Card:
    def __init__(self, details):
        self.details = details
        self.key = None

    def generate_token(key):
        name = details["name"]
