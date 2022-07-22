from main import *



def checkStockSymbol(output):

    while True:

        SpecialCharacters = False
        userInput = output
        if 0 < len(userInput) <= 7:  #checks if user inputs a string between 1 and 5 characters
            for letter in userInput:
                if not letter.isupper() and not letter.isalpha(): #checks if letter isn't a number or a letter
                    SpecialCharacters = True
                    print("Test Failed; symbol included special characters ")
                    #unitTest break
                    break
            if not SpecialCharacters:
                break
        else:
            print("please input a symbol of 5 characters or less")
            #unitTest break
            break
        break


    return userInput, print("test passed ")




checkStockSymbol(get_stock_symbol())
