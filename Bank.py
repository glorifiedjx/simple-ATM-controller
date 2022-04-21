class Bank:
    def __init__(self):
        self.data = {}

    def add_account(self, card_no, acc, amt):
        if card_no in self.data:
            self.data[card_no]["account"][acc] = amt
        else:
            return False, "The card number is wrong"


    def is_account(self, card_no, acc):
        if acc not in self.data[card_no]["account"]:
            return False
        return True

    def update_account_amt(self, card_no, acc, amt):
        if self.data[card_no]["account"][acc] in self.data[card_no]["account"]:
            self.data[card_no]["account"][acc] = amt
        else:
            self.add_account(card_no, acc, amt)

    def add_card(self, card_no, pin,acc, amt):
        self.data[card_no] = {"pin" : pin, "account" : {acc : amt}}

    def check_card(self, card_no):
        if card_no in self.data.keys():
            return True
        else:
            return False

    def check_pin(self, card_no, entered_pin):
        if card_no in self.data and self.data[card_no]["pin"] == entered_pin:
            return self.data[card_no]["account"]
        else:
            return None


    # def __repr__(self):
    #     return f"Bank('{self.data}')"