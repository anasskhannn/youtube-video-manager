# YouTube Video Manager

## Project Description

YouTube Video Manager is a simple Python console application that allows users to manage a list of YouTube videos by storing their titles and durations. The application provides functionality to list, add, update, and delete video entries, with data persistently stored in a Sqlite Database.

## Features

- **List Videos**: View all stored videos with their titles and durations
- **Add Videos**: Add new videos to the collection
- **Update Videos**: Modify existing video details
- **Delete Videos**: Remove videos from the collection
- **Persistent Storage**: Saves data to a Sqlite Database for data retention between sessions

## Prerequisites

- Python 3.10 or higher (due to the use of match-case statement)
- No external libraries required (uses only standard Python libraries)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/anasskhannn/youtube-video-manager.git
   ```

2. Navigate to the project directory:
   ```bash
   cd youtube-video-manager
   ```

## Usage

Run the application using Python:

```bash
python youtube_video_manager.py
```

### Menu Options

- **1. List all Youtube Videos**: Displays all stored videos
- **2. Add a Youtube Video**: Allows adding a new video (title and duration)
- **3. Update the Video Details**: Modify an existing video's information
- **4. Delete a Video**: Remove a video from the list
- **5. Exit**: Close the application

### Example Interaction

```
 Youtube Video Manager | Choose Option From Below 

1. List all Youtube Videos
2. Add a Youtube Video
3. Update the Video Details
4. Delete a Video
5. Exit

Enter Your Choice: 2
Enter Video Title: Python Tutorial
Enter Video Duration: 2:30:45
```

## How It Works

- The application uses a `sqlite database` file to store videos.
- The application executes basic SQL Read and Update commands for Processing

## Error Handling

- If no database file exists, the application starts with creating one table in Database
- Invalid menu choices are handled with an "Invalid Input" message
- Attempting to update or delete with an invalid index shows an error message

## Customization

- You can easily modify the `conn` variable to change the database file name and path
- The code can be extended to add more features like sorting or searching videos

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


Project Link: [https://github.com/anasskhann/youtube-video-manager](https://github.com/anasskhannn/youtube-video-manager)