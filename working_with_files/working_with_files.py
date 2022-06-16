# with open("readme.txt", "w") as file:
#     file.write("first line\nsecond line\nthird line")

# with open("readme.txt", "r") as file:
#     for line in file.readlines():
#         print(line)

with open("readme.txt", "a") as file:
    file.write("\n")
    file.write("fourth line")
    file.write("\n")
    file.write("fifth line")
    file.write("\n")
