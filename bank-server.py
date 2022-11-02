'''
Krav för G
TODO: Du kan lägga till en kund i registret
TODO: Du kan fråga servern om vilka kunder som finns
TODO: Du kan fråga om detaljer för en specifik kund
TODO: Du skriver något enhetstest

"bank-server.py" ska vara server
"bank-client.py" ska vara klient
TODO: Måste göra så att servern exekverar funktioner beroende på input från klient
'''

# customer_dict = {
#     "name": name_input,
#     "money": money_input
# }

# add_customer = json.dumps(customer_dict, indent=4)

# with open(self.accounts_file, "w") as f:
#     f.write(add_customer)

# def view_accounts(self):
#     with open(self.accounts_file, "r") as f:
#         temp = json.load(f)
#         i = 1
#         print("--- Accounts ---")
#         for entry in temp:
#             name = entry["name"]
#             money = entry["money"]
#             print(f"{i}. {name}")
#             print(f"Money: {money}")
#             i = i+1
#             print(" ")


import json
from pprint import pprint


def Choices():
    print("Welcome to the bank, what do you want to do?")
    print("1. Add an account")
    print("2. View all accounts")
    print("3. View specific account info")
    print("4. Exit program")


class Customer:

    def __init__(self):
        # self.id = id
        self.accounts_file = "accounts/accounts.json"
        self.accounts_file_test = "accounts/accounts_test.json"

    def create_account(self):
        name_input = input("Enter customers name: ")
        balance_input = int(input("Enter account balance: "))
        new_acc_dict = {
            "name": name_input,
            "balance": balance_input
        }
        return new_acc_dict

    def write_to_json(self, new_data):
        with open(self.accounts_file_test, 'r+') as accounts_open:
            data = json.load(accounts_open)
            data["accounts"].append(new_data)
            accounts_open.seek(0)
            json.dump(data, accounts_open, indent=4)

    def new_account(self):
        new_acc = self.create_account()
        self.write_to_json(new_data=new_acc)

    # def new_account(self, item):
    #     new_acc = self.create_account()
    #     with open(self.accounts_file_test) as accounts_open:
    #         data = json.load(accounts_open)
    #         data["accounts"][new_acc] = item
    #         self.save_to_json(data, filename=self.accounts_file_test)

    def save_to_json(self, data, filename):
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
            return

    def load_accounts(self):
        with open(self.accounts_file, "r") as f:
            loaded_accounts = json.load(f)
            return loaded_accounts

    def view_accounts(self):
        # works with dict {}, not with list
        with open(self.accounts_file, "r") as f:
            temp = json.load(f)
            account = temp["accounts"]
            print("--- Accounts ---")
            for key, value in account.items():
                print(key, value)

    def view_accounts_list(self):
        with open(self.accounts_file_test, "r") as f:
            temp = json.load(f)
            account = temp["accounts"]
            pprint(account[::-1])

    def view_accounts_list2(self):
        data = json.load(open(self.accounts_file_test, "r"))
        pprint(data)


if __name__ == "__main__":
    bank1 = Customer()

    while True:
        Choices()
        choice = input("\nEnter your choice: ")

        if choice == "1":
            bank1.new_account()
            # add account

        elif choice == "2":
            bank1.view_accounts_list()
            # bank1.view_accounts()
            # view all accounts

        elif choice == "3":
            pass
            # view specific account info

        elif choice == "4":
            break

        elif choice == "5":
            bank1.create_account()

        else:
            print("Error! Please select a valid option!")
