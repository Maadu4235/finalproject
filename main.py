from multiprocessing import Process

def A():
    return "first function"

def B():
    return "second function"

if __name__=="__main__":
    p1=Process(target=A)
    p2=Process(target=B)
    p1.start()
    p2.start()

    p1.join()
    p2.join()
    print(" Both process completed")