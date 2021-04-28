class User:
    def log(self):
        print(self)

class Customer(User):
    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @name.deleter
    def name(self):
        del self._name

    def update_membership(self, new_membership):
        print("Calculating cost")
        self.membership_type = new_membership

    def __str__(self):
        return self.name + " " + self.membership_type

    def print_all_customers(customers):
        for customer in customers:
            print(customer)

    def __eq__(self, other):
        if self.name == other.name and self.membership_type == other.membership_type:
            return True

        return False

    hash = None

customers = [Customer("Caleb", "Gold"),
             Customer("John", "Silver")]

print(customers[0].name)

customers[0].log