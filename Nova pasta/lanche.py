class Lanche:

    def __init__(self, id, name, price, description, image):
        self.__id = id
        self.__name = name
        self.__price = price
        self.__description = description
        self.__image = image

    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_price(self):
        return self.__price
    
    def get_description(self):
        return self.__description
    
    def get_image(self):
        return self.__image