import sqlite3

con=sqlite3.connect('YouTubeVideos.db')
cur=con.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS videos(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )
""")


def list_all_videos():
    cur.execute("SELECT * FROM videos")
    print("*" * 50)
    for row in cur.fetchall():
        print(row)
    print("*" * 50)    

def add_video(name,time):
    cur.execute("INSERT INTO videos(name,time) VALUES (?,?)",(name,time))
    con.commit()

def update_video(video_id,new_name,new_time):
    cur.execute("UPDATE videos SET name=?,time=? WHERE id=?",(new_name,new_time,video_id))
    con.commit()

def delete_video(video_id):
    cur.execute("DELETE FROM videos WHERE id=?",(video_id,))
    con.commit()


def main():
    while True:
        print("\n YouTube Manager|Choose an Option")
        print("1.List all youtube videos")
        print("2.Add a youtube video")
        print("3.Update a youtube video details")
        print("4.Delete a youtube video")
        print("5.Exit from app")

        choice=input("Enter your choice:")

        if choice=='1':
            list_all_videos()

        elif choice=='2':
            name=input("Enter the video name:")
            time=input("Enter the video time:")
            add_video(name,time) 

        elif choice=='3':
            video_id=input("Enter video id to update:")
            name=input("Enter the video new name:")
            time=input("Enter the video  new time:")
            update_video(video_id,name,time) 

        elif choice=='4':
            video_id=input("Enter video id to delete:")
            delete_video(video_id) 

        elif choice=='5':
            break

        else:
            print("Invalid Choice")              
    
    con.close()

if __name__=="__main__":
    main()