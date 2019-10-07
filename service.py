from abc import ABC,abstractmethod
from Startapp import *

class BankService(ABC):

    @abstractmethod
    def withdraw_amount(self,bankId,accno,amnt):
        pass

    @abstractmethod
    def deposit_amount(self,bankId,accno,amnt):
        pass

    @abstractmethod
    def get_account_balance(self,bankId,accNo):
        pass



class HDFC(BankService):
    def withdraw_amount(self, bankId, accno, amnt):
        bank_found = False
        account_found = False
        trac_success=False

        for bank in listOfBanks:
            if bank.bankId==bankId:
                bank_found=True
                for cust in bank.customers:
                        for account in cust.custAccounts:
                            if account.accountNo==accno:
                                account_found=True
                                if account.accountBalance>=amnt:
                                    print('Customer with name', cust.custName, 'before debit amnnt is', account.accountBalance)
                                    account.accountBalance-=amnt
                                    trac_success=True
                                    print('Customer with name',cust.custName,'debited amnnt is',amnt)
                                    print('Customer with name', cust.custName, 'After debit amnnt is',
                                          account.accountBalance)


                                break
                        if account_found:
                            break
            if bank_found:
                break

        if trac_success:
            print('AMount is withdrawn...')
        elif account_found and trac_success==False:
            print('insufficient balance')
        elif bank_found and account_found==False:
            print('Account not found..!')
        elif bank_found==False:
            print('Bank not exist with given code')



    def deposit_amount(self, bankId, accno, amnt):
        pass

    def get_account_balance(self, bankId, accNo):
        pass

class ICICI(BankService):
    def withdraw_amount(self, bankId, accno, amnt):
        pass

    def deposit_amount(self, bankId, accno, amnt):
        pass

    def get_account_balance(self, bankId, accNo):
        pass

class SBI(BankService):

    def withdraw_amount(self, bankId, accno, amnt):
        pass

    def deposit_amount(self, bankId, accno, amnt):
        pass

    def get_account_balance(self, bankId, accNo):
        pass


hdfcService = HDFC()
hdfcService.withdraw_amount("ICICI2832",142325,5000)