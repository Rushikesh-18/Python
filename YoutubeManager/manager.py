import json


def load_data():
    try:
        with open('youtube.txt','r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos,file)


def list_all_videos(videos):
    for index,video in enumerate(videos,start=1):
        print(f"{index}.{video}")

def add_video(videos):
    name=input("Enter your new video name: ")
    time=input("Enter your video time: ")
    videos.append({'name':name,'time':time})
    save_data_helper(videos)


def update_video(videos):
    list_all_videos(videos)
    which=int(input("Which video you want to update: "))
    name=input("Enter your video updated name: ")
    time=input("Enter your video updated time: ")
    if 1<=which<=len(videos):
        videos[which-1]={'name':name,'time':time}
    else:
        print("Invalid video Selected")
    
def delete_video(videos):
    list_all_videos(videos)
    which=int(input("Which video you want to delete: "))
    del videos[which-1]
   


def main():
    videos= load_data()
    run=True
    while(run):
        print("\n Youtube Manager")
        print("1. List all Youtube Videos")
        print("2. Add a Youtube Video")
        print("3. Update a youtube video details")
        print("4. Delete a Youtube video")
        print("5. Exit a App")
        choice=input("Enter your choice: ")

        match choice:
            case '1':
                list_all_videos(videos)
            
            case '2':
                add_video(videos)

            case '3':
                update_video(videos)
            
            case '4':
                delete_video(videos)

            case '5':
                run=False
            
            case _:
                print("Invalid Choice")


if __name__== "__main__":
    main()
