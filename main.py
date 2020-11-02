from articles import Article
from articles import Inventory

superMarketInventory = Inventory.Inventory()
superMarketInventory.loadListFromFile("Inventory.csv")
superMarketInventory.addArticle(Article.Article(12, "AbraKadabra", 99.99))
superMarketInventory.addArticle(Article.Article(123, "Monster Energy", 1.99))
superMarketInventory.saveListToFile("Inventory.csv")
