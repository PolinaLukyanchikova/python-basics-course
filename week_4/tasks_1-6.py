
"""
TASK 1
Below are a set of scores that students have received in the past semester.
Write code to determine how many are 90 or above and assign that result to the value a_scores.
"""


scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"
scores_split = scores.split(" ")
a_scores = 0
for grade in scores_split:
    grade = float(grade)
    if grade >= 90:
        a_scores += 1


"""
TASK 2
For each character in the string saved in ael, append that character to a list that should be saved in a variable app.
"""


ael = "python!"
app = []
for item in ael:
    app.append(item)
print(app)


"""
TASK 3
For each string in wrds, add ‘ed’ to the end of the word (to make the word past tense).
Save these past tense words to a list called past_wrds.
"""


wrds = ["end", 'work', "play", "start", "walk", "look", "open", "rain", "learn", "clean"]
past_wrds = []
for item in wrds:
    past_wrds.append(item + "ed")


"""
TASK 4
Assign an empty string to the variable output. Using the range function,
write code to make it so that the variable output has 35 a s inside it (like "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
"""


output = ""
for i in range(35):
    output += "a"


"""
TASK 5
For each character in the string already saved in the variable str1, add each character to a list called chars.
"""


str1 = "I love python"
chars = []
for i in str1:
    chars.append(i)


"""
TASK 6
Write code to add ‘horseback riding’ to the third position (i.e., right before volleyball) in the list sports.
"""


sports = ['cricket', 'football', 'volleyball', 'baseball', 'softball', 'track and field', 'curling', 'ping pong', 'hockey']
sports.insert(3,'horseback riding')
print(sports)