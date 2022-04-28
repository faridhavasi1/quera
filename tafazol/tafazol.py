def game(number:str):

    if int(number[0]) > int(number[1]):
        return int(number[0]) - int(number[1])
    else:
        return int(number[1]) - int(number[0])
    
print(game('45'))    #outbut 1 ===game('54')