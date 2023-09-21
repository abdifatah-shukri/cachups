 #string 
# # anything with qoutes '2'"4
# # numbers
# # 1 2 3 4 
# # booleans  false true
# # None


# # sequences
# # list

# my_list=[1,2,3,4,5]
# my_word=["a","halo","main"]

# # tuple
# (1,2,3,4)

# #set
# set_one={1,2,3,4,5}
# print(set([1,2,4,7,7,74,56,2,4,]))

# # control flow
# # comparisonoperators ==, !=, >,<, <=,>=

# print (3>"3")

# #logical operators and or not
# print (3==3 and 2>4) 
# if 5 not in my_list:
#     print("none existence")
# elif 5 not in my_list:
#     print("you got me")

# #conditional statement 
# x=0
# if x>=20:
#     print(f"counting down,{x}")
#     x=x-1
# elif x<0:
#     print("x is a negative")
# else:
#     pass
# try:
#     #logic to run
#     pass
# except:
#     #logic to run
#     pass

# car ="white"
# dict_map={
#     "black":"ksh8000",
#     "blue":"ksh700",
#     "red":"ksh5000"
# }
# payment = dict_map.get(car)
# print(payment)


# #basic loop
# i=0
# while i<10:
#     print(f"counting {i}")
#     i+=1


#     # for loop
# for i in range(10):
#     print(f"counting{i}")

#     # list comprehension

#     halfed= [x for x in my_list if x==2]
#     print(halfed)

#     # sorted
#     # sort
#     # new_l
#     # print()

#     class Car:
#         pass
#         def init (self):
#             print("new instance of class car created")

#         def start_engine(delf):
#             print("engine roer")

#     bmw = Car()

#WEEK2 CATCHUP STARTS FROM HERE

#oop
    #class
    #instance
    #class attribute and method
    #instance attribute and methods
    #inheritance

    # CLASS
    # INSTANCE
    # Class attributes & methods
    # instance attributes & methods
    # inheritance
    # decorator

# instance method - deposit  that takes amount
# self.initial balance

# Savings account
# subClass => SavingsAccount



class Bank_accounts:
    total_balance = 0

    def __init__(self,acc_number,acc_name,balance):
        self.acc_number = acc_number
        self.acc_name = acc_name
        self.balance = balance
        Bank_accounts.total_balance += self.balance
    
    @classmethod
    def total_bank_balance(cls):
            print(cls.total_balance)

    def deposit(self, amount):
        self.balance += amount
        Bank_accounts.total_balance += amount


    def check_balance(self):
        print(f'Hello {self.acc_name}, Your current balance is {self.balance}')

    def withdraw(self,amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f'Hello {self.acc_name},You have successfully withdrawn Ksh {amount}. Your current balance is {self.balance}')
        else:
            print("Insufficient balance")


class Savings_account(Bank_accounts):
        
        def add_interest(self):
            self.balance *= 1.03


Bin = Bank_accounts(122334422,"Bin Amin",0)
Dan = Bank_accounts("122223334423","Danwycliff",5000)
Bin.deposit(60000)

print(Bank_accounts.total_bank_balance())
