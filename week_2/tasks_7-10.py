"""
TASK 7
addition_str is a string with a list of numbers separated by the + sign.
Write code that uses the accumulation pattern to take the sum of all of the numbers and assigns it to sum_val
(an integer). (You should use the .split("+") function to split by "+" and int() to cast to an integer).
"""


addition_str = "2+5+10+20"
sum_val = 0
addition_str = addition_str.split("+")
for i in addition_str:
    sum_val = sum_val + int(i)


"""
TASK 8
week_temps_f is a string with a list of fahrenheit temperatures separated by the , sign.
Write code that uses the accumulation pattern to compute the average (sum divided by number of items)
and assigns it to avg_temp. Do not hard code your answer (i.e., make your code compute both the sum or
the number of items in week_temps_f) (You should use the .split(",") function to split by "," and float()
to cast to a float).
"""


week_temps_f = "75.1,77.7,83.2,82.5,81.0,79.5,85.7"
week_temps_f = week_temps_f.split(",")
avg_temp = 0
for i in week_temps_f:
avg_temp = avg_temp + float(i)
avg_temp = avg_temp/len(week_temps_f)
print(avg_temp)


"""
TASK 9
Write code to create a list of numbers from 0 to 67 and assign that list to the variable nums.
Do not hard code the list.
"""


nums = []
nums = list(range(0, 68))
print(nums)


"""
TASK 10
Create an empty string and assign it to the variable lett.
Then using range, write code such that when your code is run, lett has 7 b’s ("bbbbbbb").
"""


lett = ""
for i in range(7):
    lett += "b"
print(lett)

