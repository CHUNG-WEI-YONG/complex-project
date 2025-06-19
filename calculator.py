#📝 Problem Statement
#Write a function that prints the numbers from 1 to n.
#But for multiples of 3, print "Fizz" instead of the number,
#for multiples of 5, print "Buzz",
#and for numbers which are multiples of both 3 and 5, print "FizzBuzz
def buzzfizz():
    i = int(input("What is your number? \n >>"))
    for number in range(1 , i+1):
        if number %3 == 0 and number%5 ==0:
            print ("FIZZBUZZ")
        elif number %3 == 0:
            print("FIZZ")
        elif number %5 == 0:
            print("Buzz")
        else:
            print(number)

buzzfizz()
        
