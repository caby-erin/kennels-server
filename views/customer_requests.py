CUSTOMERS = [
  {
    "id": 1,
    "name": "Sir Isaac Newton"
  },
  {
    "id": 2,
    "name": "Monty Mole"
  }
]

def get_single_customer(id):
    requested_customer = None
    for customer in CUSTOMERS:
        if customer["id"] == id:
            requested_customer = customer
    return requested_customer
def get_all_customers():
    return CUSTOMERS
