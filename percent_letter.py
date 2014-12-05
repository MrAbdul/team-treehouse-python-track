# testing for int and float and also using try and except

user_string = input("what's your word? ")
user_num    = input("what's your number? ")

try: # this tells python to try to convert the input into int using the int function
  our_num = int(user_num)  
except: #if anything goes wrong with that let's say the user enter's a float the programm is going to go to the except block and try that insted 
  our_num = float(user_num) # convert the user number to float using the float function

if not '.' in user_num: # this if statment is going to test if . is not in the provided user number therefore the user didn't enter a float
  print(user_string[our_num]) # if not the programme os going to print the user_string coresbonding letter fore example if the string is Magic and the number is 3 it is going to print the 3rd element in the string which is the i because it starts counting on 0
else: #else if the user have entered a . therefore a float 
  ratio = round(len(user_string)*our_num) # new var that rounds the lentgh of the user string times the number this is assuming the number is less than one and more than zero to give us a location
  print(user_string[ratio]) #print the corresbonding letter index in the user string