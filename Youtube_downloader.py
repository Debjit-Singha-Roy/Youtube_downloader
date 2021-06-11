from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube
folder_name = " "
def folder_location():
    global folder_name 
    folder_name= filedialog.askdirectory()
    if(len(folder_name)>1):
        location.config(text=folder_name,fg="green",font=("jost",8))

def video_download():
    choice=ytdchoices.get()
    url=entryfield.get()
    if(len(url)>1):
        yt=YouTube(url)
        if(choice==choices[0]):
            select=yt.streams.filter(progressive=True,file_extension="mp4").order_by("resolution").desc()[0]
        elif(choice==choices[1]):
            select=yt.streams.filter(only_audio=True).first()
    select.download(folder_name)
    ytddownload.config(text="Download Completed..",fg="green",font=("jost",8))



root=Tk()
root.title("YouTube Video Downloader")
root.geometry("350x200")
root.columnconfigure(0,weight=1)
#url=input("Enter the Video URL: ")
#my_video=YouTube(url)
#print(f"The Title of the video is : {my_video.title}")
link=Label(root,text="Enter The URL of the Video",font=("jost",12)) #top heading
link.grid()
#entry field for the url
entryurl=StringVar()
entryfield=Entry(root,textvariable=entryurl,width=50)
entryfield.grid()
#select the destination folder
select=Label(root,text="Select the folder",font=("jost",10))
select.grid()
destfield=Button(root,bg="black",fg="white",text="Choose Folder",command=folder_location)
destfield.grid()
location=Label(root,text="")
location.grid()
#quality
quality=Label(root,text="Select the Video Quality",font=("jost",10))
quality.grid()
choices=["mp4","mp3"]
ytdchoices=ttk.Combobox(root,values=choices)
ytdchoices.grid()
downloadbttn=Button(root,bg="black",fg="white",text="Download",command=video_download)
downloadbttn.grid()
ytddownload=Label(root,text="")
ytddownload.grid()
root.mainloop()