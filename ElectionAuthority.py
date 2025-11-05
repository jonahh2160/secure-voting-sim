from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import json

class ElectionAuthority:
    def __init__(self):
        self.key = RSA.generate(2048)
        self.public_key = self.key.publickey()
        self.votes = []

    def encrypt_vote(self, vote_data):
        cipher = PKCS1_OAEP.new(self.public_key)
        return cipher.encrypt(vote_data.encode())

    def decrypt_vote(self, encrypted_vote):
        cipher = PKCS1_OAEP.new(self.key)
        return cipher.decrypt(encrypted_vote).decode()

    def verify_vote(self, voter_pub_key, vote_data, signature):
        h = SHA256.new(vote_data.encode())
        try:
            pkcs1_15.new(voter_pub_key).verify(h, signature)
            return True
        except (ValueError, TypeError):
            return False

    def cast_vote(self, voter, vote_choice):
        vote_data = json.dumps({"voter": voter.name, "vote": vote_choice})
        signature = voter.sign_vote(vote_data)
        encrypted_vote = self.encrypt_vote(vote_data)
        self.votes.append((encrypted_vote, voter.public_key, signature))

    def tally_votes(self):
        results = {}
        for encrypted_vote, pub_key, signature in self.votes:
            vote_data = self.decrypt_vote(encrypted_vote)
            if self.verify_vote(pub_key, vote_data, signature):
                vote = json.loads(vote_data)["vote"]
                results[vote] = results.get(vote, 0) + 1
        return results
