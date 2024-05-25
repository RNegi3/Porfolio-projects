import json

def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)  



def list_of_videos(videos):
    
    print("\n")
    print("*"* 70)

    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']}")

def add_videos(videos):
    video_name = input("Enter video name: ")
    video_time = input("Enter video time: ")
    videos.append({'name': video_name, 'time': video_time})
    print(videos)
    save_data_helper(videos)

def update_videos(videos):
    list_of_videos(videos)
    index = int(input("Enter the video number to update: "))
    if 1<= index <= len(videos):
        name = input("Enter the new video name: ")
        time = input("Enter the new video time: ")
        videos[index-1] = {'name': name, 'time': time}
        save_data_helper(videos)
    else:
        print("Entered invalid index.")

def delete_videos(videos):
    list_of_videos(videos)
    index = int(input("Enter the video number to delete: "))
    if 1<= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("Invalid video index selected")

def main():
    videos = load_data()
    while True:
        print("\n Youtube Manager | choose an option")
        print("1. List all youtube videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube video ")
        print("5. Exit the loop ")

        choice = input("Enter your choice: ")

        match choice:
            case '1':
                list_of_videos(videos)
            case '2':
                add_videos(videos)
            case '3':
                update_videos(videos)
            case '4':
                delete_videos(videos)
            case '5':
                break
            case _:
                print("Invalid Choice")
        

if __name__=='__main__':
    main()