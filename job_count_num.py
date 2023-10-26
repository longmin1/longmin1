def decorator(func):
    n=0
    def inner(*args,**kwargs):
        func(*args,**kwargs)
        nonlocal n
        n+=1
        print(f"函数{func.__name__}程序被调用{n}次")
    return inner

@decorator
def count_num():
    print("开始运行")


for i in range(10):
    count_num()