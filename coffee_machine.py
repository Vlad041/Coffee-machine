water = 400
milk = 540
beans = 120
cups = 9
money = 550


def available():
    print('''
The coffee machine has:
''' + str(water) + ''' of water
''' + str(milk) + ''' of milk
''' + str(beans) + ''' of coffee beans
''' + str(cups) + ''' of disposable cups
''' + '$' + str(money) + ''' of money
''')


def buy():
    print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
    global water
    global milk
    global beans
    global money
    global cups
    coffee_type = input()
    if coffee_type == '1':
        if water <= 250:
            print('Sorry, not enough water!')
        elif beans <= 16:
            print('Sorry, not enough beans!')
        else:
            water -= 250
            beans -= 16
            money += 4
            cups -= 1
            print('I have enough resources, making you a coffee!')
    elif coffee_type == '2':
        if water <= 350:
            print('Sorry, not enough water!')
        elif milk <= 75:
            print('Sorry, not enough milk!')
        elif beans <= 20:
            print('Sorry, not enough beans!')
        else:
            water -= 350
            milk -= 75
            beans -= 20
            money += 7
            cups -= 1
            print('I have enough resources, making you a coffee!')
    elif coffee_type == '3':
        if water <= 200:
            print('Sorry, not enough water!')
        elif milk <= 100:
            print('Sorry, not enough milk!')
        elif beans <= 12:
            print('Sorry, not enough beans!')
        else:
            water -= 200
            milk -= 100
            beans -= 12
            money += 6
            cups -= 1
            print('I have enough resources, making you a coffee!')
    elif coffee_type == 'back':
        pass


def fill():
    global water
    global milk
    global beans
    global cups
    print('Write how many ml of water do you want to add:')
    water += int(input())
    print('Write how many ml of milk do you want to add:')
    milk += int(input())
    print('Write how many grams of coffee beans do you want to add:')
    beans += int(input())
    print('Write how many disposable cups of coffee do you want to add:')
    cups += int(input())


def take():
    global money
    print('I gave you $' + str(money))
    money = 0


while True:
    print('Write action (buy, fill, take, remaining, exit):')
    request = input()
    if request == 'buy':
        buy()
    elif request == 'fill':
        fill()
    elif request == 'take':
        take()
    elif request == 'remaining':
        available()
    elif request == 'exit':
        break
