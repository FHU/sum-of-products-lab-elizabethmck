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

    if len(list1) == len(list2):
        num1 = split1[0] * split2[0]
        num2 = split1[1] * split2[1]
        num3 = split1[2] * split2[2]

        sum = num1+num2+num3
        return sum
    
    else:
        print("error")

if __name__ == '__main__':
    a = input()
    b = input()

    total = sum_of_products(a,b)
    #test
    print(total)

# Test