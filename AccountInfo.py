class Account:
    def __init__(self,aid,atype,abal):
        self.accountNo = aid
        self.accountType= atype
        self.accountBalance = abal

    def __str__(self):
        return '\n AccNo:{}, AccBal: {}, AccType: {}'.format (self.accountNo,self.accountBalance,self.accountType)

    def __repr__(self):
        return str(self)