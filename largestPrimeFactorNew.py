import math

def largest_prime_factor(n):
   prime_list=[]
   while n % 2 == 0:
       n = n/2
   for i in range(3,int(math.sqrt(n)+1),2):
      while n % i == 0:
         n = n/i
         prime_list.append(i)
   print('largest prime factor: {}'.format(prime_list[-1]))


a = int(input('Enter number: '))
largest_prime_factor(a)
