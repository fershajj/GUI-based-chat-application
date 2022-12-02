#import the necessary modules!
import random
import string

def main():
    #input the length of password
    length = 5                    

    #define data
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation
    #string.ascii_letters

    #combine the data
    all = lower + upper + num + symbols

    #use random 
    temp = random.sample(all,length)

    #create the password 
    password = "".join(temp)

    return password