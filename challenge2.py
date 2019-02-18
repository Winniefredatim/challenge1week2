
from datetime import datetime
#in order to get the current year, import datetime.
# create a function that holds the users age. 
def my_age():
    try:
        current_year=datetime.now().year
#create a variable that allows a user to enter his/her year of birth.
        inputyear=int(input("enter your year of Birth \n"))
#get current ade of the user.
        current_age = current_year - inputyear
        if(current_age <18):
                print("You are a minor")
        elif(current_age>=18 and current_age<36):
                print("You are a youth")
        else:
             print("You are an elder")
    except ValueError:
        print("not a valid year")
    
             

if __name__=="__main__":
    my_age()
