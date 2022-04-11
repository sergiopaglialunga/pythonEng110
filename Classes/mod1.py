# Create an input for money, type in a number, and make sure the format function transforms it into a money format e.g. 10.22

class Bank():
    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return f"Your bank balance is: {self.amount}"

    def __format__(self, format_spec):
        if format_spec == "uk":
            return f"Your bank balance is: £{round(self.amount, 2)}"
        else:
            return self.__str__()

user = Bank(5085.12335)

print(f"{user:uk}")

print(f"{user}")
