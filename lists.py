# python lists.py
# Lists
names_list = ["pogs", "gingin", "ading"]
print("List", names_list)
print(names_list[0])
print(names_list[-1])

names_list.append("pedong")
print("Appended", names_list[-1])

more_names_list = ["kuya", "nanay", "tatay"]
names_list.extend(more_names_list)
print("Extended", names_list)

names_list.insert(0, "first")
print("Insert", names_list)

print("Sliced list", names_list[0:2])
print("Everything except the last two", names_list[:-2])

gingin_index = names_list.index("gingin")
print("Found index", gingin_index)

try:
    unknown_index = names_list.index("unknown")
except:
    unknown_index = "Nothing found"
print("Exception Handling", unknown_index)

# Loops
for name in names_list:
    print("For Loop", name)

current_index = 0
while current_index < len(names_list):
    print("While Loop", names_list[current_index])
    current_index += 1

sorted_names_list = sorted(names_list)
print("Sorted", sorted_names_list)
# names_list.sort()

# range(start, end, step)
for idx in range(len(sorted_names_list)):
    print("Range Sorted", sorted_names_list[idx])
