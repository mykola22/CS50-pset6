def main():
    
    height = 0 #variable for height 
    row = 0 #variable that count the rows
    hash = 0 #variable that  count the hashes
    
    #asking user for valid height of pyramid
    while height <= 0 or height > 23:
        print("How high:", end="")
        height = int(input())
        
    #initial conditions for printing new line for the row
    for row in range (height):
        #printing spaces
        for space in range (height - row - 1):
            print(" ", end=" ")
        #printing hashes    
        for hash in range (row +2):
            print("#", end=" ")
        #printing new line    
        print("")
if __name__ == "__main__":
    main()