class Article(object):
    """docstring for Article."""

    name = " "
    price = -1
    id = -1
    #Constructor
    def __init__(self, id, name, price):
        super(Article, self).__init__()
        self.id = id
        self.name = name
        self.price = price

    #Getter
    def indentify(self):
        id_string = str(self.id) + " " + str(self.name) + " " + str(self.price)
        return id_string

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_args(self):
        return self.args
    #Setter
    def set_id(self, intVal):
        self.id = intVal

    def set_name(self, strVal):
        self.name = strVal

    def set_price(self, doubleVal):
        self.price = doubleVal

    #other Methods
    def toList(self):
        attrList = [self.id, self.name, self.price]
        return attrList
