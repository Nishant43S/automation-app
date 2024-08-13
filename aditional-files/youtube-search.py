import requests
import pywhatkit as kit

def check_internet_connection():
    try:
        # Attempt to make an HTTP GET request to a reliable site
        response = requests.get("https://www.google.com", timeout=5)
        # Check if the request was successful (status code 200)
        return response.status_code == 200
    except requests.ConnectionError:
        return False
    except requests.Timeout:
        return False
    

def search_yt(text_search)->str:
    try:
        kit.playonyt(text_search)
    except:
        print("Something went wrong...")

if __name__ == "__main__":
    if check_internet_connection():
        
        Search = input("Search: ")
        if Search == "":
            print("Write something")
        else:
            search_yt(text_search=Search)
    else:
        print("No internet connection.")
