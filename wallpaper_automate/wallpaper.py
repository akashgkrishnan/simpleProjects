import requests
import wget
import os

def set_wallpaper(file_name):
    wallpaper = file_name
    command = "/usr/bin/gsettings set org.gnome.desktop.background picture-uri /home/akash/Desktop/simpleProjects/wallpaper_automate/"+ wallpaper
    os.system(command) #runs the command in terminak for us

def get_wallpaper():
    ACCESS_KEY = '' #removed personal acces key for security stored the key in my local system
    base_url = 'https://api.unsplash.com/photos/random'+ '?client_id='+ ACCESS_KEY
    params = { 'orientation' : 'landscape', 'query' :'Cars'}
    res = requests.get(base_url, params).json() #uses the request module to send  a get request to specified URL in JSON format
    image_url = res['urls']['full']
    return wget.download(image_url) # this downloads from the image url we have extracted from the API and returns the file name
    #which we pass back to the call and then it used for calling the set wallpaper function 


def main():
    wallpaper = get_wallpaper()
    set_wallpaper(wallpaper)


if __name__ == "__main__":
    main()