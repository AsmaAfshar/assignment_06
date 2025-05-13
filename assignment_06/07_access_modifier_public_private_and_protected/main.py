# protected variable single under score se access hoga
# private  variable double under score se access hoga
# public variable easa variable jo k class k andr aur bahar dono jaga access ho jata hai
# protected variable easa variable jo class k andr access hota hai aur bahe bhi ho jata hai access mgr
# recommended nhi hota ye (semi private variables) hote hain jo class sub class hr jga acess ho skte hain 
# but recommended nhi hain.
#  private variable jo k nam se zahir hain sirf class k andr hi access hote hain class k bahr acces krte hain
# to attribute error ajata hai



class Employee:
    def __init__(self, name, salary, ssn):    # ssn means (social securiry number)
        self.name = name  # public variable
        self._salary = salary  # protected variable
        self.__ssn = ssn      # private variable
        
if __name__ == "__main__":
    emp = Employee("Asma", 40000, "123-4576-90")
# access public variable
    print("Public Variable:", emp.name)
#access protected variable   
    print("Protected Variable:", emp._salary)
#access private variable    

# error ko custom bnane k lie try expet ka method use kra
    try:
        print("Private Variable:", emp.__ssn)
    except AttributeError:
        print("Cannot access private variable__ssn")