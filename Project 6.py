#Kate Blunt
#COP2002
#Project 6


from decimal import Decimal



def title ():
    print("Welcome to the Interest Calculator")

def userInputLoan ():
    loanAmount = 0
    

    loanAmount = (input("Enter loan amount: "))
    loanAmount = loanAmount.replace("$","")
    loanAmount = loanAmount.replace(",","")
    if "K" in loanAmount:
        loanAmount = loanAmount.replace("K","")
        loanAmount = Decimal(loanAmount) * 1000

    #if "k" in loanAmount:
        #loanAmount = loanAmount.replace("k","")
        #loanAmount = Decimal(loanAmount) * 1000
        
    loanAmount = Decimal(loanAmount).quantize(Decimal("1.00"))
    return loanAmount

def userInputInterest():
    intAmount = 0
    intAmount = (input("Enter interest rate: "))
    intAmount = intAmount.replace("%","")
    intAmount = Decimal(intAmount).quantize(Decimal("1.000"))
    return intAmount

def formResults(loan, interest):
    interest = Decimal(interest/100)
   
    totalInterest = interest * loan
    #interest = interest.quantize(Decimal("1.00"))
    totalInterest = totalInterest.quantize(Decimal("1.00"))
    print()
    print("Loan amount:          ${:10,}".format(loan))
    print("Interest rate:        {:11,%}".format(interest))
    print("Interest amount:      ${:10,}".format(totalInterest))
    

    
    
def main():
    loan = 0;
    interest = 0
    
    title()

  
    choice = "y"
    while choice.lower() == "y":

        loan = userInputLoan()
        interest = userInputInterest()
        formResults(loan, interest)
        print()
        choice = input("Continue? (y/n): ")
        print()
        
    print("Thanks for using this program! Good bye!")





main()
