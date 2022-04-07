whoryou=input("who are you?\n")
interest=input("out of 10 give the rate in number yourself how you are interested in this project \n")
#interest=int(interest)
try:
    if interest.isdigit():
        interest=int(interest)
except:
    print("run again and enter integer value out of 10 in second time")

def check_interest(interest):
    try:
        
        if interest>7:
            return 1
        else:
            return 0
    except:
        print("type")

check_y_n=check_interest(interest)
try:
    if check_y_n==0:
         print("greate")
    elif check_y_n==1:
        print("most welcome👍")
except:
    print("not to worry")