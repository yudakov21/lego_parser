from bs4 import BeautifulSoup

class LegoParser:
    def __init__(self, raw_data):
        self.soup = BeautifulSoup(raw_data, 'html.parser')

    @staticmethod
    def get_toys_info(toy_data):
        t_data = {
            'age': None,
            'pieces': None,
            'rating': None
        }

        for d in toy_data:
            if '+' in d:
                t_data['age'] = d
            elif '.' in d:
                t_data['rating'] = d
            else:
                t_data['pieces'] = d

        return t_data
    
    @staticmethod
    def get_price(toy):
        try:
            price_span = toy.find('span', {'data-test': 'product-leaf-price'})
            t_price = price_span.text.strip() if price_span else None

            discount_span = toy.find('span', {'data-test': 'product-leaf-discounted-price'})
            t_discount = discount_span.text.strip() if discount_span else None

            return t_price, t_discount
        except AttributeError:
            return None, None
        
    @staticmethod    
    def get_description(toy):
        try:
            description = toy.find('span', {'data-test': 'product-leaf-price-description'})
            t_description = description.text if description else None
            return t_description
        except AttributeError:
            print("Error при извлечении")
            return None

    def parse_toys(self):
        toys = []
        toy_elements = self.soup.find_all('li', {'data-test': 'product-item'})

        for toy in toy_elements:
            name = toy.find('h3').text.strip() if toy.find('h3') else "Nothing"

            attr_row = toy.find('div', {'data-test': 'product-leaf-attributes-row'})
            if attr_row:
                toy_data = [item.text.strip() for item in attr_row.find_all('span')]
                toy_data = self.get_toys_info(toy_data=toy_data)
            else:
                toy_data = {'age': None, 'pieces': None, 'rating': None, }

            price, discount = self.get_price(toy)
            description = self.get_description(toy)

            toys.append({
                'name': name,
                'age': toy_data['age'],
                'pieces': toy_data['pieces'],
                'rating': toy_data['rating'],
                'price': price,
                'discount': discount,
                'description': description
            })
        return toys