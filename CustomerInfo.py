class Customer():

    def __init__(self,cid,cnm,aage,address):
        self.custId=cid
        self.custName=cnm
        self.custAge=aage
        self.custAddress=address
        self.custAccounts = set()

    def __str__(self):
        return '\n CustId : {},CustName : {}, CustAge : {},CustAddress : {} \n Accounts {}'.format(self.custId,self.custName,self.custAddress,self.custAge,self.custAccounts)

    def __repr__(self):
        return str(self)