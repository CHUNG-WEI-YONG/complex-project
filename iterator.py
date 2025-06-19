class SquareIterator:
    def __init__(self,n):
        self.n = n
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration
        val =self.current**2
        self.current +=1
        return val


class ReverseSquareIterator:
    def __init__(self,n):
        self.n = n
        self.current =n

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration
        val = self.n **2
        self.n -=1
        return val



    
class EvenSquareIterator:
    def __init__(self,n):
        self.current = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.current<1:
            raise StopIteration
        val = self.current **2
        self.current -= 1
        if val %2 == 0:
            return val
        else:
            return self.__next__()

    if __name__ == "__main__":
        for x in EvenSquareIterator(5):
            print(x)
        print("Done!")


class InfiniteSquareIterator:
    def __init__(self):
        self.current = 1
        

    def __iter__(self):
        return self

    def __next__(self):
        val = self.current**2
        self.current+=1
        return val



class DivisibleSquareIterator:
    def __init__(self,n,k):
        self.current = 1
        self.k = k
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration
        val = self.current**2
        self.current+=1
        if val % self.k == 0:
            return val
        else:
            return self.__next__()


class InfiniteFibonacciIterator:
    def __init__(self):
        self.a = 0  # 当前值
        self.b = 1  # 下一个值

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            self.a,self.b = self.b, self.a+b
            value = self.a
            return value
        
