from InstagramAPI import InstagramAPI
from toolname import tool
import time


print(f"{tool}")
print("Developed by Parker v.1\n")

username = input("Please enter your Instagram username: \n")
password = input("Please enter your password: \n")

api = InstagramAPI(username, password)
api.login()


with open("usernames.txt", "r") as f:
    usernames = f.readlines()

while True:
    for username in usernames:
        api.searchUsername(username.strip())
        result = api.LastJson
        is_available = result.get("status") == "ok" and not result.get("user")

        if is_available:
            print(f"{username} is available!")
            api.edit_profile(username=username)
            print(f"CLAIMED {username}")
            break

        else:
            print(f"{username} is NOT available")

    time.sleep(2)

    

   
    
