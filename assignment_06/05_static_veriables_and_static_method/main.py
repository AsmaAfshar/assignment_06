# static ka mtlb hi calculation hota hai
# static method  ka mtlb jo kam hum krenge wo logic base hoga jesa k is me hamen sum krne k lie dia hai
# static metod easa method hota hai jis me na to class use hoti hai aur na hi object pe kam hoga
# means k na to is me (cls) use hoga na (self)

class MathUyils:
    @staticmethod   # calculation and comparison etc logic run krwana ho
    
    def add(a , b):
        return a + b
 
if __name__ == "__main__":
    result = MathUyils.add(10 , 5)
    print("Sum is equal to", result)