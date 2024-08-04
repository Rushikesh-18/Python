import sqlite3

conn=sqlite3.connect('youtubedb.db')

cursor=conn.cursor()

cursor.execute('''
    create table if not exists youtubedb (
        id integer primary key,
        name text not null,
        time text not null
    )
''')

def list_all_videos():
    cursor.execute("select * from youtubedb")
    for row in cursor.fetchall():
        print(row)

def add_video():
    name=input("Enter your new video name: ")
    time=input("Enter your video time: ")
    cursor.execute("insert into youtubedb (name,time) values (?,?)",(name ,time))
    conn.commit()


def update_video():
    list_all_videos()
    which=int(input("Which video you want to update: "))
    name=input("Enter your video updated name: ")
    time=input("Enter your video updated time: ")
    cursor.execute("select MAX(id) from youtubedb")
    maxi=cursor.fetchall()
    till=int(maxi[0][0])
    if 1<=which<=till:
        cursor.execute("update youtubedb set name=? ,time=? where id=?",(name,time,which))
        conn.commit()
    else:
        print("Invalid video Selected")
    
def delete_video():
    list_all_videos()
    which=int(input("Which video you want to delete: "))
    cursor.execute("delete from youtubedb where id=?",(which,))
    conn.commit()



def main():
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
                list_all_videos()
            
            case '2':
                add_video()

            case '3':
                update_video()
            
            case '4':
                delete_video()

            case '5':
                run=False
            
            case _:
                print("Invalid Choice")

conn.close()

if __name__=="__main__":
    main()