# SPOTLESS FR FR

class Machine:
    def __init__(self, water, milk, beans, cups, cash):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.cash = cash
        self.espresso = Coffee(250, 0, 16, 4)
        self.latte = Coffee(350, 75, 20, 7)
        self.cappuccino = Coffee(200, 100, 12, 6)

    def buy(self):
        drinks = {"1": self.espresso, "2": self.latte, "3": self.cappuccino}
        ans = input("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n")
        if ans == "back":
            return

        if self.water >= drinks[ans].water:
            if self.milk >= drinks[ans].milk:
                if self.beans >= drinks[ans].beans:
                    print("I have enough resources, making you a coffee!")
                    self.water -= drinks[ans].water
                    self.milk -= drinks[ans].milk
                    self.beans -= drinks[ans].beans
                    self.cash += drinks[ans].cash
                    self.cups -= 1
                else:
                    print("Sorry, not enough beans!")
            else:
                print('Sorry, not enough milk!')
        else:
            print("Sorry, not enough water!")

    def take(self):
        print(f"I gave you ${self.cash}")
        self.cash = 0

    def fill(self):
        self.water += int(input("\nWrite how many ml of water you want to add:\n"))
        self.milk += int(input("Write how many ml of milk you want to add:\n"))
        self.beans += int(input("Write how many grams of coffee beans you want to add\n"))
        self.cups += int(input("Write how many disposable cups you want to add:\n"))

    def state(self):
        print(f"The coffe machine has:\n"
              f"{self.water} ml of water\n"
              f"{self.milk} ml of milk\n"
              f"{self.beans} g of coffee beans\n"
              f"{self.cups} disposable cups\n"
              f"${self.cash} of money\n")

    def job(self, ans):
        if ans == "buy":
            self.buy()
        elif ans == "take":
            self.take()
        elif ans == "fill":
            self.fill()
        elif ans == "remaining":
            self.state()
        else:
            print("Wrong input!!")
            return

class Coffee:
    def __init__(self, water, milk, beans, cash):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cash = cash


def main():
    machine = Machine(400, 540, 120, 9, 550)

    while True:

        ans = input("Write action (buy, fill, take, remaining, exit):\n")

        if ans == "exit":
            break
        else:
            machine.job(ans)


if __name__ == "__main__":
    main()
