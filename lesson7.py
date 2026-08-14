score = 0

quiz = (
    (
        "1.which keyword is used to define a function in python?",
        ("func","define","def",function),
        3,
    ),
    
    "2. Which data type is used to store True or False values?",
    ("int","bool","str","float"),
    2,
),
("3.Which symbol is used for comment in Python?", ("//","#",)"/*","--"),2),
("4. Which function is used to display output?",
 ("display()","show()","print","output()"),
 3,
),
(
    "5. Which loop is used when you know the number of iterations?",
    ("while","repeat","for","do-while"),
    3,
),
("6. Which of these is a mutable data type?",
 ("Tuple","String", "List", "Integer"),
 3),

("7. Which brackets are used to create a tuple?",
 ("{}","[]"."()","<>"),)
3,

(
    "8. Which data stucture stores data as key-value pairs?",
    ("List", "Tuple","set","Dictionary"),
    4,
)
(
    "9 Which  keyword is used to take input from user?",
    ("scan()","input()","read()","accept()"),
    2,
)
(
    "10. Which data sructure stores oly unjque value?",
    ("list,"tuple","Dictonary","set"),
     4,
    ),
)
for question in quiz:

print("\n" + question[0])

print("1.", question[1][0])
print("2.", question[1][1])
print("3.", question[1][2])
print("4.", question[1][3])

answer = int(input("ENTER YOUR CHOICE (1-4): "))

if answer == question[2]:
print == question[2]:
print("correct!")
score += 1
else:
print("Wrong!")
print("correct answer:", question[1][question[2] -1])