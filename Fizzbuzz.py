#loop for 100 times i.e. range 
for fizzbuzz in range(100):  
  
    # divisible by 3, print 'Fizz'  
    # instead of number 
    if fizzbuzz % 15 == 0:  
        print("FizzBuzz")                                          
        continue
  
    # divisible by 5, print 'Buzz' 
    # instead of number 
    elif fizzbuzz % 3 == 0:      
        print("Fizz")                                          
        continue
  
    # divisible by both 3 & 5, print 'FizzBuzz' 
    # instead of number 
    elif fizzbuzz % 5 == 0:          
        print("Buzz")                                      
        continue
  
    # print numbers 
    print(fizzbuzz) 
