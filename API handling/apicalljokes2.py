import requests
import json

def give_joke():
    url="https://api.freeapi.app/api/v1/public/quotes?page=1&limit=10&query=human"
    response=requests.get(url)
    jokes=response.json()

    if jokes["success"] and "data" in jokes:
        value=[]
        joke=jokes["data"]["data"]

        for joking in joke:
            author=joking["author"]
            thought=joking["content"]
            value.append({"Author": author ,"Thought": thought})
        return value
    
    else:
        print("Not able to fetch content")
    





def main():
    try:
        final_data=give_joke()
        print(json.dumps(final_data,indent=3,default=str))
    except Exception as e:
        print(e)
    


if __name__=="__main__":
    main()








