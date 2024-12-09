import string
import os
script_dir = os.path.dirname(__file__)  
file_path = os.path.join(script_dir, 'common.txt')
password=input("Enter your password:")

upper_case=any([1 if c in string.ascii_uppercase else 0 for c in password])
lower_case=any([1 if c in string.ascii_lowercase else 0 for c in password])
special=any([1 if c in string.punctuation else 0 for c in password])
digits=any([1 if c in string.digits else 0 for c in password])

characters=[upper_case,lower_case, special, digits]
length=len(password)

try:
    with open(file_path, 'r') as f:
        common = f.read().splitlines()
except FileNotFoundError:
    print(f"Error: 'common.txt' not found in {script_dir}.")
    exit()


if password in common:
    print("Password was found in a common list. Score:0/7")
    exit()

score=0
if length>8:
    score+=1
if length>12:
    score+=1
if length>16:
    score+=1
if length>20:
    score+=1
print(f"Password Strength is  {str(length)}, adding {str(score)} points!")

if sum(characters)>1:
    score+=1
if sum(characters)>2:
    score+=1
if sum(characters)>3:
    score+=1
print(f"Password has  {str(sum(characters))} different character types adding {str(sum(characters)-1)}")

if score<4:
    print(f"Password is weak. Score: {str(score)}/7")
elif score==4:
    print(f"Password is okay. Score: {str(score)}/7")
elif 4<score<6:
    print(f"Password is good. Score: {str(score)}/7")
elif score>6:
    print(f"Password is strong. Score: {str(score)}/7")
