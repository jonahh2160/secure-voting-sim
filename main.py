import customtkinter as ctk
import Voter
import ElectionAuthority

def main():
    # Setup
    authority = ElectionAuthority()
    alice = Voter("Alice")
    bob = Voter("Bob")

    # Voting
    authority.cast_vote(alice, "Candidate A")
    authority.cast_vote(bob, "Candidate B")

    # Tally
    results = authority.tally_votes()
    print("Election Results:", results)


if __name__ == "__main__":
    main()
