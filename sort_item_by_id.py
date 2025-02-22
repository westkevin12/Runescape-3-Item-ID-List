# Read items from source file
items = []
with open('RS3_Item_ID.txt', 'r') as file:
    for line in file:
        # Split line into ID and name
        item_id = int(line.split(' ', 1)[0])  # Convert ID to integer for proper sorting
        item_name = line.split(' ', 1)[1].strip()  # Get name and remove whitespace
        items.append((item_id, item_name))

# Sort items by ID
items.sort(key=lambda x: x[0])

# Write sorted items to destination file
with open('RS3_Item_ID.txt', 'w') as file:
    for item_id, item_name in items:
        file.write(f"{item_id} {item_name}\n")
