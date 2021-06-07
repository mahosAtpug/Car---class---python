class Car(object):
    def __init__(self , color , model , speedLimit , company ):
        self.color = color
        self.model = model
        self.speedLimit = speedLimit
        self.company = company

    def start(self):
        print("Started")
    
    def stop(self):
        print("Stopped")
    
    def accelerate(self):
        print("Accelerating")

audi = Car("Red" , "A6" , "200 kmph" , "Audi")
print(audi.color)

audi.start()
audi.accelerate()
audi.stop()

mercedes = Car("Grey" , "S" , "160 kmph" , "Mercedes Benz")
print(mercedes.speedLimit)
print(mercedes.company)



