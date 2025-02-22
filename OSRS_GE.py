import requests
import time

base_url = "http://secure.runescape.com/m=itemdb_oldschool/api/catalogue/detail.json?"


def get_item_info(item_id):
    request_url = base_url + "item=" + str(item_id)

    response = requests.get(request_url)

    try:
        data = response.json()
        return data
    except:
        return None

responses = []

with open("OSRS_Item_List.txt", "a") as f:
    for item_id in range(25051, 26200):

        time.sleep(0.75)
        print(f"Querying item ID {item_id}...")
        item_info = get_item_info(item_id)

        if item_info is not None:
            if "name" in item_info["item"]:
                responses.append({
                    "item_id": item_id,
                    "name": item_info["item"]["name"]
                })
                f.write(str(item_id) + " " + item_info["item"]["name"] + "\n")
                f.flush()
            else:
                print(f"Error: No name found for item ID {item_id}")
        else:
            print(f"Error: Failed to retrieve information for item ID {item_id}")

print(responses)
