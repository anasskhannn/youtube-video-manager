import sqlite3

# Establish Db connecttion
conn = sqlite3.connect("youtube_videos.db")

# Cursor to execute the queries
cur = conn.cursor()


# Create a table in database
cur.execute("""
            CREATE TABLE IF NOT EXIST videos
            id INT PRIMARY KEY,
            name TEXT NOT NULL,
            time TEXT NOT NULL
            """)

# Function to Show all Videos
def list_all_videos(videos):
    print("\n")
    print("*" * 50) #just for decoration
    print("\n")


    print("\n") 
    print("*" * 50) 
    print("\n") 

# function to add one video
def add_video(videos):
    pass
    
    
# Function to update detail of video
def update_details(videos):
    pass



# Function to Delete Video
def delete_video():
    pass

  

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
                add_video() #this will take list of videos and append new video in it
            
            # Update Details
            case "3":
                update_details() #we will edit according to the index of that video
            
            # Delete Video
            case "4":
                delete_video() #same concept of indexing
            
            case "5":
                break
            
            # Default Case 
            case _:
                print("Invalid Input")
                
    # Close the Database Connection After break
    conn.close()
            

if __name__ == "__main__":
    main()