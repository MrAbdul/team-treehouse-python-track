#lists are just like arrays
#this is how we craete a list just create a variable then add an array to it
my_list = [1, 2.5, 'a']
# just like in c++ list's values have index number and it starts from zero eg: if i do my_list[1] this will call the elemnt with index number 1 which is 2.5
print (my_list[2])
#we can also change a value in one of the locations of the list by calling it and assigning another value to it
my_list[2] = 'b'
print (my_list)
# we can make lists from string by using the list() function
list('a')
# we can also check if something is in a list
hello_list = list('hello')
# to check we is the in command which will return true or false
print( 'e' in hello_list)
print( 'a' in hello_list)

my_sentence = "I'm funny and i'm ok! i sleep all night and work all day!"
# we can split strings using the split function
my_sentence_split = my_sentence.split()
print(my_sentence_split)
# we can join using the join function 
print(' '.join(my_sentence_split))