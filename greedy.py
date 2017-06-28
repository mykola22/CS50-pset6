# CS50 pset6 greedy.py
# Known issue: it does't work with user's input if it contain coma 
def main():
    
    #counter for the coins
    getCoins = 0
    
    #geting input from the user
    print("O hai! How much change is owed?:", end=" ")
    money = input()
    
    #making float variable from the users input
    fmoney = float(money)
    
    #protection from the fool
    while fmoney < 0:
        print("Give me a real number?:", end=" ")
        money = input()
    
    #making the integer from the float
    #I'm not completely shure that it is correct way, but it works fine. I guess.
    totalSum = fmoney * 100
    
    #counting the coins
    while totalSum > 0:
        if ((totalSum - 25) >= 0):
            totalSum = totalSum - 25
            getCoins += 1
        elif ((totalSum - 10) >= 0):
            totalSum = totalSum - 10
            getCoins += 1
        elif ((totalSum - 5) >= 0):
            totalSum = totalSum - 5
            getCoins += 1
        elif ((totalSum - 1) >= 0):
            totalSum = totalSum - 1
            getCoins += 1
    #printing the value of the coins counter
    print ("", getCoins)

if __name__ == "__main__":
    main()