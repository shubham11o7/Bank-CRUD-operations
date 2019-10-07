from CustomerInfo import Customer
from AccountInfo import Account
from BankInfo import Bank

b1 = Bank("ICICI2832", "ICICI", "Pune", "Karve")
b2 = Bank("SBI3433", "SBI", "Pune", "Karve")
b3 = Bank("HDFC2636", "HDFC", "Pune", "Karve")



b1c1 = Customer(1011, "Abhay", 22, "Pune")
b1c2 = Customer(1341, "BBBB2", 52, "Pune")
a1 = Account(1911225, "Saving", 150000.34)
a11 = Account(142325, "Saving", 15000.34)
a2 = Account(2411224, "Saving", 93833.63)
b1c1.custAccounts.add(a1)
b1c1.custAccounts.add(a11)
b1c2.custAccounts.add(a2)



b2c1 = Customer(9011, "AAAA", 23, "Pune")
b2c2 = Customer(9321, "BCCC", 22, "Pune")
b2c3 = Customer(9341, "CCVV", 32, "Pune")
a3 = Account(361223, "Current", 83843.56)
a4 = Account(494522, "Saving", 37353.33)
a5 = Account(5911225, "Saving", 68433.34)
b2c1.custAccounts.add(a3)
b2c2.custAccounts.add(a4)
b2c3.custAccounts.add(a5)


b3c1 = Customer(7011, "TTT", 52, "Pune")
b3c2 = Customer(7341, "BTVVB", 72, "Pune")
b3c3 = Customer(7011, "AAFA", 62, "Pune")
b3c4 = Customer(7231, "BAFFFB", 22, "Pune")

a6= Account(611224, "Saving", 353833.63)
a7 = Account(761223, "Current", 243843.56)
a77 = Account(451223, "Current", 4233843.56)
a8 = Account(894522, "Saving", 38353.33)
a9 = Account(94522, "Saving", 18353.33)

b3c1.custAccounts.add(a6)
b3c2.custAccounts.add(a7)
b3c2.custAccounts.add(a77)
b3c3.custAccounts.add(a8)
b3c4.custAccounts.add(a9)


b1.customers.extend([b1c1,b1c2])
b2.customers.extend([b2c1,b2c2,b2c3])
b3.customers.extend([b3c1,b3c2,b3c3,b3c4])

listOfBanks = [b1,b2,b3]

#print(listOfBanks)

