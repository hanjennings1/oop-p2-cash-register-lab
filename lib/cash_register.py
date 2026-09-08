#!/usr/bin/env python3

# Create the Class:
class CashRegister:
  def __init__ (self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.previous_transactions = []

  # Define the Discount Property
  @property
  def discount(self):
    # getter: lets us access register.discount like a normal attribute
    return self._discount

  @discount.setter
  def discount(self, discount):
      # setter: runs validation whenever self.discount = ... is called
      if type(discount) is int and 0 <= discount <= 100:
          self._discount = discount
      else:
          print("Not valid discount")

  # add_item function
  def add_item(self, item, price, quantity=1):
      # add this item's total cost to the running total
      self.total += price * quantity

      # add the item to the items list once per quantity
      for i in range(quantity):
          self.items.append(item)

      # record this transaction so it can be voided/discounted later
      transaction = {"item": item, "price": price, "quantity": quantity}
      self.previous_transactions.append(transaction)

  # apply_discount
  def apply_discount(self):
    if self.discount == 0:
        # if no discount, print this error message:
        print("There is no discount to apply.")
    else:
       # reduce total by the discount %
       self.total = self.total * (1 - self.discount / 100)
       # print the success message for user - formatted w/o decimals
       print(f"After the discount, the total comes to ${self.total:.0f}.")
       # remove the most recent transaction since it's now been discounted
       self.previous_transactions.pop()

  # void_last_transaction
  def void_last_transaction(self):
     if not self.previous_transactions:
        print("There is no transaction to void.")
     else: 
        # grab the most recent transaction
        last_transaction = self.previous_transactions.pop()
        item = last_transaction["item"]
        price = last_transaction["price"]
        quantity = last_transaction["quantity"]

        # subtract the full cost of that transaction from total
        self.total -= price * quantity

        # remove each occurrence of the item from items (list.remove(item) only removed the first occurence)
        for i in range(quantity):
            self.items.remove(item)