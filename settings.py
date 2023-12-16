import tkinter
import pyautogui
from PIL import ImageTk ,Image
import os
from tkinter import ttk
import tkinter.filedialog as file_browser
from tkinter import messagebox as tm
import time

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

def download_path():
	global download_path_final, download_location_entry
	download_path_final=file_browser.askdirectory()
	download_location_entry.delete(0, tkinter.END)
	download_location_entry.insert(tkinter.END,download_path_final)


def check_validity():
	# global download_path_final
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
	# print(download_path_final)
	# print(download_quality_final)

def cancel_command():
	global path_setter
	path_setter.destroy()

def ask_settings():
	global path_setter, default_quality
	global download_path_final,download_location_entry
	#fonts
	font1=('Lucida Bright', 16 )
	fonts=('Gabriola', 17,'bold' )

	#setting up the settings window
	path_setter=tkinter.Tk()
	path_setter.title("HappyYoutuber\\Settings ")
	# path_setter.geometry('1080x760')
	path_setter.geometry('985x630')
	# path_setter.iconbitmap(r"")

	#setting background
	os.chdir(r'F:\My_projects 27-08-19\youtube video downloader GUI')
	image1=Image.open('ezgif-3-0527232a44cf.gif')
	# image_resized=image.resize((1600,850), Image.ANTIALIAS)
	path_setter_background_image=ImageTk.PhotoImage(image1)
	path_setter_background_label = tkinter.Label(path_setter ,image=path_setter_background_image)
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

# ask_settings()