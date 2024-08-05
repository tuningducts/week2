class BillCalc:
    def __init__(self,tip=0.18,tax=0.07 ):
        self.TIP_PERCENTAGE = tip
        self.TAX_PERCENTAGE = tax


    def get_check(self):
        check = input("Enter the cost of the meal: ")
        try:
            float(check)
        except:
            print("invalid input. Please enter a dollar amount X.XX")
            self.get_check(self) 
        check = round(float(check), 2)
        return check

    def get_tip(self,check):
        tip = round((check * self.TIP_PERCENTAGE),2)
        return tip 

    def get_tax(self,check):
        tax = round((check * self.TAX_PERCENTAGE),2)
        return tax

if __name__ == "__main__":
    
    bc = BillCalc()
    check = bc.get_check()
    tip = bc.get_tip(check)
    tax = bc.get_tax(check)
    #check = get_check()
    #tip = get_tip(TIP_PERCENTAGE, check)
    #tax = get_tax(TAX_PERCENTAGE, check)
    total = round(check + tip + tax,2)
    print("Check Total \n"
        f"Meal cost: ${check:.2f} \n"
        f"Tip amount: ${tip:.2f} \n"
        f"Tax: ${tax:.2f} \n"
        f"Total: ${total:.2f}")
