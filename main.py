import random

from ElectionAuthority import ElectionAuthority
from Voter import Voter


def main():
    authority = ElectionAuthority()

    voters = [
        Voter("Alice"),
        Voter("Bob"),
        Voter("Carol"),
        Voter("Daisy"),
        Voter("Ezra"),
        Voter("Finley"),
        Voter("Gavin"),
        Voter("Hannah"),
        Voter("Ivan"),
        Voter("Julia"),
    ]

    for v in voters:
        authority.cast_vote(v, random.choice(["Candidate A", "Candidate B"]))

    results = authority.tally_votes()
    print("Demo tally:", results)
    print("Stored encrypted votes:", len(authority.votes))

    # Show a decrypted example (for demonstration only)
    if authority.votes:
        encrypted, pub_key, sig = authority.votes[0]
        print("Decrypted first vote:", authority.decrypt_vote(encrypted))


if __name__ == "__main__":
    main()
