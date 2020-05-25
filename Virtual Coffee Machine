class CoffeeMachine:

    def __init__(self, water, milk, beans, cups, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money

    def remain(self):
        print(f'''
    The coffee machine has:
    ''' + str(self.water) + ''' of water
    ''' + str(self.milk) + ''' of milk
    ''' + str(self.beans) + ''' of coffee beans
    ''' + str(self.cups) + ''' of disposable cups
    ''' + '$' + str(self.money) + ''' of money
    ''')

    def buy(self):
        coffee_type = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
        if coffee_type == '1':
            if self.water <= 250:
                print('Sorry, not enough water!')
            elif self.beans <= 16:
                print('Sorry, not enough beans!')
            else:
                print('I have enough resources, making you a coffee!')
                self.water -= 250
                self.beans -= 16
                self.money += 4
                self.cups -= 1
        elif coffee_type == '2':
            if self.water <= 350:
                print('Sorry, not enough water!')
            elif self.milk <= 75:
                print('Sorry, not enough milk!')
            elif self.beans <= 20:
                print('Sorry, not enough beans!')
            else:
                self.water -= 350
                self.milk -= 75
                self.beans -= 20
                self.money += 7
                self.cups -= 1
                print('I have enough resources, making you a coffee!')
        elif coffee_type == '3':
            if self.water <= 200:
                print('Sorry, not enough water!')
            elif self.milk <= 100:
                print('Sorry, not enough milk!')
            elif self.beans <= 12:
                print('Sorry, not enough beans!')
            else:
                self.water -= 200
                self.milk -= 100
                self.beans -= 12
                self.money += 6
                self.cups -= 1
                print('I have enough resources, making you a coffee!')
        elif coffee_type == 'back':
            pass

    def fill(self):
        self.water += int(input('Write how many ml of water do you want to add:'))
        self.milk += int(input('Write how many ml of milk do you want to add:'))
        self.beans += int(input('Write how many grams of coffee beans do you want to add:'))
        self.cups += int(input('Write how many disposable cups of coffee do you want to add:'))

    def take(self):
        print(f'I gave you $' + str(self.money))
        self.money = 0

    def power_on(self):
        while True:
            action = input('Write action (buy, fill, take, remaining, exit):')
            if action == 'buy':
                CoffeeMachine.buy(self)
            elif action == 'fill':
                CoffeeMachine.fill(self)
            elif action == 'take':
                CoffeeMachine.take(self)
            elif action == 'remaining':
                CoffeeMachine.remain(self)
            elif action == 'exit':
                break


Coffee_Machine = CoffeeMachine(400, 540, 120, 9, 550)
Coffee_Machine.power_on()
