import tkinter
from tkinter import messagebox as tm
import time
from tkinter import ttk
import os
import win10toast
import pyautogui
from pynput import keyboard
from PIL import ImageTk ,Image
import random
from pytube import YouTube
from pytube import Playlist 
# import base64
from urllib.request import urlopen
from io import BytesIO
from threading import *
import tkinter.filedialog as file_browser
# import settings
import concurrent.futures

all_photoimage=[]

getting=False
def start_downlaod_thread():
	pass

	# image_byt = urlopen(thumbnamil_url).read()
	# background_image=ImageTk.PhotoImage(Image.open((image_byt)))
	# background_label = tkinter.Label(window ,image=baBytesIOckground_image)
	# background_label.place(x=1, y=1, relwidth=1, relheight=1)
	# pass



path_setter=''
default_quality=''

if 'settings_log.txt' in os.listdir():
	with open('settings_log.txt','r') as ss:
		content=ss.read()
	download_path_final=content
if 'settings_log.txt' not in os.listdir():
	download_path_final=os.getcwd()

# print(download_path_final)
download_quality_final='720p'
download_location_entry=''

def basic_widgits():
	global all_photoimage

	def download_path():
		global download_path_final, download_location_entry
		download_path_final=file_browser.askdirectory()
		download_location_entry.delete(0, tkinter.END)
		download_location_entry.insert(tkinter.END,download_path_final)


	def check_validity():
		global download_path_final
		if os.path.exists(download_location_entry.get())==False:
			download_location_entry.config(highlightbackground = "red")
			# path_setter.after(10,check_validity)
			tm.showwarning(title='Warning  !!!', message='path does not exist.')
		else:
			download_location_entry.configure(highlightbackground = "green")
			with open('settings_log.txt','w') as sa:
				sa.write(download_location_entry.get())
			update_settings()

	def update_settings():
		global download_path_final, download_quality_final
		download_path_final=download_location_entry.get()
		download_quality_final=default_quality.get()
		path_setter.destroy()
		print(download_path_final)
		print(download_quality_final)

	def cancel_command():
		global path_setter
		path_setter.destroy()

	def ask_settings():
		global path_setter, default_quality
		global download_path_final,download_location_entry
		global all_photoimage
		#fonts
		font1=('Lucida Bright', 16 )
		fonts=('Gabriola', 17,'bold' )

		#setting up the settings window
		path_setter=tkinter.Toplevel(window)
		path_setter.title("HappyYoutuber\\Settings ")
		# path_setter.geometry('1080x760')
		path_setter.geometry('985x630')
		# path_setter.iconbitmap(r"")

		#setting background
		os.chdir(r'F:\My_projects 27-08-19\youtube video downloader GUI')
		
		# image_resized=image.resize((1600,850), Image.ANTIALIAS)

		path_setter_background_label = tkinter.Label(path_setter ,image=all_photoimage[3])
		path_setter_background_label.place(relx=0, rely=0)
		# path_setter_background_label.pack(expand=1,fill='both')


		# default quality setting
		default_quality_list=['1080p','720p (recommended)','360p']
		default_quality = ttk.Combobox(path_setter ,values=default_quality_list, font=('Lucida Bright', 13 ))
		default_quality.place(y=77-27 ,x=765-10,width=165, height=43)
		default_quality.current(0)

		#geting the download path

		download_location_entry=tkinter.Entry(path_setter, font=('Gabriola', 13,'bold' ), justify='center', highlightthickness=1,background='#2f2f2f', fg='#e6e6e6',highlightbackground = "green")
		download_location_entry.insert(tkinter.END,download_path_final)
		# download_location_entry.configure()
		download_location_entry.place(y=179-27 ,x=180-10,width=765, height=43)

		browser=ttk.Button(path_setter,text='Browse', command=download_path)
		browser.place(y=245-27 ,x=450-10, height= 37, width=120)

		submit_btn=tkinter.Button(path_setter,text='  Apply Changes  ', bg='#1b1b1b' , fg='#e6e6e6', command=check_validity)
		submit_btn.place(y=550, x=824, height=37, width=120)

		cancel_btn=tkinter.Button(path_setter,text='  Cancel  ', bg='#e6e6e6' , fg='#1b1b1b', command=cancel_command)
		cancel_btn.place(y=550, x=700, height=37, width=120)



		path_setter.mainloop()


	def import_settings():
		ask_settings()
	

	getting=False
	def thumbnail(event):
		global getting, all_photoimage
		if 'https://www.youtube.com/watch?v=' in entry.get() and getting==False :
			getting=True
			loading=tkinter.Label(window, text= 'Parsing video information...', font= ('Gabriola', 20,'bold' ))
			# loading.place(rely=0.16 ,relx=0.07,relwidth=0.21, relheight=0.2)
			loading.pack()
			video_url=entry.get()
			yt=YouTube(video_url)
			thumbnail_url=yt.thumbnail_url
			print(thumbnail_url)

			resized_thumbnail_byt = urlopen(thumbnail_url).read()
			resized_thumbnail_byt=Image.open(BytesIO(resized_thumbnail_byt))
			# resized_thumbnail_byt=resized_thumbnail_byt.resize((100,100),Image.ANTIALIAS)
			thumbnail_image=ImageTk.PhotoImage(resized_thumbnail_byt)
			# thumbnail_image=ImageTk.PhotoImage(Image.open(r"F:\My_projects 27-08-19\youtube video downloader GUI\settings_back.jpg"))
			all_photoimage.append(thumbnail_image)
			print(len(all_photoimage))
			thumbnail_label = tkinter.Label(window ,image=all_photoimage[4])
			thumbnail_label.place(rely=0.16 ,relx=0.07,relwidth=0.18, relheight=0.2)
			loading.pack_forget()
			# print('yess')
		getting=False





	#setting up the window
	window=tkinter.Tk()
	screen_width, screen_height=window.winfo_screenwidth(),window.winfo_screenheight()
	# print(screen_width,'  ',screen_height)
	window.title("HappyYoutuber ")
	window.geometry(f'{screen_width}x{screen_height}')
	# window.iconbitmap(r"happyoutubers.ico")

	#fonts
	font1=('Lucida Bright', 14 )
	fonts=('Gabriola', 15,'bold' )



	#getting ready all images
	all_image_path=[r"F:\My_projects 27-08-19\youtube video downloader GUI\all required images\background.jpg",
		r"F:\My_projects 27-08-19\youtube video downloader GUI\all required images\background canvas edited.png",
		r"F:\My_projects 27-08-19\youtube video downloader GUI\all required images\settings page_ final.png",
		r"F:\My_projects 27-08-19\youtube video downloader GUI\all required images\settings.png",
	]

	all_photoimage=[]

	background_image=ImageTk.PhotoImage(Image.open(r'F:\My_projects 27-08-19\youtube video downloader GUI\backgrounds\bg.png'))
	all_photoimage.append(background_image)

	image=Image.open(r"F:\My_projects 27-08-19\youtube video downloader GUI\settings.png")
	resized_image=image.resize((60,60), Image.ANTIALIAS)
	settings_img = ImageTk.PhotoImage(resized_image)
	all_photoimage.append(settings_img)

	canvas_image=Image.open(r'F:\My_projects 27-08-19\youtube video downloader GUI\background canvas edited.png')
	resized_canvas_image=canvas_image.resize((1350+600,760+380), Image.ANTIALIAS)
	canvas_img_load = ImageTk.PhotoImage(resized_canvas_image)
	all_photoimage.append(canvas_img_load)

	image1=Image.open(r'F:\My_projects 27-08-19\youtube video downloader GUI\ezgif-3-0527232a44cf.gif')
	path_setter_background_image=ImageTk.PhotoImage(image1)
	all_photoimage.append(path_setter_background_image)

	
	






	#setting background image
	os.chdir(r'F:\My_projects 27-08-19\youtube video downloader GUI\backgrounds')
	
	background_label = tkinter.Label(window ,image=all_photoimage[0])
	background_label.place(x=1, y=1, relwidth=1, relheight=1)

	#setting entry box
	
	def clear_entry(event):
		entry.delete(0, tkinter.END)
	def fill_entry(event):
		global getting
		if entry.get()=='':
			entry.insert(tkinter.END,'Link Address...')
		if 'https://www.youtube.com/watch?v=' in entry.get() and getting==False:  
			thumbnail(event)

	entry= tkinter.Entry(window,bd=2, font=fonts, justify='center')
	entry.insert(tkinter.END,'Link Address...')
	entry.place(rely=0.076 ,relx=0.197,relwidth=0.5-0.027, relheight=0.065-0.0143)
	entry.bind("<Button-1>", clear_entry)
	entry.bind("<Leave>", fill_entry)
	entry.bind("<Control-v>", thumbnail)

	#setting download button
	download_btn=tkinter.Button(window, text='Download', bg='red',fg='white',font=('Gabriola', 18 ), relief='groove',border=4, command=start_downlaod_thread)
	download_btn.place(rely=0.085-0.007 ,relx=0.84,relwidth=0.1-0.017, relheight=0.065-0.018)

	#setting 'SETTINGS' button
	
	# bg='#d2231e'
	# relief='flat',
	settings= tkinter.Button (window, image=all_photoimage[1], font=('ISOCTEUR', 5), bg=None, command=import_settings)
	settings.place(rely=0.006 ,relx=0.004)
	#setting 'SETTINGS LABEL'
	settings_label=tkinter.Label(window, text=' Settings ', bg='gray', fg='white', font=('Gabriola', 19,'bold'))
	settings_label.place(rely=0.006 ,relx=0.0392)

	#setting combobox for quality selection
	qualty_list=['  Video Quality','1080p','720p (recommended)','360p']
	comboExample = ttk.Combobox(window ,values=qualty_list, font=font1)
	comboExample.place(rely=0.086-0.007 ,relx=0.7,relwidth=0.16-0.021, relheight=0.065-0.02)
	comboExample.current(0)

	#setting up canvas
	
	lower_canvas=tkinter.Canvas(window, height=400, width=400,border=-1)

	Canvas_Image = lower_canvas.create_image(940,100 ,image=all_photoimage[2], anchor='center')
	lower_canvas.place(rely=0.4 ,relx=0.01,relwidth=0.9799, relheight=0.587)


	#text label 'Downloading...' on canvas
	text='Downloads'
	downloading_label=tkinter.Label(lower_canvas,text=text,bg='#ba2737',fg='white', font=('Lucida Bright', 15, 'bold'))
	downloading_label.place(rely=0.03 ,relx=0.017)

	#text label 'Downloaded' on canvas
	# downloaded_label=tkinter.Label(lower_canvas,text='Previous Downloads',bg='#ab6867',fg='white', font=('Lucida Bright', 16, 'bold'))
	# downloaded_label.place(rely=0.7 ,relx=0.019)



	window.mainloop()

basic_widgits()