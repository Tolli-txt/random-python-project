'''
Krav för G
TODO: Du kan lägga till en kund i registret - Klar
TODO: Du kan fråga servern om vilka kunder som finns - Klar
TODO: Du kan fråga om detaljer för en specifik kund - Klar
TODO: Du skriver något enhetstest - Försök skriva så många som möjligt,
försök dela upp funktioner om det går?

"bank-server.py" ska vara server
"bank-client.py" ska vara klient
Måste göra så att servern exekverar funktioner 
beroende på input från klient
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

# def new_account(self, item):
#     new_acc = self.create_account()
#     with open(self.accounts_file_test) as accounts_open:
#         data = json.load(accounts_open)
#         data["accounts"][new_acc] = item
#         self.save_to_json(data, filename=self.accounts_file_test)

# def write_to_json_dict(self, new_data):
#     with open(self.accounts_file, "r+") as accounts_open:
#         data = json.load(accounts_open)
#         data["accounts"].update(new_data)
#         accounts_open.seek(0)
#         json.dump(data, accounts_open, indent=4)

# def add_to_json_dict(self, item):
#     with open(self.accounts_file) as accounts:
#         data = json.load(accounts)
#         data["accounts"][self.create_account()] = item
#         self.save_to_json(data, filename=self.accounts_file)

# def number_of_keys(self):
#     accounts_dict = self.load_accounts()
#     count = 0
#     for key, value in accounts_dict["account"].items():
#         count += 1
#     return count

# def view_accounts_list4(self):
#         with open(self.accounts_file_test) as f:
#             data = json.loads(f.read())
#             print(data['accounts'][0::-1])

# def view_num_of_accounts(self):
#     with open(self.accounts_file_test) as accounts_list:
#         data = json.load(accounts_list)
#         print("Type:", type(data))
#         print("\nAccounts", data["accounts"])

# def view_accounts_list2(self):
#     data = json.load(open(self.accounts_file_test, "r"))
#     pprint(data)

# def view_accounts_list(self):
#     with open(self.accounts_file_test, "r") as f:
#         temp = json.load(f)
#         account = temp["accounts"]
#         pprint(account[::-1])

# def view_specific_account(self):
#     with open(self.accounts_file_test, "r") as f:
#         data = json.load(f)
#         accounts = data["accounts"]
#         i = 1
#         for info in accounts:
#             print(f"Customer #{i}")
#             print("Name:", info["name"])
#             print("Balance:", info["balance"])
#             i = i+1
#             print(" ")
#             return


import json
from pprint import pprint


def Choices():
    print("\nWelcome to the bank, what do you want to do?")
    print("1. Add an account")
    print("2. View all accounts")
    print("3. View specific account info")
    print("4. Exit program")


class Customer:

    def __init__(self):
        #self.items = self.load_accounts()
        self.accounts_file = "accounts/accounts.json"
        self.accounts_file_test = "accounts/accounts_test.json"

    def write_to_json(self, new_data):
        with open(self.accounts_file_test, 'r+') as accounts_open:
            data = json.load(accounts_open)
            data["accounts"].append(new_data)
            accounts_open.seek(0)
            json.dump(data, accounts_open, indent=4)

    def save_to_json(self, data, filename):
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
            return

    def create_account(self):
        name_input = input("Enter customers name: ")
        balance_input = int(input("Enter account balance: "))
        new_acc_dict = {
            "name": name_input,
            "balance": balance_input
        }
        return new_acc_dict

    def new_account(self):
        new_acc = self.create_account()
        self.write_to_json(new_data=new_acc)

    def load_accounts(self, filename):
        with open(filename, "r") as accounts_loaded:
            items = json.load(accounts_loaded)
            return items

    def view_accounts(self):
        with open(self.accounts_file, "r") as f:
            temp = json.load(f)
            account = temp["accounts"]
            print("--- Accounts ---")
            for key, value in account.items():
                print(key, value)

    def view_accounts_list3(self):
        with open(self.accounts_file_test) as accounts:
            data = json.load(accounts)
            i = 1
            print("\n--- Accounts at the bank ---")
            for info in data["accounts"]:
                print(f"Customer #{i}")
                print("Name:", info["name"])
                #print("Balance:", info["balance"])
                i = i+1
                print("")

    def view_specific_account(self):
        choice = int(input("Who do you want to inspect? \n"))
        with open(self.accounts_file_test, "r") as f:
            data = json.load(f)
            accounts = data["accounts"][choice - 1]
            print(accounts)

    def view_specific_account_2(self, item):
        with open(self.accounts_file_test, "r") as f:
            data = json.load(f)
            accounts = data["accounts"][item - 1]
            return accounts

    def print_spec_acc_info(self):
        specific_acc = self.view_specific_account_2()
        print(specific_acc)


if __name__ == "__main__":
    bank1 = Customer()

    while True:
        Choices()
        choice = input("\nEnter your choice: ")

        if choice == "1":
            bank1.new_account()  # This works
            # add account

        elif choice == "2":
            bank1.view_accounts_list3()
            # bank1.view_accounts_list()
            # bank1.view_accounts()
            # view all accounts

        elif choice == "3":
            choice = int(input("Who do you want to inspect? "))
            print(bank1.view_specific_account_2(item=choice))

            # bank1.view_specific_account() # This works
            # view specific account info

        elif choice == "4":
            break

        elif choice == "5":
            bank1.create_account()

        else:
            print("Error! Please select a valid option!")
