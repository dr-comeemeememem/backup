# Date created: Thu Oct 21 15:34:26 2021
# Last date modified: Sat Jul 24 17:17:04 2021
def account_Numbers():
    account_Nums = [5658845, 4520125, 7895122, 8777541, 8451277, 1302850, 8080152, 4562555, 5552012, 5050552, 7825877, 1250255, 1005231, 6545231, 3852085, 7576651, 7881200, 4581002]
    num = int(input("Enter your account number: "))
    while(num not in account_Nums):
        num = int(input("The account number is not found in the database, please try again: "))

    if(num in account_Nums):
        return "The account number is found in the database"

if __name__ == '__main__':
    checkAccount = account_Numbers()
    print(checkAccount)
