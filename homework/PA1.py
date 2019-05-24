import platform, traceback


#Takes in a list of Account objects accountList, and if there are at least 2
#Account objects in the list, subtracts 1337 from the Account with the maximum
#balance and adds 1337 to the Account with the minimum balance.  Returns nothing.
def hack_bank(account_list):
    # TODO: Implement this.
    if len(account_list) > 1:
        min_ = max_ = account_list[0]
        for i in range(0, len(account_list)):
            if min_.get_balance() > (account_list[i]).get_balance():
                min_ = account_list[i]
            if max_.get_balance() < (account_list[i]).get_balance():
                max_ = account_list[i]

        for i in range(0, len(account_list)):
            if account_list[i].get_name() == min_.get_name():
                account_list[i].add_balance()
            if account_list[i].get_name() == max_.get_name():
                account_list[i].sub_balance()



pass

#Account class (you are not required to change anything here, but you may want
# to add some extra methods)
class Account:
    #Initialize an Account object.  Account objects have two instance variables
    #self.name is a string, representing the name associated with the Account
    #self.balance is a float, representing the balance of the account in $.
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
    #String representation of an Account object - "name: $balance"
    def __repr__(self):
        return self.name + ": $" + str(self.balance)
    def __gt__(self,other):
        return self.balance > other.balance

    def get_balance(self):
        return self.balance

    def add_balance(self):
        self.balance += 1337

    def sub_balance(self):
        self.balance -= 1337

    def get_name(self):
        return self.name


# DO NOT EDIT ANYTHING BELOW THIS LINE

#Test Cases
a1 = Account("Scrooge McDuck", 10000000000)
a2 = Account("Macklemore",20)
a3 = Account("Loch Ness Monster",3.5)
a4 = Account("College Student",-78000)
a5 = Account("Bruce Wayne", 212013114)
a6 = Account("The Shoe from Monopoly",200)
a7 = Account("Sheriff of Nottingham",78000)
a8 = Account("Emmitt Brown", -80)
a9 = Account("Jesse Loude", -4.74)
a10 = Account("Ron Weasley", 0)

a11 = Account("Scrooge McDuck", 10000000000)
a12 = Account("Macklemore",20)
a13 = Account("Loch Ness Monster",3.5)
a14 = Account("College Student",-78000)
a15 = Account("Bruce Wayne", 212013114)
a16 = Account("The Shoe from Monopoly",200)
a17 = Account("Sheriff of Nottingham",78000)
a18 = Account("Emmitt Brown", -80)
a19 = Account("Jesse Loude", -4.74)
a20 = Account("Ron Weasley", 0)
a21 = Account("Lone Starr", -1000000)

bank1 = []
bank2 = [a5]
bank3 = [a1,a2,a3,a4]
bank4 = [a6,a7]
bank5 = [a8,a9,a10]
bank6 = [a21,a14,a18,a19,a16,a13,a17,a20,a11,a12,a15]

ans1 = []
ans2 = [212013114]
ans3 = [9999998663,20,3.5,-76663]
ans4 = [1537,76663]
ans5 = [1257,-4.74,-1337]
ans6 = [-998663,-78000,-80,-4.74,200,3.5,78000,0,9999998663,20,212013114]

test_banks = [bank1,bank2,bank3,bank4,bank5,bank6]
correct_balances = [ans1,ans2,ans3,ans4,ans5,ans6]

count = 0

try:
    vers = platform.python_version()
    assert vers[0] == '3', "You must use Python 3, "+vers+" is not acceptable"
    for i in range(len(test_banks)):
        print("TEST #"+str(i+1))
        original_names = list(map(lambda x: x.name,test_banks[i]))
        print("Running: hack_bank(",test_banks[i],")\n")
        hack_bank(test_banks[i])
        correct = list(map(lambda x,y: Account(x,y),
                           original_names,correct_balances[i]))
        print("Expected:",correct,"\n\nGot:",test_banks[i])
        assert len(correct) == len(test_banks[i]), "Number of bank accounts altered"
        for j in range(len(test_banks[i])):
            acc = test_banks[i][j]
            assert acc.name == original_names[j], original_names[j] + \
                   " account name altered." 
            assert acc.balance == correct_balances[i][j], acc.name + \
                   " account balance incorrect."
        count=count+1
        print("\n---------------------------------------\n")

except AssertionError as e:
    print("\nFAIL: ",e)
except Exception:
    print("\nFAIL: ",traceback.format_exc())


print("\n---------------------------------------\n")
print(count,"out of",6,"tests passed.")

