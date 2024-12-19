import sqlite3

# Establish Db connecttion
conn = sqlite3.connect("youtube_videos.db")

# Cursor to execute the queries
cur = conn.cursor()


# Create a table in database
cur.execute("""
            CREATE TABLE IF NOT EXISTS videos(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            time TEXT NOT NULL)
            """)

# Function to Show all Videos
def list_all_videos():
    print("*" * 50) #just for decoration
    print("\n")
    cur.execute("SELECT * FROM videos") #this will hold the result thus we have to loop it
    for row in cur.fetchall():
        print(row)
    print("\n") 
    print("*" * 50) 

# function to add one video
def add_video(name,time):
    cur.execute(" INSERT INTO videos (name,time) VALUES (?, ?)",(name, time))
    # Save this 
    conn.commit()
    
    
# Function to update detail of video
def update_details(video_id,new_name,new_time):
    cur.execute("UPDATE videos SET name = ?, time =? WHERE id= ?", (new_name, new_time, video_id))
    conn.commit()


# Function to Delete Video
def delete_video(video_id):
    cur.execute("DELETE FROM videos WHERE id=?", (video_id,))
    conn.commit()

  

def main():
    while True:
        print(" \n Youtube Video Manager | Choose Option From Below \n")
        print("1. List all Youtube Videos")
        print("2. Add a Youtube Video")
        print("3. Update the Video Details")
        print("4. Delete a Video")
        print("5. Exit")
        
        choice = input("Enter Your Choice: ")
        
        
        match choice:
            
            # List all Youtube Videos
            case "1":
                list_all_videos()
            
            # Add A new Youtube
            case "2":
                name = input("Enter the name of the Video: ")
                time = input("Enter the time of the Video: ")
                add_video(name,time) 
            
            # Update Details
            case "3":
                video_id = input("Enter the id of the Video: ") 
                new_name = input("Enter the name of the Video: ")
                new_time = input("Enter the time of the Video: ")
                update_details(video_id,new_name,new_time)
            
            # Delete Video
            case "4":
                video_id = input("Enter the id of the Video: ")
                delete_video(video_id) 
            
            # Exit Case
            case "5":
                break
            
            # Default Case 
            case _:
                print("Invalid Input")
                
    # Close the Database Connection After break
    conn.close()
            

if __name__ == "__main__":
    main()