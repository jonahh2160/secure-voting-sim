from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

class Voter:
    def __init__(self, name):
        self.name = name
        self.key = RSA.generate(2048)
        self.public_key = self.key.publickey()

    def sign_vote(self, vote_data):
        h = SHA256.new(vote_data.encode())
        signature = pkcs1_15.new(self.key).sign(h)
        return signature