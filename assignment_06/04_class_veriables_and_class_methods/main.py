# class veriables 
class Bank:
    bank_name = "Alfalah Bank"
    
    @classmethod    #ye decurator class method k lie use hoga 
    def change_bank_name(cls, name):    # -----> parameters
        cls.bank_name = name
        
if __name__ == "__main__":
    user1 = Bank()       # --> objects
    user2 = Bank()
    
    print("Before changing bank name:")
    print(f"User1's bank name: {user1.bank_name}")
    print(f"User2's bank nmae: {user2.bank_name}")
    
    Bank.change_bank_name("Habib Bank Limited")
    print("\nAfter changing bank name:")
    
    print(f"User1's bank name:{user1.bank_name}")
    print(f"User2's bank nmae: {user2.bank_name}")