#REMOVE PASS AND FIX THE FUNCTION
#change to test push and forks

def sum_of_products(list1, list2):
    split1 = []
    split2 = []
    
    for i in list1:
        if i.isspace():
            continue
        else:
            split1.append(int(i))
    for i in list2:
        if i.isspace():
            continue
        else:
            split2.append(int(i))

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