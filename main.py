from Voter import Voter
from ElectionAuthority import ElectionAuthority

def main():
    authority = ElectionAuthority()

    voters = [Voter("Alice"), Voter("Bob"), Voter("Carol")]
    choices = ["Candidate A", "Candidate B", "Candidate A"]

    for v, c in zip(voters, choices):
        authority.cast_vote(v, c)

    results = authority.tally_votes()
    print("Demo tally:", results)
    print("Stored encrypted votes:", len(authority.votes))

    # Show a decrypted example (for demonstration only)
    if authority.votes:
        encrypted, pub_key, sig = authority.votes[0]
        print("Decrypted first vote:", authority.decrypt_vote(encrypted))


if __name__ == "__main__":
    main()
