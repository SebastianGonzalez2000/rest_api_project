import requests

BASE = "http://127.0.0.1:5000/"


def request_video():
    video_id = input('enter the video ID: ')
    response = requests.get(BASE + 'video/' + video_id)
    print(response.json())

def publish_video():

    while(True):
        video_id = input('Video ID Number: ')
        name = input('Video Name: ')
        likes = input('How many likes does the video have? ')
        views = input('How many views does the video have? ')
        response = requests.put(BASE + 'video/' + video_id, {"name": name, "views": views, "likes": likes})
        print(response.json())

        if "message" not in response.json():
            break

        print('Failed to publish video. Read error message for more information and try again.')

def update_video():
    video_id = input('Video ID Number: ')

    while(True):

        print('\n\nWhat do you want to update? \n\n')
        print('Video Name -> 1\n')
        print('Video Likes -> 2\n')
        print('Video Views -> 3\n')
        print('Exit Update Menu -> 4\n')

        option = input('Enter your option: ')

        if option == '1':
            new_name = input('Input new name: ')
            response = requests.patch(BASE + "video/" + video_id, {"name": new_name})
            print(response.json())
        elif option == '2':
            new_likes = input('Input new amount of likes: ')
            response = requests.patch(BASE + "video/" + video_id, {"likes": new_likes})
            print(response.json())
        elif option == '3':
            new_views = input('Input new amount of views: ')
            response = requests.patch(BASE + "video/" + video_id, {"views": new_views})
            print(response.json())
        elif option == '4':
            break
        else:
            print('Invalid option...')


def main():
    print('Welcome to the Video Data Base.\n')

    while(True):
        print('Pick an option: \n\n')
        print('Request a video -> 1\n')
        print('Publish a video -> 2\n')
        print('Update a Video -> 3\n')
        print('Exit Menu -> 4\n\n')
        option = input('Enter your option: ')

        if option == '1':
            request_video()
        elif option == '2':
            publish_video()
        elif option == '3':
            update_video()
        elif option == '4':
            break
        else:
            print('Invalid option...')

if __name__ == '__main__':
    main()

