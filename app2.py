import pandas as pd
from enum import Enum
import statistics

if __name__ == "__main__":
    df = pd.read_csv('diamonds.csv')
    user_result = ""

    class Actions(Enum):
        Exit = 0
        AVERAGE_PRICE = 1
        MOST_EXPENSIVE = 2
        COUNT_IDEAL = 3
        COUNT_BY_COLOUR = 4
        AVERAGE_PER_CARAT = 5
        AVERAGE_PER_COLOUR = 6

    def most_expensive():
        priced = list(df['price'])
        print(f"The highest price is:{max(priced)}")

    def avaraged():
        priced = list(df['price'])
        print(f"The average price is:{statistics.mean(priced):.2f}")

    def menu():
        for act in Actions:
            print(f"{act.value}-{act.name}")
        return input("What is your selection?")
    
    def ideal_cut():
        ideal = list(df['cut'])
        count = sum(1 for x in ideal if x == 'Ideal')
        print(f"There are {count} diamonds with an Ideal cut.")

    def colored():
        colors = list(df['color'])
        userchoice = input("Choose a color letter (e.g., 'D' 'E' 'F' 'H' 'I' 'G' 'J'.): ")
        countC = sum(1 for x in colors if x == userchoice)
        print(f"There are {countC} diamonds of color {userchoice}.")

    def average_per_carat():
        avg_price_per_carat = df.groupby('cut')['carat'].mean()
        print("Average price per carat:")
        for cut, avg_price in avg_price_per_carat.items():
            print(f"{cut}: {avg_price:.2f}")

    def average_per_colour():
        average_per_colour = df.groupby('color')['price'].mean()
        print("Average price per colour:")
        for cut, avg_price in average_per_colour.items():
            print(f"{cut}: {avg_price:.2f}")

    while True:
        user_result = Actions(int(menu()))  
        if user_result == Actions.Exit:
            print("Exiting the program.")
            break
        elif user_result == Actions.MOST_EXPENSIVE: most_expensive()
        elif user_result == Actions.COUNT_IDEAL: ideal_cut()
        elif user_result == Actions.AVERAGE_PRICE: avaraged()
        elif user_result == Actions.COUNT_BY_COLOUR: colored()
        elif user_result == Actions.AVERAGE_PER_CARAT: average_per_carat() 
        elif user_result == Actions.AVERAGE_PER_COLOUR: average_per_colour() 
        else:
            print("error choose from the menu.")
