import json


def customer():
    customer_name = input("Enter customer name: ")
    customer_filename = "accounts/" + customer_name + ".json"
    money_input = int(input("Enter amount of money in account: "))

    customer_dict = {
        "name": customer_name,
        "money": money_input
    }

    add_to_json = json.dumps(customer_dict, indent=4)

    with open(customer_filename, "w") as f:
        f.write(add_to_json)


if __name__ == "__main__":
    customer()
