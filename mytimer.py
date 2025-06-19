import time as t

class MyTimer():
    def __init__(self):
        self.unit = ['year','month','day','hour','minutes','second']
        self.prompt = "Havent started"
        self.lasted = []
        self.init = False
        self.end = False
    def __str__(self):
        return self.prompt
    __repr__=__str__

    
    def start(self):
        if self.init == False:
            self.starttime = t.localtime()
            print("Timer started")
            self.prompt = "Please stop first"
            self.init = True
        else:
            print("The timer has been started")

    def __add__(self,other):
        prompt = "Total time is"
        result =[]
        for index in range(6):
            result.append(self.lasted[index]+other.lasted[index]
            prompt+= (str(result[index]+self.unit[index]))
        return prompt
            

    def stop(self):
        if self.init == True:
            self.stoptime = t.localtime()
            print("Timer stopped")
            self._calc()
        else:
            print("The timer has not been started")

    def _calc(self):
        self.lasted =[]
        self.prompt = "Run for "
        for index in range (6):
            self.lasted.append(self.stoptime[index]-self.starttime[index])
            if self.lasted [index]:
                self.prompt += (str(self.lasted[index])+self.unit[index])
        self.__repr__

    def reset(self):
        self.prompt = "Havent started"
        self.lasted = []
        self.init = False
        self.end = False
        print("Timer has been reset")
        
              

