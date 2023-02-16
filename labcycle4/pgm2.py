class BankAccount:
    
    def __init__(self,name,accNumber,accType) -> None:
        self.name=name
        self.accnum=accNumber
        self.acctype=accType
        balance = 0
        self.bal=balance

    def deposit(self,dep):
        self.dep=dep
        self.bal=self.bal+self.dep
        print("Successfully credited to account, new balance in account is : ",self.bal)

    def withdraw(self,amnt):
        self.amnt=amnt
        if(self.amnt > self.bal):
            print("INSUFFICIENT BALANACE")
        else:
            self.bal=self.bal-self.amnt
            print("Rupees {} withdrwan from account new balance is {}".format(self.amnt,self.bal))

ob1 = BankAccount('Vishnu', 1234,'savings')

ob1.deposit(2456)
ob1.withdraw(300)
ob1.withdraw(3000)