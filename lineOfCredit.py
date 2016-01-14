from __future__ import  division

__author__ = 'POOJA'

class Transaction:
    def __init__(self, amt, day, type):  ##Intializing every transaction with amount, dat and type of transaction
        self.amount = amt
        self.day = day
        self.type = type


class LineOfCredit:
    def __init__(self, credit_line, apr): # getting the credit and apr details
        self.apr = apr
        self.credit_line = credit_line
        self.trans_list = [] #This list maintains all the transaction in the 30 days period for the user



    def calc_payoff_amount(self):
        old_credit_line = self.credit_line # intializing all varaibles used
        old_balance = 0
        new_balance = 0
        old_transaction_date = 0
        new_transaction_date = 0
        noOfDays = 0
        new_credit_line = 0
        interest = 0

        for i in range(len(self.trans_list)): # calculating interest for all transactions in the list
            tr = self.trans_list[i]

            if tr.type == 'Withdrawal':
                new_credit_line = old_credit_line - tr.amount #decrease credit limit
                old_balance = new_balance # save previous balance amount
                new_balance = old_balance + tr.amount # balance to be paid
                old_transaction_date = new_transaction_date #save the previous transaction date
                new_transaction_date = tr.day
                noOfDays = new_transaction_date - old_transaction_date# calculating the number of days for interest
                interest += noOfDays * (self.apr / 365) * old_balance


            elif tr.type == 'Payment':
                new_credit_line = old_credit_line + tr.amount # increase credit limit
                old_balance = new_balance
                new_balance = old_balance - tr.amount # balance to be paid
                old_transaction_date = new_transaction_date #save the previous transaction date
                new_transaction_date = tr.day
                noOfDays = new_transaction_date - old_transaction_date# calculating the number of days for interest
                interest += noOfDays * (self.apr / 365) * old_balance
            else:
                pass



        return interest + new_balance


if __name__ == "__main__":
    print "Welcome to Line of Credit Application"
    print "Enter the credit line and APR of the User"
    inp = raw_input().split()
    creditline = int(inp[0])
    apr = float(inp[1])/100
    scenario1 = LineOfCredit(creditline,apr)
    while(True):
        print "Do you want a record a new transaction(Y/N) "
        if raw_input() == 'Y':
            print "Record the Transaction in the following format "
            print "Amount(Any amount greater than 0) Day(0-30) Type of transaction(Withdrawal or Payment)"
            transc = raw_input().split()
            amt = int(transc[0])
            day = int(transc[1])
            type = transc[2]
            if amt > scenario1.credit_line:
                print "Amount is greater that credit line "
                break
            else:
                scenario1.trans_list.append(Transaction(amt,day,type))
        else:
            scenario1.trans_list.append(Transaction(0, 30, 'Withdrawal'))  # End of Month Transaction
            break

    print "The Pay off Amount of the User is $%.2f" % scenario1.calc_payoff_amount()


