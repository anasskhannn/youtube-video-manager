import json

# File path
filename = 'youtube.txt'

# Function to load Data from file/server/db
def load_data():
    try:
        # open the file and return the data in json format
        with open(f"{filename}",'r') as file:
            return json.load(file)

    # If file not found
    except FileNotFoundError:
        return []
        
# Helper method to save files
def save_videos_helper(videos):
    with open(f"{filename}", "w") as file:
        # Dump the data of add_videos functions to file
        json.dump(videos, file)

# Function to Show all Videos
def list_all_videos(videos):
    """Why enumerate?
    enumerate() -> returns tuple of index and data of video.
    This will help in update and delete part of the Project"""
    print("\n")
    print("*" * 50) #just for decoration
    print("\n")
    for index, video in enumerate(videos, start=1):
        print(f"{index} :- {video["title"]}, Duration {video['duration']} \n")
    print("\n") 
    print("*" * 50) 
    print("\n") 

# function to add one video
def add_video(videos):
    name = input("Enter Video Title: ")
    time = input("Enter Video Duration: ")
    videos.append({"title": name, "duration": time})
    save_videos_helper(videos) #this will save the data
    
    
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
        
        choice = input("Enter Your Choice:")
        # print(videos) #to check what are in videos
        
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