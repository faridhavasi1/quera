def game(n1: int, n2: int):
    if n1 and n2 in range(0, 10):
        pass
    else:
        if n1 > n2:
            return n1 - n2
        else:
            return n2 - n1
    
print(game(3,5))    # Output: 2