#REMOVE PASS AND FIX THE FUNCTION
#change to test push and forks

def sum_of_products(list1, list2):
    split1 = []
    split2 = []
    
    list1 = list1.split()
    list2 = list2.split()

    x = 0
    for y in range(len(split1)):
        x = x + int(split1[y]) * int(split2[y])
    return x
    
   # else:
        #print("error")

if __name__ == '__main__':
    list1 = input()
    list2 = input()

    total = sum_of_products(list1,list2)
    #test
    print(total)

# Test