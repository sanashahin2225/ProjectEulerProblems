num=[]
def  fibo(n):
   a,b=1,2
   print(a)
   print(b)
   for i in range(0,n):
      sum1=a+b
      print(sum1)
      if  sum1%2==0:
         num.append(sum1)
      a=b
      b=sum1

fibo(10)
print("Even Valued sum: {}".format(sum(num)))
