import datetime

class Purchase:
 
    
    purchase_date = ""
    purchase_card = ""
    amount_paid = ""
    card_amoumt = ""
    conv_fee = ""
    payment_status = ""
 
 

p1 = Purchase()

#ask user to enter date, YYYY-MM-DD
pDate = input("Enter the purchase date in YYYY-MM-DD format:\n"
year,  month, day = map(int, pDate.split('-'))
date = datetime.date(year, month, day)


class User_details:
    name = ""
    fullname = ""
    Phone_no = ""
    Password = ""
    country = ""
    addresss = ""

user1 = User_details()


class Card_deets:
    Amex = 
