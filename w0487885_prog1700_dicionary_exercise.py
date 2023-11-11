# empty dictionary
student_scores = {
    "Alice": 90,
    "Kane": 85,
    "Charlie": 78,
    "Vincent": 92,
    "Eve": 88,
}

# add names and scores to dictionary
thisdict = { 
    "Alice": 90,
    "Kane": 85,
    "Charlie": 78,
    "Vincent": 92,
    "Eve": 88,
}
print(thisdict)

# calculate average score
student_scores = {
    "Alice": 90,
    "Kane": 85,
    "Charlie": 78,
    "Vincent": 92,
    "Eve": 88,
}
# average from least to greatest
student_scores = {
    "Charlie": 78,
    "Kane": 85,
    "Eve": 88,
    "Alice": 90,
    "Vincent": 92,
}
print("78, 85, 88, 90, 92")

# ping names
name = input("Charlie")
name = input("Kane")
name = input("Eve")
name = input("Alice")
name = input("Vincent")

# update score
def showScore():
    score = 78
    score = score + 2
    print('New score is 80')

# remove student 
thisdict = {
    "Charlie": 78,
}
del thisdict
print(thisdict) #error because "thisdict" shouldnt exist


