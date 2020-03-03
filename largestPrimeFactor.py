import math

def prime_checker(n):
   res = n%10
   count=0
   if res == 0 or res == 2 or res == 4 or res == 6 or res == 8:
      return -1
   elif res == 0 or res == 5:
      return -1
   else:
      num = [int(i) for i in str(n)]
      if sum(num)%3 == 0:
         return -1
      else:
         sq_root = int(math.sqrt(n))
         for i in range(sq_root,6,-1):
             if n%i == 0:
                count+=1
         if count > 0:
             return -1
         else:
             return 1

a = int(input('Enter number: '))
if prime_checker(a) == 1:
   print('largest prime factor is : {}'.format(a))
else:
   for i in range((int(math.sqrt(a))),1,-1):
      if prime_checker(i) == 1:
         if a%i == 0:
            print('Largest prime factor is : {}'.format(i))
            break
   
      
