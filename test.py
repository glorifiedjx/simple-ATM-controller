import sys
from Bank import Bank
from Controller import Controller


def check_PIN(s):
    if atm.check_pin(s):
        print("Right PIN")
        print("Show Accounts: ", atm.auth_accounts_list())
    else:
        print("Wrong PIN")
        print("Show Accounts: ", atm.auth_accounts_list())



if __name__ == "__main__":

    test_bank = Bank()
    test_bank.add_card(439967, "0003", "checking", 1000)
    test_bank.add_card(95555, "7321", "checking", 20000)
    test_bank.add_account(439967, "saving", 22344)
    print(test_bank)

    ## ATM Controller API Test Begin ###
    print ('\n ## ATM Controller API Test Begin ##')
    atm = Controller(test_bank, 1000000)
    print(atm.insert_card(439967))
    print(atm.is_valid_card)

    check_PIN("1234")
    atm.select_account="checking"
    print(atm.select_account)

    check_PIN("0003")
    atm.select_account="checkings"
    print(atm.select_account)

    atm.select_account="checking"
    print(atm.select_account)

    print("balance: ", str(atm.balance))

    atm.cash_bin = 40000
    print("Cashbin: ",atm.cash_bin)

    atm.account_actions("Check Balance",0)
    atm.account_actions("Withdraw", 400)
    print("balance: ", str(atm.balance))
    atm.account_actions("Deposit", 400)
    print("balance: ", str(atm.balance))
    ## ATM Controller API Test Ends ###
    print ('## ATM Controller API Test Ends ##\n')


    action_list1 = [("Check Balance",0), ("Withdraw", 40), ("Withdraw", 1000), ("Deposit", 100)]
    print()
    ## Test Normal (valid)
    print ('\n Normal Test ')
    print (atm(95555, "7321", "checking", action_list1))

    ##Test overdraft
    print ('\n Overdraft test ')
    print (atm(439967, "0003", "checking", action_list1))

    ##Cashbin not enough
    atm.cash_bin = 100
    print ('\n Cashbin not enough ')
    print (atm(439967, "0003", "checking", action_list1))

    ## Test incorrect PIN number
    print ('\n Incorrect PIN ')
    print (atm(95555, 1234, "checking", action_list1))




