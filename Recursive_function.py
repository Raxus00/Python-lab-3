int_num = int(input("Input a number:")) 

def count_digits(int_num):
    if int_num < 10:
        return 1
    else:
        return 1 + count_digits(int_num/10)
print (count_digits(int_num))
        
         