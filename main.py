import random
import threading

from ElectionAuthority import ElectionAuthority
from gui import UserGui
from Voter import Voter


def submit_user_vote(vote_choice, authority, thread, gui):
    voter = Voter("User")
    authority.cast_vote(voter, vote_choice)

    thread.join()

    results = authority.tally_votes()
    winner = max(results)
    winner_votes = max(results.values())
    loser = min(results)
    loser_votes = min(results.values())

    gui.message_label.configure(
        text=f"Tallying complete!\n\nWinner: {winner} with {winner_votes} votes\nLoser: {loser} with {loser_votes} votes"
    )

    print("Demo tally:", results)
    print("Stored encrypted votes:", len(authority.votes))

    # Show a decrypted example (for demonstration only)
    if authority.votes:
        encrypted, pub_key, sig = authority.votes[0]
        print("Decrypted first voter:", authority.decrypt_vote(encrypted))


def submit_random_votes(authority):
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


def main():
    authority = ElectionAuthority()

    thread = threading.Thread(
        target=submit_random_votes, args=(authority,), daemon=True
    )
    thread.start()

    gui = UserGui(on_submit=lambda vote: submit_user_vote(vote, authority, thread, gui))
    gui.root.mainloop()


if __name__ == "__main__":
    main()
