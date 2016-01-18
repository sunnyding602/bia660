def fib(num):
    first = 1
    second = 1
    print first
    print second
    position_of_current_num = 3
    while (position_of_current_num <= num):
        next = first + second
        print next
        first = second
        second = next
        position_of_current_num = position_of_current_num+1
            
            


print fib(3)
