import customtkinter as ctk


class UserGui:
    def __init__(self, on_submit):
        ctk.set_appearance_mode("System")

        self.root = ctk.CTk()
        self.root.title("Secure Voting Sim")
        self.root.geometry("700x300")

        self.submit_callback = on_submit

        self.create_widgets()

    def create_widgets(self):
        label = ctk.CTkLabel(self.root, text="Please select a candidate.")
        label.pack(pady=20)

        self.radio_var = ctk.StringVar(value="No Vote")

        self.radio_A = ctk.CTkRadioButton(
            self.root, text="Candidate A", value="Candidate A", variable=self.radio_var
        )
        self.radio_A.pack(pady=10)

        self.radio_B = ctk.CTkRadioButton(
            self.root, text="Candidate B", value="Candidate B", variable=self.radio_var
        )
        self.radio_B.pack(pady=10)

        self.submit_button = ctk.CTkButton(
            self.root, text="Submit", command=self.handle_vote
        )
        self.submit_button.pack(pady=10)

        self.loading_label = ctk.CTkLabel(self.root, text="")
        self.loading_label.pack(pady=10)

    def handle_vote(self):
        self.radio_A.configure(state="disabled")
        self.radio_B.configure(state="disabled")
        self.submit_button.configure(state="disabled")
        self.loading_label.configure(text="Tallying votes...")
        self.root.update_idletasks()

        vote = self.radio_var.get()
        self.submit_callback(vote)
        self.loading_label.configure(text="Tallying complete!")
