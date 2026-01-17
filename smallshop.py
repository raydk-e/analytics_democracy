class MyShop:

    def __init__(self):
        name =  input("provide shop name: ")
        type = input("provide shop type: ")
        self.name = name
        self.type = type

    def display_detail(self):
        print(f"shop_name - {self.name}")
        print(f"shop_category - {self.type}")
        if self.type == "paan":
            print(f"deals with: paan, chocolate, buscuit, cookies, namkeen, cigarate, water bottle, cake, banana  ")
    def services(self, service_type):
        if service_type == 'b2b':
            print("only sells bettle leafs")
        else:
            print("all items available in the shop are sold")

padana = MyShop()
print(padana.name)
padana.display_detail()
padana.services('b2b')


dhania = MyShop()
dhania.services('b2c')

