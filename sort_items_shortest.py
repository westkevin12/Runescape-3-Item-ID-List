# Read the file
with open('RS3_Item_ID.txt', 'r') as file:
    lines = file.readlines()

# Sort lines based on the length of the item name
# Each line is in format "ID Name", so we split by first space and get the length of the name part
sorted_lines = sorted(lines, key=lambda x: len(x.split(' ', 1)[1].strip()))

# Write sorted lines back to the file
with open('RS3ItemList.txt', 'w') as file:
    file.writelines(sorted_lines)
