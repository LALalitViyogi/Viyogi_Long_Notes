import tkinter as tk
import pyttsx3
from tkinter import ttk
from tkinter import font, colorchooser, filedialog, messagebox
import os 


main_application=tk.Tk()
main_application.geometry('800x600')
main_application.title("Viyogi Long Notes")


################################################# main menu front end ###################################

main_menu= tk.Menu()


###### File menu ########
# //////Using icons///// right now its code is comment out.
new_icon=tk.PhotoImage(file="icons2/new.png")
open_icon=tk.PhotoImage(file="icons2/open.png")
save_icon=tk.PhotoImage(file="icons2/save.png")
save_as_icon=tk.PhotoImage(file="icons2/save_as.png")
exit_icon=tk.PhotoImage(file="icons2/exit.png")

files = tk.Menu(main_menu,tearoff=False)


###### Edit menu ########
# //////Using icons///// right now its code is comment out.
copy_icon=tk.PhotoImage(file="icons2/copy.png")
cut_icon=tk.PhotoImage(file="icons2/cut.png")
paste_icon=tk.PhotoImage(file="icons2/paste.png")
clear_all_icon=tk.PhotoImage(file="icons2/clear_all.png")
find_icon=tk.PhotoImage(file="icons2/find.png")

edit = tk.Menu(main_menu,tearoff=False)


###### View menu ########

# //////Using icons///// right now its code is comment out.
tool_bar_icon=tk.PhotoImage(file="icons2/tool_bar.png")
status_bar_icon=tk.PhotoImage(file="icons2/status_bar.png")

view = tk.Menu(main_menu,tearoff=False)

###### color menu ########
light_default_icon = tk.PhotoImage(file='icons2/light_default.png')
light_plus_icon = tk.PhotoImage(file='icons2/light_plus.png')
dark_icon = tk.PhotoImage(file='icons2/dark.png')
red_icon = tk.PhotoImage(file='icons2/red.png')
monokai_icon = tk.PhotoImage(file='icons2/monokai.png')
night_blue_icon = tk.PhotoImage(file='icons2/night_blue.png')

color_theme = tk.Menu(main_menu,tearoff=False)
theme_choice = tk.StringVar()
color_icons = (light_default_icon, light_plus_icon, dark_icon, red_icon, monokai_icon, night_blue_icon)

color_dict = {
    'Light Default ' : ('#000000', '#ffffff'),
    'Light Plus' : ('#474747', '#e0e0e0'),
    'Dark' : ('#c4c4c4', '#2d2d2d'),
    'Red' : ('#2d2d2d', '#ffe8e8'),
    'Monokai' : ('#d3b774', '#474747'),
    'Night Blue' :('#ededed', '#6b9dc2')
}

############# Speak MEnu ##########
speak_icon=tk.PhotoImage(file="icons2/speak.png")
speaked = tk.Menu(main_menu,tearoff=False)


############# cascading all menus##########
main_menu.add_cascade(label='File', menu=files)
main_menu.add_cascade(label='Edit', menu=edit)
main_menu.add_cascade(label='View', menu=view)
main_menu.add_cascade(label='Color', menu=color_theme)
main_menu.add_cascade(label='Speak it!', menu=speaked)


#----------------------------&&&&&&&------ end main menu front end ------&&&&&----------------------#


###################################################### toolbar #########################################

tool_bar = ttk.Label(main_application)
tool_bar.pack(side=tk.TOP,fill=tk.X)

#font Familly box------
font_tuple=tk.font.families()
font_family=tk.StringVar()
font_box=ttk.Combobox(tool_bar,width=30,textvariable=font_family,state='readonly')
font_box['values']=font_tuple
font_box.current(font_tuple.index('Arial'))
font_box.grid(row=0,column=0,padx=5)

#### size box---
size_var=tk.IntVar()
font_size=ttk.Combobox(tool_bar,textvariable=size_var)
font_size['values']=tuple(range(8,73,1))
font_size.current(4)
font_size.grid(row=0,column=1,padx=5)

#### bold button
bold_icon=tk.PhotoImage(file="icons2/bold.png")
bold_btn=ttk.Button(tool_bar,image=bold_icon)
bold_btn.grid(row=0,column=2,padx=5)

### italic button
italic_icon=tk.PhotoImage(file="icons2/italic.png")
italic_btn=ttk.Button(tool_bar,image=italic_icon)
italic_btn.grid(row=0,column=3,padx=5)

### underline button
underline_icon=tk.PhotoImage(file="icons2/underline.png")
underline_btn=ttk.Button(tool_bar,image=underline_icon)
underline_btn.grid(row=0,column=4,padx=5)

### font color button
font_color_icon=tk.PhotoImage(file="icons2/font_color.png")
font_color_btn=ttk.Button(tool_bar,image=font_color_icon)
font_color_btn.grid(row=0,column=5,padx=5)

### align left
align_left_icon=tk.PhotoImage(file="icons2/align_left.png")
align_left_btn=ttk.Button(tool_bar,image=align_left_icon)
align_left_btn.grid(row=0,column=6,padx=5)

### align center
align_center_icon=tk.PhotoImage(file="icons2/align_center.png")
align_center_btn=ttk.Button(tool_bar,image=align_center_icon)
align_center_btn.grid(row=0,column=7,padx=5)

### align right
align_right_icon=tk.PhotoImage(file="icons2/align_right.png")
align_right_btn=ttk.Button(tool_bar,image=align_right_icon)
align_right_btn.grid(row=0,column=8,padx=5)


####### speak button
speak_btn=ttk.Button(tool_bar,image=speak_icon)
speak_btn.grid(row=0,column=9, padx=5)

#------------------------------&&&&&&&&&&-- end tool bar ----&&&&&&&&&&&-------------------------------#


################################################ text edit space ####################################
text_editor=tk.Text(main_application)
text_editor.config(wrap='word',relief=tk.FLAT)

scroll_bar=tk.Scrollbar(main_application)
text_editor.focus_set()
scroll_bar.pack(fill=tk.Y, side=tk.RIGHT)
text_editor.pack(fill=tk.BOTH,expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)


###  basic font functionality ###
curr_font_family='Arial'
curr_font_size=24

def change_font_family(main_application):
    global curr_font_family
    curr_font_family = font_family.get()
    text_editor.configure(font=(curr_font_family,curr_font_size,))



def change_font_size(main_application):
    global curr_font_size
    curr_font_size=size_var.get()
    text_editor.configure(font=(curr_font_family,curr_font_size))

font_box.bind("<<ComboboxSelected>>", change_font_family)
font_size.bind("<<ComboboxSelected>>", change_font_size)
## --------------- basic font functionality done -----------------###

#### buttons functionality

## bold button 
def change_to_bold():
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight']=='normal':
        text_editor.configure(font=(curr_font_family,curr_font_size,'bold'))
    if text_property.actual()['weight']=='bold':
        text_editor.configure(font=(curr_font_family,curr_font_size,'normal'))
bold_btn.configure(command=change_to_bold)

## italic button
def change_to_italic():
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['slant']=='roman':
        text_editor.configure(font=(curr_font_family,curr_font_size,'italic'))
    if text_property.actual()['slant']=='italic':
        text_editor.configure(font=(curr_font_family,curr_font_size,'normal'))
italic_btn.configure(command=change_to_italic)

## underline button
def change_to_underline():
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['underline']== 0:
        text_editor.configure(font=(curr_font_family,curr_font_size,'underline'))
    if text_property.actual()['slant']==1:
        text_editor.configure(font=(curr_font_family,curr_font_size,'normal'))
underline_btn.configure(command=change_to_underline)

#### font color functionality

def change_font_color():
    color_var = tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])
font_color_btn.configure(command=change_font_color)

text_editor.configure(font=('Arial',24))

#---------------------------&&&&&&&&&&&&---------- end text edit space -----------&&&&&&&&&&&&--------------#

############################################### status bar #####################################
status_bar=ttk.Label(main_application, text ='Status Bar')
status_bar.pack(side=tk.BOTTOM)
#---------------------------- end status bar --------------------#

############################ main menu back end ##########################


## adding commands in file menu.
files.add_command(label="New",compound=tk.LEFT,image=new_icon, accelerator="CTRL+N")
files.add_command(label="Open",compound=tk.LEFT, image=open_icon ,accelerator="CTRL+O")
files.add_command(label="Save",compound=tk.LEFT, image=save_icon ,accelerator="CTRL+S")
files.add_command(label="Save as",compound=tk.LEFT, image=save_as_icon ,accelerator="CTRL+SHIFT+S")
files.add_command(label="Exit",compound=tk.LEFT, image=exit_icon ,accelerator="CTRL+Q")



#/////////// adding commands in  edit menu.
edit.add_command(label="Copy",compound=tk.LEFT,image=copy_icon ,accelerator="CTRL+C")
edit.add_command(label="Cut",compound=tk.LEFT,image=cut_icon ,accelerator="CTRL+X")
edit.add_command(label="Paste",compound=tk.LEFT,image=paste_icon ,accelerator="CTRL+V")
edit.add_command(label="Clear all",compound=tk.LEFT,image=clear_all_icon ,accelerator="CTRL+ALT+X")
edit.add_command(label="Find",compound=tk.LEFT,image=find_icon ,accelerator="CTRL+F")



#////////////// adding command in view menu.
view.add_checkbutton(label='ToolBar',image=tool_bar_icon, compound=tk.LEFT)
view.add_checkbutton(label='StatusBar',image=status_bar_icon, compound=tk.LEFT)

#/////////////////adding command in color theme.
count = 0 
for i in color_dict:
    color_theme.add_radiobutton(label = i, image=color_icons[count], variable=theme_choice, compound=tk.LEFT)
    count += 1


#//////////////// Speak Command.
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def Speaktext(audio):
 engine.say(audio)
 engine.runAndWait()
speaked.add_command(label='Speak',compound=tk.LEFT,command=Speaktext,accelerator='CTRL+T')
speak_btn.config(command=Speaktext)





#---------------------------- end main menu back end --------------------#
main_application.config(menu=main_menu)
main_application.mainloop()