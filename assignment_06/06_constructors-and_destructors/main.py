# jb bhi hum class ka object bnate hain to hamara special method automatically chlta hai wo hai __init__
#  aur wo jese hi chlta hai to us k ander jo bhi kam krwaya hota hai ham ne wo ajata hai .
# for example: hum ne koi msg print krwaya hai isse (Constructor) kehte hain
# destructor-------
# jb bhi hamara program end hota hai  ya hum kuch delete krte hain to ye method bhi automatically chl jata hai
# is ka kam hota hai clean up krna ya good bye msg dena

class Logger:
    def __init__(self):
        print("Object Created")   #Constructor
        
    def __del__(self):
        print("Object Destroyed")   # Destructor
        
if __name__ == "__main__":
    log = Logger()
    #del log     
    
    # agr hum isse comment bhi kr dain to bhi destructed chale ga 
    # q k del k ilada hum ne btaya k jb programm end hota hai to bhi destructor chlta hai
    
    