class Bank:
    def __init__(self,bifsc,bnm,baddr,bbranch):
        self.bankId = bifsc
        self.bankName= bnm
        self.bankAddress= baddr
        self.bankBranch=bbranch
        self.customers=[]

    def __str__(self):
        return '\n BankId : {}, BankName : {}, BankAddress : {},BankBranch : {}\n Customers :{}'.format(self.bankId,self.bankName,self.bankAddress,self.bankBranch,  self.customers)

    def __repr__(self):
        return str(self)