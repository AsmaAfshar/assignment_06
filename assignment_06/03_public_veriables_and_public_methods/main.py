class Car:
# publiv veriable
    def __init__(self, brand):
        self.brand = brand
        
# public method     
    def  start(self):
        print(f"{self.brand} is starting...")
        
if __name__ == "__main__":
    my_car = Car("Ferrari")  # object bn gya
# class k bahar se public veriable ko access kr rhe
    print(my_car.brand)
# public method access kr rhe class k bahar se
    my_car.start()

    