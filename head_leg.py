heads =  int(input("provide the number of heads : "))
legs =  int(input("provide the number of legs : "))

if legs%2 != 0:
    print("Invalid Input value for legs")
else:
    if heads == 1 and legs == 2:
        print("Just a hen")
    elif heads == 1 and legs == 4:
        print("just a dog")
    elif heads == 2 and legs == 4:
        print("Two hens")
    elif heads >=2 and legs >=6:
        goat = legs//4
        hen = heads -goat
        
        while goat > 0 and hen > 0:
            total_legs = (goat*4)+(hen*2)
            if total_legs > legs:
                goat = goat-1
                hen = hen+1
            elif total_legs == legs:
                print(f"goat = {goat} and hen = {hen}")
                break
            else:
                hen = hen-1
                goat = goat +1
        



