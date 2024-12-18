import json

# Function to load Data from file/server/db
def load_data():
    try:
        # open the file and return the data in json format
        with open("youtube.txt",'r') as file:
            return json.load(file)

    # If file not found
    except FileNotFoundError:
        return []
        
# Function to Show all Videos
def list_all_videos(videos):
    pass

# function to add one video
def add_video(videos):
    pass

# Function to update detail of video
def update_details(videos):
    pass

# Function to Delete Video
def delete_video(videos):
    pass

# Wrapping in main to get to know starting of application, i.e from where our application is starting
def main():
    videos= load_data() # to load data from file/server/db
    # Asking for input
    while True:
        print(" \n Youtube Video Manager | Choose Option From Below \n")
        print("1. List all Youtube Videos")
        print("2. Add a Youtube Video")
        print("3. Update the Video Details")
        print("4. Delete a Video")
        print("5. Exit")
        
        choice = input("Enter Your Choice: ")
        
        # Check the choice
        
        match choice:
            
            # List all Youtube Videos
            case "1":
                list_all_videos(videos)
            
            # Add A new Youtube
            case "2":
                add_video(videos) #this will take list of videos and append new video in it
            
            # Update Details
            case "3":
                update_details(videos) #we will edit according to the index of that video
            
            # Delete Video
            case "4":
                delete_video(videos) #same concept of indexing
            
            case "5":
                break
            
            # Default Case 
            case _:
                print("Invalid Input")
            

if __name__ == "__main__":
    main()