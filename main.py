from articles import Article
from articles import Inventory

def main():
    switchVal = 99
    while(switchVal < 100):
        print("Please choose one of the following actions: \n [0] Return 0 \n [1] Return 1 \n [2] Return 2 \n [3] Return 3 \n [100] End Programm"  )
        switchVal = input()

main()
#superMarketInventory = Inventory.Inventory()
#superMarketInventory.loadListFromFile("Inventory.csv")
#superMarketInventory.addArticle(Article.Article(12, "AbraKadabra", 99.99))
#superMarketInventory.addArticle(Article.Article(123, "Monster Energy", 1.99))
#superMarketInventory.saveListToFile("Inventory.csv")
