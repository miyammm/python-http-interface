# assert是断言语句，用于检查表达式是否为真，如果为假会引发AssertionError错误，并抛出
n = int(input("请输入成绩："))
assert 0 <= n <= 100
# 断言n一定在[0,100]这个范围内，如果不在这个范围内触发断言错误，程序不再继续执行
print("考试分数为：",n)

'''
应用场景：函数或类中的方法，对参数格式有严格的定义时，可以使用assert对传入的参数进行断言判断
使用断言去检测程序中理论上不应该出现的情况。
当用户输入或者外部环境（比如网络延迟、文件不存在等）引起的问题时，一般用异常。
'''