import requests

try:
    url = 'https://chisel.weirdgloop.org/gazproj/gazbot/os_dump.json'
    response = requests.get(url)
    items_data = response.json()

    with open('OSRS_Item_ID.txt', 'w', encoding='utf-8') as f:
        for item_id, item_info in items_data.items():
            if isinstance(item_info, dict) and 'id' in item_info and 'name' in item_info:
                f.write(f"{item_info['id']} {item_info['name']}\n")
            else:
                print(f"Skipping invalid item: {item_id} -> {item_info}")

except Exception as e:
    print(f"Error occurred: {str(e)}")
    print(f"Response status code: {response.status_code}")
    print(f"Response content type: {response.headers.get('content-type')}")
