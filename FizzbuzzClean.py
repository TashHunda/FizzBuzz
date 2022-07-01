#loop for 100 times i.e. range 
for fizzbuzz in range(1,101):  
  
  # divisible by 3, print 'Fizz' instead of number 
    if fizzbuzz % 3 == 0:      
        print("Fizz")                                          

    # divisible by  5, print 'Buzz' instead of number 
    elif fizzbuzz % 5 == 0:          
        print("Buzz")                                      

     # divisible by 3 & 5, print 'FizzBuzz' instead of number 
    elif fizzbuzz % 15 == 0:  
        print("FizzBuzz")                                          
    
    # print numbers 
    print(fizzbuzz) 