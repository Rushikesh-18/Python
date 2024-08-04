import requests
import pprint
import json

def fetch_random_user():
    url="https://api.freeapi.app/api/v1/public/randomusers?page=1&limit=10"
    response=requests.get(url)
    data=response.json()

    if data["success"] and "data" in data:
        value=[]
        users=data["data"]["data"]

        for user in users:
            username=user["login"]["username"]
            phone=user["phone"]
            namef=user["name"]["first"]
            namel=user["name"]["last"]
            fullname=(f"{namef} {namel}")
            country=user["location"]["country"]

            newentry={"Username": username ,"Fullname":fullname,"Phone":phone,"Country":country}
            value.append(newentry)
        return value
    else:
        raise Exception("Failed to fetch user data")
    
    


def main():
    try:
        final_data=fetch_random_user()
        # pp=pprint.PrettyPrinter(depth=4)
        # pp.pprint(final_data)
        print(json.dumps(final_data,indent=3,default=str))
      
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__=="__main__":
    main()