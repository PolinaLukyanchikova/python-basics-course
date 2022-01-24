"""
TASK 7
For each string in the list words, find the number of characters in the string.
If the number of characters in the string is greater than 3, add 1 to the variable num_words so that num_words should
end up with the total number of words with more than 3 characters.
"""


words = ["water", "chair", "pen", "basket", "hi", "car"]
num_words = 0
for i in words:
    if len(i) > 3:
        num_words = num_words + 1


"""
TASK 8
For each word in words, add ‘d’ to the end of the word if the word ends in “e” to make it past tense.
Otherwise, add ‘ed’ to make it past tense. Save these past tense words to a list called past_tense.
"""


words = ["adopt", "bake", "beam", "confide", "grill", "plant", "time", "wave", "wish"]
past_tense = []
for i in words:
    if i[len(i) - 1] == "e":
        i = i + "d"
    else:
        i = i + "ed"
    past_tense.append(i)
print(past_tense)


"""
TASK 9
Write code to take ‘London’ out of the list trav_dest.
"""


trav_dest = ['Beirut', 'Milan', 'Pittsburgh', 'Buenos Aires', 'Nairobi', 'Kathmandu', 'Osaka', 'London', 'Melbourne']
trav_dest.pop(7)


"""
TASK 10
Write code to add ‘Guadalajara’ to the end of the list trav_dest using a list method.
"""


trav_dest = ['Beirut', 'Milan', 'Pittsburgh', 'Buenos Aires', 'Nairobi', 'Kathmandu', 'Osaka', 'Melbourne']
trav_dest.append('Guadalajara')


"""
TASK 11
For each word in the list verbs, add an -ing ending. Save this new list in a new list, ing.
"""


verbs = ["kayak", "cry", "walk", "eat", "drink", "fly"]
ing = []
for i in range(len(verbs)):
    ing.append(verbs[i] + "ing")
print(ing)


"""
TASK 12
Given the list of numbers, numbs, create a new list of those same numbers increased by 5.
Save this new list to the variable newlist.
"""


numbs = [5, 10, 15, 20, 25]
newlist = []
for i in numbs:
    x = i + 5
    newlist.append(x)
print(newlist)