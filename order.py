""""""

from datetime import datetime
import random

ITEMS = {} # Dictonary for matching an item to its order count
USERS = {} # Dictionary for matching a macid to a user object

class User:
    """Class to represent a student.
        password: password of the student (HASHED)
        item_dict: dictionary of items that the user has eaten
        -- keys are the items
        -- values are tuples of Dates and counts
    """
    def __init__(self, macid, password, item_dict=None):
        self.macid = macid
        self.password = password
        self.item_dict = item_dict if item_dict else {}

    def order_item(self, item):
        """When an item is ordered,  adds the item to a personal list of eaten items and the dates when you eat them"""
        if (item not in self.item_dict.keys()):
            self.item_dict[item] = (Date(datetime.now()), 1)
        else:
            d, c = self.item_dict[item]
            c += 1
            d.add_date(datetime.now())
            self.item_dict[item] = (d, c)
        ITEMS[item] += 1
      
    def for_you(self, level=1):
        """Returns personal  recommendations based on the amount of times you've ordered, and the last time you ordered it"""
        t_dict = dict(filter(lambda x: x[0].hungerLevel >= level, self.item_dict.items()))
        return max_count(t_dict, lambda x: x[1][1] / (datetime.now().day - x[1][0].dates[0].day + 1))
  
    def recommended(self, level=1):
        """Returns most ordered by every user overall"""
        t_dict = dict(filter(lambda x: x[0].hungerLevel >= level, ITEMS.items()))
        return max_count(t_dict, lambda x: x[1])

class Date:
    """Keeps track of dates that a user ordered an item. The most recent date is kept at the front of the list dates."""
    def __init__(self, date: datetime = None):
        self.dates = [] if not date else [date]
  
    def add_date(self, d: datetime):
        """Adds a date to the front of the list, truncates the list if there are more than 10 dates."""
        if len(self.dates) > 10:
            self.dates[:] = [d] + self.dates[1:]
        else:
            self.dates[:] = [d] + self.dates[:]

class Item:
    "A class for representing an item."
    def __init__(self, name, details, restaurant, price, hungerLevel):
        self.name = name
        self.details = details
        self.restaurant = restaurant
        self.price = price
        self.hungerLevel = hungerLevel

def max_count(dic, f):
    """Sorts dictionaries based on a function in descreasing order"""
    t = list(dic.items())
    return sorted(t, key=f, reverse=True)[:min(len(t),10)]

if __name__ == "__main__":
    i_tup = (Item("burger", "", "", 0, 2), 
        Item("spaghetti", "", "", 0, 4),
        Item("perogies", "", "", 0, 2),
        Item("cheese pizza", "", "", 0, 7),
        Item("apple juice", "", "", 0, 1),
        Item("eggs", "", "", 0, 3),
        Item("hotdog", "", "", 0, 4),
        Item("sandwich", "", "", 0, 4),
        Item("coffee", "", "", 0, 1),
        Item("tea", "", "", 0, 1),
        Item("shawarma", "", "", 0, 5),
        Item("shrimp", "", "", 0, 1),
        Item("fried chicken", "", "", 0, 6)
    )
    u_tup = (User("jandricd", "mov2DtikU4Xdl2xb"), 
            User("vishnuc", "XcpVJD7dRoMBdgCV"),
            User("mohrens", "ANiuc981kjc8Cqw"),
            User("abuhatts", "FNJdkjn91fSun3x")
        )

    for item in i_tup:
        ITEMS[item] = 0

    for i in range(len(u_tup)):
        times = random.choice(list(range(30, 120)))
        for j in range(times):
            u_tup[i].order_item(random.choice(i_tup))

    print("Top food items")
    for t in u_tup[0].recommended():
        print(t[0].name, t[1])

    for u in u_tup:
        print("------------------")
        print(f"For you {u.macid}:")
        for t in u.for_you(2):
            print(f"\t{t[0].name}", t[1][1])
