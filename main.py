import random
import string

def randomPassword(stringLength=10):
  LettersAndDigits = string.ascii_uppercase + string.digits
  return ''.join(random.choice(LettersAndDigits) for i in range(stringLength))

#Create 10 random passwords
print("1st Random Password is ", randomPassword())
print("2nd Random Password is ", randomPassword())
print("3rd Random Password is ", randomPassword())
print("4th Random Password is ", randomPassword())
print("5th Random Password is ", randomPassword())
print("6th Random Password is ", randomPassword())
print("7th Random Password is ", randomPassword())
print("8th Random Password is ", randomPassword())
print("9th Random Password is ", randomPassword())
print("10th Random Password is ", randomPassword())