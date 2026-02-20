#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    def add_item(self, title, price, quantity=1):
        # add item "quantity" times
        for _ in range(quantity):
            self.items.append(title)

        # update total and store transaction amount
        transaction_total = price * quantity
        self.total += transaction_total
        self.previous_transactions.append(transaction_total)

    def apply_discount(self):
      if self.discount == 0:
          print("There is no discount to apply.")
          return

      self.total = self.total * (1 - self.discount / 100)

      # print without trailing .0 when it's a whole number
      if self.total == int(self.total):
          total_str = str(int(self.total))
      else:
          total_str = str(self.total)

      print(f"After the discount, the total comes to ${total_str}.")

    def void_last_transaction(self):
        if not self.previous_transactions:
            print("There is no transaction to void.")
            return

        last_transaction = self.previous_transactions.pop()
        self.total -= last_transaction

        if self.total == 0:
            self.total = 0.0