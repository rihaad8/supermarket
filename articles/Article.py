class Article(object):
    """docstring for Article."""
    id = 1
    name = "Monster Energy"
    price = 28.7

    def __init__(self, arg):
        super(Article, self).__init__()
        self.arg = arg
    #Getter
    def indentify(self):
        id_string = str(self.id) + " " + str(self.name) + " " + str(self.price) + " " + str(self.arg)
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
    def set_id(self, i):
        self.id = i
