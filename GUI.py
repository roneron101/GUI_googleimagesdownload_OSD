#------------------importing of libraries----------------
from google_images_download import google_images_download
import tkinter
from tkinter import *
from tkinter import messagebox
import os
import sys


#-----first feature//GUI
def Main(): #GUI
    global format_list
    global color_list
    global size_list
    global SearchChoice
    global Dict
    global MainCounter

    Main = Tk()
    Main.title("Google_image_download")
    Main.geometry('500x400')
    Main.resizable(width=True, height=True)
    Main.tk.call('tk', 'scaling', 1.4)

    
    #first row 
    EntryChoice = Label(Main, text="Keyword: ").grid(row=0, sticky=W, pady=5)
    entry_EntryChoice = Entry(Main,width=20)
    entry_EntryChoice.grid(row=0, column=1 , pady=5, sticky='ew')
    
    

    #third row
    SearchOption = Label(Main,text="Search by: ").grid(row=2, column=0,pady=5,sticky=W)    
    SearchChoice = ["entry","history"]                                  
    Choice = StringVar(Main)                                                                        
    Choice.set(SearchChoice[0])                                     
    dropdown_choice = OptionMenu(Main, Choice,*SearchChoice)    
    dropdown_choice.grid(row=2,column=1,sticky='ew')

    #fourth row
    label_limit = Label(Main, text="Limit: ").grid(row=3, sticky=W, pady=7)
    entry_limit = Entry(Main,width=40)
    entry_limit.grid(row=3, column=1 , pady=5, sticky='ew')
    limit = IntVar()
    limit.set(0)
    limitBox = Checkbutton(Main, text="limit Parameter", variable=limit,).grid(row=3, column=2)

    #fifth row
    label_format = Label(Main, text="Format: ").grid(row=4, sticky=W, pady=7)
    FormatChoice = StringVar(Main)
    FormatChoice.set(format_list[0])
    OptionMenu_format = OptionMenu(Main,FormatChoice,*format_list)
    OptionMenu_format.grid(row=4, column=1 , pady=5, sticky='ew')
    Format = IntVar()
    Format.set(0)
    FormatBox = Checkbutton(Main, text="Format Parameter", variable=Format,).grid(row=4, column=2)

    #sixth
    label_color = Label(Main, text="Color: ").grid(row=5, sticky=W, pady=7)
    ColorChoice = StringVar(Main)
    ColorChoice.set(color_list[0])
    OptionMenu_Color = OptionMenu(Main, ColorChoice, *color_list)
    OptionMenu_Color.grid(row=5, column=1 , pady=5, sticky='ew')
    Color = IntVar()
    Color.set(0)
    ColorBox = Checkbutton(Main, text="Color Parameter", variable=Color,).grid(row=5, column=2)

    #7th row
    label_size = Label(Main, text="Size: ").grid(row=6, sticky=W, pady= 7)
    SizeChoice = StringVar(Main)
    SizeChoice.set(size_list[0])
    OptionMenu_Choice = OptionMenu(Main, SizeChoice, *size_list)
    OptionMenu_Choice.grid(row=6, column=1 , pady=5, sticky='ew')
    Size = IntVar()
    Size.set(0)
    SizeBox = Checkbutton(Main, text="Size Parameter", variable=Size,).grid(row=6, column=2)


    def run():
        global Dict
        try:
            fetch_choice = Choice.get()
            keywords = ""
            if fetch_choice == SearchChoice[0]:
                entry = entry_EntryChoice.get().lower()
                keyword = entry
                if keyword =="":
                        messagebox.showinfo("no input for keyword")
                        return
                else:
                        Parameter_Dictionary("keywords",entry,Dict)
            else:
                        return
                    
            #store Limit
            LimitEntry = entry_limit.get()
            check_box_store(limit, "limit", LimitEntry, Dict)

            #Store format
            FormatEntry = FormatChoice.get()
            check_box_store(Format, "format", FormatEntry, Dict)
    
            #Store Color
            ColorEntry = ColorChoice.get()
            check_box_store(Color, "color", ColorEntry, Dict)
        
            #Store size
            SizeEntry = SizeChoice.get()
            check_box_store(Size, "size", SizeEntry, Dict)

            googleimage_download(Dict)
            
            
        except ValueError:
            messagebox.showinfo("wrong info")

    enterEntry = Button(Main, text= "Enter", command=run,bg="yellow")
    enterEntry.grid(row=7,column=1,columnspan=2,sticky='nesw')

        


def check_box_store(CheckBoxTrue,parameters,value,dictionary):
    if Box(CheckBoxTrue)==True:
        Parameter_Dictionary(parameters, value, dictionary)

#function to store the parameters and values in the dictionary
def Parameter_Dictionary(parameters, value, dictionary):
    dictionary[parameters] = value # parameter : value


#function to check if the tickbox is ticked
def Box(CheckBoxTrue):
    if CheckBoxTrue.get()==1:
        return True
    return False


def googleimage_download(dictionary):
    global Dict
    response =google_images_download.googleimagesdownload()
    arguments = Dict
    paths = response.download(arguments)



def existing_file(file_path):
    if os.path.isfile(file_path):
        return True
    return False

def file_check(txt_file):
    if  os.stat(txt_file).st_size==0:
        return True
    return False


    


Dict = {}
SearchChoice= []

format_list=["jpg", "gif", "png", "bmp", "svg", "webp", "ico"]
color_list= ["red", "orange", "yellow", "green", "teal", "blue", "purple", "pink", "white", "gray", "black"]
size_list= ["large","medium","icon",">400*300",">640*480",">800*600",">1024*768",">2MP",">4MP",">6MP",">8MP",">10MP",">12MP",">15MP",">20MP",">40MP",">70MP"]

    
Main()
