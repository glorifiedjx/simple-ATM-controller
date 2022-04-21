from Bank import Bank

class Controller:

    def __init__(self, bank, cash):
        self.Bank = bank
        self._cash_bin = cash
        self._accounts = None
        self._is_valid_card = False
        self._card_no = None
        self._selected_acc = None


    @property
    def cash_bin(self):
        return self._cash_bin


    @cash_bin.setter
    def cash_bin(self, cash):
        self._cash_bin = cash

    @property
    def card_no(self):
        if self._is_valid_card:
            return self._card_no
        else:
            return None

    def insert_card(self, card_no):
        '''
        Scan the inserted card and check if the card number is valid
        '''
        self._is_valid_card = self.Bank.check_card(card_no)
        if self._is_valid_card:
            self._card_no = card_no
        return self._is_valid_card


    @property
    def is_valid_card(self):
        return self._is_valid_card


    def check_pin(self, pin):
        '''
        check if PIN is valid
        '''
        if not self._is_valid_card:
           return False

        self._accounts = self.Bank.check_pin(self._card_no, pin)
        if not self._accounts:
            return False
        else:
            return True

    def auth_accounts_list(self):
        '''
        Return all accounts so that a client can choose one
        '''
        if self._is_valid_card and self._accounts:
            list = []
            for a in self._accounts.keys():
                list.append(a)
            return list


    @property
    def select_account(self):
        if self._is_valid_card and self._accounts:
            return self._selected_acc


    @select_account.setter
    def select_account(self, acc):
        if self._is_valid_card and self._accounts and acc in self._accounts:
            self._selected_acc = acc
        else:
            self._selected_acc = None


    @property
    def balance(self):
        if self._is_valid_card and self._accounts:
            return self._accounts[self._selected_acc]



    def account_actions(self, action, amt=0):
        '''
        customer action to :
        1. Check balance
        2. Withdraw
        3. Deposit
        '''
        if self._selected_acc:
            acc = self._selected_acc
        else: return False

        if action == "Check Balance":
            return self._accounts[acc], 1
        elif action == "Withdraw":
            if self.cash_bin < amt:     # cash_bin not enough money
                return self._accounts[acc], -999
            elif self._accounts[acc] < amt:
                return self._accounts[acc], -500
            else:
                self.cash_bin -= amt
                self._accounts[acc] -= amt
                self.Bank.update_account_amt(self._card_no, acc, self._accounts[acc])
                return self._accounts[acc], 1

        elif action == "Deposit":
            self.cash_bin += amt
            self._accounts[acc] += amt
            self.Bank.update_account_amt(self._card_no, acc, self._accounts[acc])
            return self._accounts[acc], 1
        else:
            return self._accounts[acc], 2


    def __call__(self, card_no, pin, acc, action_list):
        '''
        Run the ATM system
        '''
        customer_leave = False
        while not customer_leave:

            valid_c = self.insert_card(card_no)
            if not valid_c:
                return "Not a valid card"

            valid_p = self.check_pin(pin)
            if not valid_p:
                return "Not a valid PIN"

            self.select_account = acc
            if not self.select_account:
                return "Not a valid account."

            for action in action_list:
                if action[0] == "Leave":
                    break
                balance, msg = self.account_actions(action[0], action[1])
                # print("balance", balance, "msg: ", msg )
                if msg == 2:
                    return "Invalid action"
            return "Actions completed. Cash bin now is: " + str(self._cash_bin)


    # def __repr__(self):
    #     return f"Controller('{self.cash_bin}', '{self._accounts}')"