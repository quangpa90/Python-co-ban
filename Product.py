from database import Database

class Products:
    def __init__(self, id, name, price):
        self.__id = id
        self.__name = name
        self.__price = price
    def get_id(self):
        return self.__id
    def set_id(self, id):
        self.__id = id
    def get_name(self):
        return self.__name
    def get_price(self):
        return self.__price
    def show(self):
        print('Product: {} {} {}'.format(self.__id, self.__name, self.__price))

class Shop:
    def __init__(self, name, list_products):
        self.name = name
        self.list_products = list_products

    def show(self):
        for item in self.list_products:
            print("----------------")
            print(f"Amount: {item['amount']} Sold: {item['amount_sold']}")
            item["product"].show()

            
if __name__ == '__main__':
    db = Database()
    list_product_obj = []
    for product in db.list_products:
        # print(product['id'], product['name'], product['price'])
        obj = Products(product['id'], product['name'], product['price'])
        list_product_obj.append({
            "amount": 10,
            "product": obj,
            "amount_sold":0
        })
    print(list_product_obj)
      

    nhan_shop = Shop("Nhan Shop", list_product_obj)
    nhan_shop.show()


