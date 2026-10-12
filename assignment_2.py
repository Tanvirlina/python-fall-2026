# ============================================================
# Assignment #2 - Python Data Types
# Topic: W3Schools > Python Data Types
#
# Instructions:
#  - Write your code under each question.
#  - For "PREDICT" questions, write your guess as a comment FIRST,
#    then run the code to check if you were right.
# ============================================================

stdCode = 34551001
stdName = 'Mohammed'
stdLastname = 'Ali'
stdMidterm = 80
stdFinal = 98.5
stdGPA = 3.7
stdActive = True
stdCourses = ['Python', 'Math', 'English']
stdBirthDate = (2001, 5, 14)
stdProfile = {'name': 'Mohammed', 'city': 'Alexandria'}
stdSkills = {'typing', 'Excel', 'typing'}
stdAdvisor = None

# 1. Use type() to print the data type of stdCode, stdName and stdFinal.
print(1)
print((type(stdCode)), (type(stdName)), (type(stdFinal)))


# 2. Print the data type of stdActive and stdAdvisor.
print(2)
print((type(stdActive)), (type(stdAdvisor)))


# 3. Print the data type of stdCourses, stdBirthDate, stdProfile and stdSkills.
print(3)
print((type(stdCourses)),(type(stdBirthDate)), (type(stdProfile)), (type(stdSkills)))


# 4. PREDICT: How many items will print(stdSkills) show? Why?
#    My guess:3 My guess was wrong.
#    Now i understood that same value will count as 1
print(4)
print(stdSkills)


# 5. Create a variable x = 5j and print its data type.
print(5)
x=5j
print(type(x))


# 6. Create a variable r = range(5). Print its data type,
#    then print list(r) to see the numbers inside it.

print(6)

r=range(5)
print(type(r))
print(list(r))


# 7. Convert stdMidterm to a float using float(). Print the new value and its type.
print(7)

stdMidterm = float(stdMidterm)
print(type(stdMidterm))


# 8. PREDICT: What will print(int(stdFinal)) show? Does it round up? Yes
#    My guess: 99  My guess was wrong. i though it will go to next for above .5 but it remain the previous full number
print(8)

print(int(stdFinal))


# 9. Convert stdCode to a string and print how many characters it has using len().
print(9)
stdCode = str(stdCode)
print (len(stdCode))


# 10. Create a frozenset from stdCourses and print its data type.
print(10)
stdCourses = frozenset(stdCourses)
print(type(stdCourses))


# 11. Create a variable msg = b"Hello" and print its data type.
print(11)
msg = b"Hello"
print(type(msg))


# 12. PREDICT the data type of each value below, then check with type():
#     10    10.0    "10"    [10]    (10,)    {10}    {'a': 10}    True
#     My guesses: Int, Float, String, List, Not sure, tuple, dict, boolean

print(12)

print(type(10))
print(type(10.0))
print(type("10"))
print(type([10]))
print(type((10,)))
print(type({10}))
print(type({'a':10}))
print(type(True))


# 13. PREDICT: What is the data type of stdMidterm + stdFinal?
#     My guess: Float

print(13)
print(type(stdMidterm+stdFinal))


# 14. PREDICT: What is the data type of stdMidterm / 2 ?  (Hint: 80 / 2 = 40 ... or is it?)
#     My guess: Int My guess was wrong but understood not that division result will be in float

print(14)

print(stdMidterm/2)

print(type(stdMidterm/2))


# 15. Fill in the blank so the output is <class 'tuple'>
#     print(type(_))

print(15)
print(type(("Tan", "Tin", "Tun")))


# BONUS: Why does print(type((1))) show <class 'int'> and not <class 'tuple'>?
#        Answer in a comment. Tuple take more than 1 string and comma, that is why it is showoing int