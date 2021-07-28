class Database:
    list_products = []
    def __init__(self):
        f = open(f'./products.txt','r')
        for line in f.readlines():
            id, name, price = line.split(',')
            self.list_products.append({
                'id': int(id),
                'name': name,
                'price': float(price.replace('\n',''))
            })




if __name__ == '__main__':
    db = Database()
    print(db.list_products)