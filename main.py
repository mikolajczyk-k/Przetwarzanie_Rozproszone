import requests

url = "http://colormind.io/api/"

def get_random_colors():
    
    data = '{"model" : "default"}'
    
    try:
        response = requests.get(url, data=data)
        response.raise_for_status()
        colors = response.json()
        return colors
    except requests.exceptions.RequestException as e:
        print(f"Request failed. Code: {e}")
        return None
    
def post_colors():
    data = '{"model" : "default", "input": [[44, 43, 44], [90, 83, 82], "N", "N", "N"]}'

    try: 
        response = requests.post(url, data=data)
        response.raise_for_status()
        palette = response.json()
        return palette
    except requests.exceptions.RequestException as e:
        print(f"Request failed. Code: {e}")
        return None
    
def put_colors():
    data = '{"model" : "default", "input": [[55, 54, 34], [92, 85, 33], [12, 14, 20]]}'

    try: 
        response = requests.post(url, data=data)
        response.raise_for_status()
        palette = response.json()
        return palette
    except requests.exceptions.RequestException as e:
        print(f"Request failed. Code: {e}")
        return None
    
def delete_palette(palette_id):  #<--- niedozwolone, tylko dla przykładu
    delete_url = f"{url}{palette_id}/"

    try:
        response = requests.delete(delete_url)
        response.raise_for_status()
        print(f"Palette {palette_id} deleted successfully.")
    except requests.exceptions.RequestException as e:
        print(f"Failed to delete palette. Error: {e}")

    

if __name__ == "__main__":
    colors = get_random_colors()
    if colors is not None:
        print("Fetched colors:", colors)

    post_palette = post_colors()
    if post_palette:
        print("Created palette:", post_palette)

    put_palette = put_colors()
    if put_palette:
        print("Created palette:", put_palette)

    delete_palette('123456') # <--- niedozwolone 



