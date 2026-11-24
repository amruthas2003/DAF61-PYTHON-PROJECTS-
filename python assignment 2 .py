# 1. List Creation

age_list = [24, 25, 26, 27, 28]

name_list = ["Anu", "Meenu", "Riya", "Amal", "Arun"]

print("Age List:", age_list)
print("Name List:", name_list)


# 2. List Operations / Modifications

# a. Append Yazhini to name_list
name_list.append("Yazhini")
print("After Append:", name_list)

# b. Insert 30 at index 2 in age_list
age_list.insert(2, 30)
print("After Insert:", age_list)

# c. Remove Yazhini from name_list
name_list.remove("Yazhini")
print("After Remove:", name_list)

# d. Pop the last element from age_list
age_list.pop()
print("After Pop:", age_list)

# e. Extend age_list with additional ages
age_list.extend([29, 30, 26])
print("After Extend:", age_list)

# f. Sort age_list in descending order
age_list.sort(reverse=True)
print("Descending Order:", age_list)

# g. Find maximum, minimum and sum
print("Maximum Age:", max(age_list))
print("Minimum Age:", min(age_list))
print("Sum of Ages:", sum(age_list))


# 3. Accessing List Elements

# a. Print the first element
print("First Element:", name_list[0])

# b. Print the last element
print("Last Element:", name_list[-1])

# c. Print elements from index 2 to index 4
print("Elements from index 2 to 4:", name_list[2:5])

# d. Print elements in reverse order
print("Reverse Order:", name_list[::-1])


# 4. Dictionary Creation

student_marks = {
    "Anu": 85,
    "Meenu": 90,
    "Riya": 78,
    "Amal": 88,
    "Arun": 75
}

print("Student Marks:", student_marks)


# b. Access and print a specific student's mark
print("Meenu's Mark:", student_marks["Meenu"])


# c. Add a new student Janani with mark 80
student_marks["Janani"] = 80
print("After Adding Janani:", student_marks)


# d. Update an older student's mark to 82
student_marks["Anu"] = 82
print("After Updating Anu:", student_marks)


# e. Print keys, values and items
print("Student Names:", student_marks.keys())
print("Student Marks:", student_marks.values())
print("Student Details:", student_marks.items())


# 5. Sets Operations

# a. Create a set with given values

my_set = {'a', 'e', 'i', 'o', 'u', 'a', 'a', 'i'}

print("My Set:", my_set)
print("Length of Set:", len(my_set))


# b. Attempt to change a set value

try:
    my_set[4] = 's'
except TypeError as e:
    print("Error:", e)
    print("Explanation: Sets do not support indexing or item assignment.")

# c. Create two sets

set1 = {1, 3, 5, 7, 9}

set2 = {2, 3, 5, 8, 10}

# d. Union and Intersection

print("Union:", set1.union(set2))

print("Intersection:", set1.intersection(set2))


# 6. Conditional Statements
# Performance Category Program

score = int(input("Enter your score (0 to 10): "))

if score < 0 or score > 10:
    print("Invalid score! Please enter a score between 0 and 10.")

elif score > 7:
    print("Above Average: Excellent performance! Keep it up.")

elif score >= 4:
    print("Average: Good effort! Keep practicing, there's room for improvement.")

else:
    print("Below Average: Need to improve your performance. Consistent practice will lead to better results.")
