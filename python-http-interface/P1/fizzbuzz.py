n=int(input("请输入一个小于100的数字:"))
for i in range(1,n+1):
    if i%3==0:
        if i%5==0:
            print("FizzBuzz")
        else:
            print("Fizz")
    else:
        if i%5==0:
            print("Buzz")
        else:
            print(i)





