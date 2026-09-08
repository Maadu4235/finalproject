from multiprocessing import Process

def A():
    return "first function"

def B():
    return "second function"

def C(a,b):
    return a+b

if __name__=="__main__":
    p1=Process(target=A)
    p2=Process(target=B)
    p3=Process(target=C)
    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()
    print(" Both process completed")