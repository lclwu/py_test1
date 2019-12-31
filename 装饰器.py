import time

def my_object(keys):#装饰器参数
    def my_func(func):
        def my_cresdit(*args):#被装饰方法参数
            print(keys)
            print(time.time())
            a=func(*args)#装饰
            print(time.time())
            return a
        return my_cresdit
    return my_func

@my_object(2)
def adds(key):
    print("你好呀")
    return key

if __name__=="__main__":
    a=adds(10)
