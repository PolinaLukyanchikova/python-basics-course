"""
TASK 1
Write a program that extracts the last three items in the list sports and assigns it to the variable last.
Make sure to write your code so that it works no matter how many items are in the list.
"""

sports = ['cricket', 'football', 'volleyball', 'baseball', 'softball', 'track and field', 'curling', 'ping pong', 'hockey']
last = sports[-3:]


"""
TASK 2
Write code that combines the following variables so that the sentence “You are doing a great job, keep it up!”
is assigned to the variable message. Do not edit the values assigned to by, az, io, or qy.
"""


by = "You are"
az = "doing a great "
io = "job"
qy = "keep it up!"
message = by+ " "+az+io+", " +qy


"""
TASK 3
Write one for loop to print out each character of the string my_str on a separate line.
"""


my_str = "MICHIGAN"
for i in my_str:
    print(i)


"""
TASK 4
Write one for loop to print out each element of the list several_things.
Then, write another for loop to print out the TYPE of each element of the list several_things.
To complete this problem you should have written two different for loops,
each of which iterates over the list several_things, but each of those 2 for loops should have a different result.
"""


several_things = ["hello", 2, 4, 6.0, 7.5, 234352354, "the end", "", 99]
for i in several_things:
    print(i)
for i in several_things:
    print(type(i))


"""
TASK 5
Write code that uses iteration to print out the length of each element of the list stored in str_list.
"""


str_list = ["hello", "", "goodbye", "wonderful", "I love Python"]
for i in str_list:
    print(len(i))


"""
TASK 6
Write code to count the number of characters in original_str using the accumulation pattern and assign the answer
to a variable num_chars. Do NOT use the len function to solve the problem 
(if you use it while you are working on this problem, comment it out afterward!)
"""


original_str = "The quick brown rhino jumped over the extremely lazy fox."
num_chars = 0
for i in original_str:
    num_chars += 1


