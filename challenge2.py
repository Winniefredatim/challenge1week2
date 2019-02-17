
from datetime import datetime
def ageBracket():
    try:
        current_year=datetime.now().year
        inputyear=int(input("Please enter your year of Birth \n"))
        current_age = current_year - inputyear
        if(current_age <18):
                print("You are a minor")
                #elif(person_age>=18):
                #print("You are a youth")
        else:
             print("You are an elder")
    except ValueError:
        print("This is not a valid year")

if __name__=="__main__":
    ageBracket()
