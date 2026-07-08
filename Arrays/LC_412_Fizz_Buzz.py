class Solution(object):
    def fizzBuzz(self, n):
        b = []
        for i in range(1,n+1):
            if i % 3 == 0 and i % 5 == 0 :
                b.append("FizzBuzz")
            elif i % 3 == 0 : 
                b.append("Fizz")
            elif i % 5 == 0 :
                b.append("Buzz")
            else:
                b.append(str(i))
        return b 







