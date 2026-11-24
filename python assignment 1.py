
string1 = "Hello "

name = input("Enter your Name: ")

string2 = string1 + name

print(string2)

string3 = ", welcome to Python programming"

final_string = string2 + string3

print(final_string)


print(final_string[0])

print(final_string[-1])

print(final_string[:5])

print(final_string[-11:])

print(final_string[::-1])

start = final_string.index("Python")
print(final_string[start:start+6])


strM = "Python beginner tutorial"

print(strM.upper())

print(strM.lower())

print(strM.capitalize())

print(strM.count('t'))

print(strM.replace("Python", "Machine Learning"))


tuple1 = (10, 20, 30)

tuple2 = (40, 50, 60)

t_combine = tuple1 + tuple2

print(t_combine)

print(t_combine * 3)

print(t_combine[2])

print(t_combine[:3])

print(t_combine[-3:])

