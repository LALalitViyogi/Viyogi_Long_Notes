import tkinter as tk
from tkinter import ttk
from tkinter import font, colorchooser, filedialog, messagebox
import os 


main_application=tk.Tk()
main_application.geometry('1200x800')
main_application.title("Viyogi Long Notes")
main_application.wm_iconbitmap('icon.ico')

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

############# cascading all menus##########
main_menu.add_cascade(label='File', menu=files)
main_menu.add_cascade(label='Edit', menu=edit)
main_menu.add_cascade(label='View', menu=view)
main_menu.add_cascade(label='Color', menu=color_theme)


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


### align functionality --------------

#     $$$ ALIGN LEFT
def change_to_left():
    text_content = text_editor.get(1.0,'end')
    text_editor.tag_config('left', justify=tk.LEFT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'left')
align_left_btn.configure(command=change_to_left)


#    $$$ ALIGN CENTER $$$
def change_to_center():
    text_content = text_editor.get(1.0,'end')
    text_editor.tag_config('center', justify=tk.CENTER)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'center')
align_center_btn.configure(command=change_to_center)


#    $$$ ALIGN RIGHT 
def change_to_right():
    text_content = text_editor.get(1.0,'end')
    text_editor.tag_config('right', justify=tk.RIGHT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'right')
align_right_btn.configure(command=change_to_right)

text_editor.configure(font=('Arial',12))

#---------------------------&&&&&&&&&&&&---------- end text edit space -----------&&&&&&&&&&&&--------------#

############################################### status bar #####################################
status_bar = ttk.Label(main_application, text = 'Status Bar')
status_bar.pack(side=tk.BOTTOM)

text_changed = False 
def changed(event=None):
    global text_changed
    if text_editor.edit_modified():
        text_changed = True 
        words = len(text_editor.get(1.0, 'end-1c').split())
        characters = len(text_editor.get(1.0, 'end-1c'))
        status_bar.config(text=f'Characters : {characters} Words : {words}')
    
    # this is for adding '*' in the name of file in application title
    #to show that the FILE IS UN-SAVED.
    if text_editor.edit_modified() and file_url:
        main_application.title('*'+str(os.path.basename(file_url)))
    text_editor.edit_modified(False)

text_editor.bind('<<Modified>>', changed)
#---------------------------- end status bar --------------------#

############################ main menu back end ##########################

#main menu variables
file_url=""

########----------- New File Functionlity--------#######
def new_file(event=None):
    global file_url
    if file_url is not None:
        file_url=""
    text_editor.delete(1.0,tk.END)
    main_application.title("Untitled file")

## adding commands in file menu.
files.add_command(label="New",compound=tk.LEFT,image=new_icon, accelerator="CTRL+N", command=new_file)


###    OPEN FILE FUNCTIONALITY _______________
def open_file(event=None):
    global file_url
    file_url=filedialog.askopenfilename(initialdir=os.getcwd(), title='Open File', filetypes=(('Text File','*.txt'),('Python File','*.py'),('All Files','*.*')))
    try:
        with open(file_url,'r') as file_read:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(1.0, file_read.read())
    except FileNotFoundError :
        return
    except:
        return
    main_application.title(os.path.basename(file_url))

files.add_command(label="Open",compound=tk.LEFT, image=open_icon ,accelerator="CTRL+O", command=open_file)


### SAVE FILE FUNCTIONALITY _________________________

def save_file(event=None):
    global file_url
    try:
        if file_url :
            content=str(text_editor.get(1.0,tk.END))
            with open(file_url,'w',encoding='utf-8') as file_write:
                file_write.write(content)
        else:
            file_url=filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetypes=(('Text File','*.txt'),('Python File','*.py'),('All Files','*.*')))
            content2=text_editor.get(1.0,tk.END)
            file_url.write(content2)
            file_url.close()
        # this is remove '*' from the title name of file in application title
        main_application.title(os.path.basename(file_url))  
    except:
        return

files.add_command(label="Save",compound=tk.LEFT, image=save_icon ,accelerator="CTRL+S", command=save_file)

# Save As Functionality---------------------
def save_as_file(event=None):
    global file_url
    try:
        content=text_editor.get(1.0,tk.END)
        file_url=filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetypes=(('Text File','*.txt'),('Python File','*.py'),('All Files','*.*')))
        file_url.write(content)
        file_url.close()
    except :
        return

files.add_command(label="Save as",compound=tk.LEFT, image=save_as_icon ,accelerator="CTRL+SHIFT+S", command=save_as_file)

### Exit Functionality ---------
def exit_func(event=None):
    global file_url,text_changed
    try:
        if text_changed:
            popup = messagebox.askyesnocancel('WARNING','Do you want to save the file ?')
            if popup is True:
                if file_url:
                    content=text_editor.get(1.0,tk.END)
                    with open(file_url,'w',encoding='utf-8') as file_write:
                        file_write.write(content)
                        file_write.close()
                        main_application.destroy()
                else:
                    content2=str(text_editor.get(1.0,tk.END))
                    file_url=filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetypes=(('Text File','*.txt'),('Python File','*.py'),('All Files','*.*')))
                    file_url.write(content2)
                    file_url.close()
                    main_application.destroy()
            elif popup is False:
                main_application.destroy()
            else:
                return
        else:
            main_application.destroy()
    except :
        return

files.add_command(label="Exit",compound=tk.LEFT, image=exit_icon ,accelerator="CTRL+Q",command=exit_func)


#/////////// adding commands in  edit menu.
edit.add_command(label="Copy",compound=tk.LEFT,image=copy_icon ,accelerator="CTRL+C",command=lambda:text_editor.event_generate("<Control c>") )
edit.add_command(label="Cut",compound=tk.LEFT,image=cut_icon ,accelerator="CTRL+X", command=lambda:text_editor.event_generate("<Control x>"))
edit.add_command(label="Paste",compound=tk.LEFT,image=paste_icon ,accelerator="CTRL+V", command=lambda:text_editor.event_generate("<Control v>"))
edit.add_command(label="Clear all",compound=tk.LEFT,image=clear_all_icon ,accelerator="CTRL+ALT+X", command=lambda:text_editor.delete(1.0,tk.END))
def find_func(event=None):
    find_box=tk.Toplevel()
    find_box.geometry('450x250+500+200')
    find_box.title('Find & Replace')
    find_box.resizable(0,0)
    ##functions
    def findnow():
        word=find_entry.get()
        number_matches=0
        data=str(text_editor.get(1.0,tk.END))
        text_editor.tag_remove('match', '1.0', tk.END)
        if word:
            start='1.0'
            while True:
                start = text_editor.search(word, start, stopindex=tk.END)
                if not start:
                    break 
                end_pos = f'{start}+{len(word)}c'
                text_editor.tag_add('match', start, end_pos)
                number_matches += 1
                start =end_pos
                text_editor.tag_config('match', foreground='yellow', background='red')
                
               
    def replacenow():
        word = find_entry.get()
        replace_text = replace_entry.get()
        content = text_editor.get(1.0, tk.END)
        new_content = content.replace(word, replace_text)
        text_editor.delete(1.0, tk.END)
        text_editor.insert(1.0, new_content)
    #visualcreations
    #frame
    find_frames=ttk.LabelFrame(find_box,text='FIND/REPLACE')
    find_frames.pack(pady=20)

    #labels
    find_label=ttk.Label(find_frames,text='Find :')
    replace_label=ttk.Label(find_frames,text='Replace :')

    #entry box
    find_entry=ttk.Entry(find_frames,width=30)
    replace_entry=ttk.Entry(find_frames,width=30)

    #button
    find_button=ttk.Button(find_frames,text='Find',command=findnow)
    replace_button=ttk.Button(find_frames,text='Replace',command=replacenow)

    ####packing/griding
    #grid_labels
    find_label.grid(row=0,column=0,padx=4,pady=4)
    replace_label.grid(row=1,column=0,padx=4,pady=4)

    #grid_entrybox
    find_entry.grid(row=0,column=1,padx=4,pady=4)
    replace_entry.grid(row=1,column=1,padx=4,pady=4)

    #grid_button
    find_button.grid(row=2,column=0,padx=8,pady=4)
    replace_button.grid(row=2,column=1,padx=8,pady=4)

    find_box.mainloop()

edit.add_command(label="Find",compound=tk.LEFT,image=find_icon ,accelerator="CTRL+F", command=find_func)


#////////////// adding command in view menu.
show_statusbar = tk.BooleanVar()
show_statusbar.set(True)
show_toolbar = tk.BooleanVar()
show_toolbar.set(True)

def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar = False 
    else :
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP, fill=tk.X)
        text_editor.pack(fill=tk.BOTH, expand=True)
        status_bar.pack(side=tk.BOTTOM)
        show_toolbar = True

def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar = False
    else :
        status_bar.pack(side=tk.BOTTOM)
        show_statusbar = True

view.add_checkbutton(label='ToolBar',image=tool_bar_icon, onvalue=True, offvalue=0 , variable = show_toolbar , compound=tk.LEFT, command=hide_toolbar)
view.add_checkbutton(label='StatusBar',image=status_bar_icon,onvalue=1, offvalue=False,variable = show_statusbar ,compound=tk.LEFT,command=hide_statusbar)

#/////////////////adding command in color theme.
def change_theme():
    choosen_theme=theme_choice.get()
    color_tuple=color_dict.get(choosen_theme)
    fg_color , bg_color = color_tuple[0],color_tuple[1]
    text_editor.config(background=bg_color,fg=fg_color)
count = 0 
for i in color_dict:
    color_theme.add_radiobutton(label = i, image=color_icons[count], variable=theme_choice, compound=tk.LEFT,command=change_theme)
    count += 1

#---------------------------- end main menu back end --------------------#

### window protocol event handelling
main_application.protocol("WM_DELETE_WINDOW",exit_func)

main_application.config(menu=main_menu)

## Binding Keys

main_application.bind("<Control-n>", new_file)
main_application.bind("<Control-o>", open_file)
main_application.bind("<Control-s>", save_file)
main_application.bind("<Control-Alt-s>", save_as_file)
main_application.bind("<Control-q>", exit_func)
main_application.bind("<Control-f>", find_func)
## for enabling binding keys when Capslock is on.
main_application.bind("<Control-N>", new_file)
main_application.bind("<Control-O>", open_file)
main_application.bind("<Control-S>", save_file)
main_application.bind("<Control-Alt-S>", save_as_file)
main_application.bind("<Control-Q>", exit_func)
main_application.bind("<Control-F>", find_func)

main_application.mainloop()