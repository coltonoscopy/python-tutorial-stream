'''
CS50 Python Tutorial

Simple shop example, with the ability to buy goods.
'''

import collections
import random

ShopItem = collections.namedtuple('ShopItem', 'name, cost')

shop_items = [ShopItem('Deku Stick', 5), ShopItem('Deku Nut', 5), ShopItem('Deku Shield', 40),
              ShopItem('Kokiri Sword', 60), ShopItem('Fairy Slingshot', 80), 
              ShopItem('Hylian Shield', 90), ShopItem('Bomb', 50)]

def display_shop(items, funds):
    print(f'Welcome to the Kokiri Shop!\nYour funds: {funds} Rupees\n')
    [print(f'{i+1}) {item.name}: {item.cost} Rupees') for i, item in enumerate(items)]
    return int(input('\nSelect an option to purchase (enter -1 to quit): '))

def display_inventory(inventory):
    print('Your Inventory:')
    
    if inventory: 
        [print(item.name) for item in inventory]
    else: 
        print('Empty!')
    
    print()

if __name__ == '__main__':

    # create a set of shop items from our list of options above, then turn into list
    shop = list(set([random.choice(shop_items) for i in range(5)]))

    # an amount of money to spend
    wallet = 100

    # an inventory of items
    inventory = []

    display_inventory(inventory)
    choice = display_shop(shop, wallet)

    # poll for sentinel input until we quit or hit a valid shop choice
    while choice != -1:

        # ensure we're within the shop's bounds
        if choice < 0 or choice >= len(shop) + 1:
            print('Invalid choice; be sure to choose one of the listed options!')
        else:
            if shop[choice - 1].cost > wallet:
                print("Oops; you can't afford that! Try again!\n")
            else:
                print(f"\nThank you for your purchase of the {shop[choice - 1].name}!\n")
                wallet -= shop[choice - 1].cost
                inventory.append(shop.pop(choice - 1))

        display_inventory(inventory)
        choice = display_shop(shop, wallet)

    print("Thanks for your patronage; please come again!")