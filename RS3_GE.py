import requests
import time

base_url = "http://services.runescape.com/m=itemdb_rs/api/catalogue/detail.json?"

def get_item_info(item_id):
    request_url = base_url + "item=" + str(item_id)
    response = requests.get(request_url)

    if response.status_code == 200:
        return response.json()
    else:
        return None

responses = []

for item_id in range(57395, 59000):
    time.sleep(3)
    print(f"Querying item ID {item_id}...")
    item_info = get_item_info(item_id)

    if item_info is not None:
        if "name" in item_info["item"]:
            responses.append({
                "item_id": item_id,
                "name": item_info["item"]["name"]
            })

            with open("RS3_Item_List.txt", "a") as f:
                f.write(str(item_id) + " " + item_info["item"]["name"] + "\n")
        else:
            print(f"Error: No name found for item ID {item_id}")
    else:
        print(f"Error: Failed to retrieve information for item ID {item_id}")



print(responses)
