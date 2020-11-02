from articles import Article
import csv

class Inventory(object):
    """docstring for Inventory."""

    articleList = []

    def __init__(self):
        super(Inventory, self).__init__()

    def addArticle(self, Article):
        idTaken = False
        for article in self.articleList:
            if(article.id == Article.id):
                idTaken = True
        if(not idTaken):
                self.articleList.append(Article)
        else:
            print("ID [",Article.get_id(),"] is already taken! Please try to add another Article.")

    def saveListToFile(self, fileName):
        with open(fileName, 'w', newline='') as inventoryFile:
            writer = csv.writer(inventoryFile)
            writer.writerow(vars(self.articleList[0]))
            for article in self.articleList:
                writer.writerow(article.toList())

    def loadListFromFile(self, fileName):
        with open(fileName, 'r') as inventoryFile:
            reader = csv.reader(inventoryFile)
            firstLine = True
            for row in reader:
                if(firstLine):
                    firstLine = False
                    continue
                self.addArticle(Article.Article(int(row[0]), str(row[1]), float(row[2])))
