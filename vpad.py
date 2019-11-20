import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, font, colorchooser, filedialog
import os

win = tk.Tk()
win.geometry('1200x800')
win.title('V-Pad Text Editior')
win.wm_iconbitmap('icon.ico')
############################################################# main menu ##########################################
main_menu = tk.Menu(win)

####################################################### file menu ##############################################
#######################file menu icons #############################
new_icon = tk.PhotoImage(file = 'icons2/new.png')
open_icon = tk.PhotoImage(file = 'icons2/open.png')
save_icon = tk.PhotoImage(file = 'icons2/save.png')
save_as_icon = tk.PhotoImage(file = 'icons2/save_as.png')
exit_icon = tk.PhotoImage(file = 'icons2/exit.png')

file_menu = tk.Menu(main_menu, tearoff = 0)

main_menu.add_cascade(label = 'File', menu = file_menu)

######################################################### Edit Menu ##############################################
################### edit icons ################
copy_icon = tk.PhotoImage(file = 'icons2/copy.png')
paste_icon = tk.PhotoImage(file = 'icons2/paste.png')
cut_icon = tk.PhotoImage(file = 'icons2/cut.png')
clear_all_icon = tk.PhotoImage(file = 'icons2/clear_all.png')
find_icon = tk.PhotoImage(file = 'icons2/find.png')

edit_menu = tk.Menu(main_menu, tearoff = 0)

main_menu.add_cascade(label = 'Edit', menu = edit_menu)

####################################################### View menu ############################################
tool_bar_icon = tk.PhotoImage(file = 'icons2/tool_bar.png')
status_bar_icon = tk.PhotoImage(file = 'icons2/status_bar.png')

view_menu = tk.Menu(main_menu, tearoff = 0)

main_menu.add_cascade(label = 'View', menu = view_menu)

##################################################### Color Theme ########################################
##############color theme icon ###########################

light_default_icon = tk.PhotoImage(file = 'icons2/light_default.png')
light_plus_icon = tk.PhotoImage(file = 'icons2/light_plus.png')
dark_icon = tk.PhotoImage(file = 'icons2/dark.png')
red_icon = tk.PhotoImage(file = 'icons2/red.png')
monokai_icon = tk.PhotoImage(file = 'icons2/monokai.png')
night_blue_icon = tk.PhotoImage(file = 'icons2/night_blue.png')

color_menu = tk.Menu(main_menu, tearoff = 0)

theme_choice = tk.StringVar()
color_icons = (light_default_icon, light_plus_icon, dark_icon, red_icon, monokai_icon, night_blue_icon)

color_dict = {
    'Light Default ' : ('#000000', '#ffffff'),
    'Light Plus' : ('#423a3a', '#f0dddd'),
    'Dark' : ('#c4c4c4', '#2d2d2d'),
    'Red' : ('#2d2d2d', '#ffe8e8'),
    'Monokai' : ('#d3b774', '#474747'),
    'Night Blue' :('#ededed', '#6b9dc2')
}
main_menu.add_cascade(label = 'Color Theme', menu = color_menu)

##################################################### TOOLBAR ###########################################
tool_bar = ttk.Label(win)
tool_bar.pack(side = tk.TOP , fill = tk.X)
############## Font box ##############
font_tuples = tk.font.families()
font_family = tk.StringVar()
font_box = ttk.Combobox(tool_bar, width = 30, textvariable = font_family, state='readonly')

font_box['values'] = font_tuples
font_box.current(font_tuples.index('Arial'))
font_box.grid(row = 0, column = 0, padx = 5)

######################## SIZE BOX ##################

size_var = tk.IntVar()
font_size = ttk.Combobox(tool_bar, width = 14, textvariable = size_var)

font_size['values'] = tuple(range(8,81,2))
font_size.current(2)
font_size.grid(row = 0 , column = 1, padx = 5)

#################### BOLD BUTTON ###############

bold_icon = tk.PhotoImage(file = 'icons2/bold.png')
bold_btn = ttk.Button(tool_bar, image = bold_icon)
bold_btn.grid(row = 0 , column = 2, padx = 5)

#####################ITALIC BUTTON ########################

italic_icon = tk.PhotoImage(file = 'icons2/italic.png')
italic_btn = ttk.Button(tool_bar, image = italic_icon)
italic_btn.grid(row = 0, column = 3, padx = 5)

################### UNDERLINE BUTTON #########################

underline_icon = tk.PhotoImage(file = 'icons2/underline.png')
underline_btn = ttk.Button(tool_bar, image = underline_icon)
underline_btn.grid(row = 0, column =4, padx = 5)

####################### FONT COLOUR CHOOSER #####################
font_color_icon = tk.PhotoImage(file = 'icons2/font_color.png')
font_color_btn = ttk.Button(tool_bar, image = font_color_icon)
font_color_btn.grid(row = 0, column = 5, padx = 5)

################## Align Left ########################

align_left_icon = tk.PhotoImage(file = 'icons2/align_left.png')
align_left_btn = ttk.Button(tool_bar, image = align_left_icon)
align_left_btn.grid(row = 0, column = 6, padx = 5)

###################### Align Center ##########################

align_centre_icon = tk.PhotoImage(file = 'icons2/align_center.png')
align_centre_btn = ttk.Button(tool_bar, image = align_centre_icon)
align_centre_btn.grid(row = 0, column = 7, padx = 5)

########################## Align Left ######################

align_right_icon = tk.PhotoImage(file = 'icons2/align_right.png')
align_right_btn = ttk.Button(tool_bar, image = align_right_icon)
align_right_btn.grid(row = 0, column = 8, padx = 5)


#################################################### TEXT EDITOR ########################################

text_editor = tk.Text(win)
text_editor.config(wrap = 'word', relief = tk.FLAT)

scroll_bar = tk.Scrollbar(win)
text_editor.focus_set()

scroll_bar.pack(side = tk.RIGHT, fill = tk.Y)
text_editor.pack(fill = tk.BOTH, expand = True)

scroll_bar.config(command = text_editor.yview)
text_editor.config(yscrollcommand = scroll_bar.set)

################ FONT FAMILY AND FONT FUNCTIONALITY ################

current_font_family = 'Arial' #global variable
current_font_size = 12 #global variable

def change_font(envent=None):
    global current_font_family
    current_font_family = font_family.get()
    text_editor.configure(font=(current_font_family, current_font_size))

def change_fontsize(event=None):
    global current_font_size
    current_font_size = size_var.get()
    text_editor.configure(font=(current_font_family, current_font_size))

font_box.bind("<<ComboboxSelected>>", change_font)
font_size.bind("<<ComboboxSelected>>", change_fontsize)


####################### BUTTON FUNCTION ####################
############## Bold Button Function ###############

def change_bold():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight'] == 'normal':
        text_editor.configure(font = (current_font_family, current_font_size, 'bold'))
    
    if text_property.actual()['weight'] == 'bold' :
        text_editor.configure(font = (current_font_family, current_font_size, 'normal'))

bold_btn.configure(command = change_bold)

############## Italic Button Function ##############

def change_italic():
    text_property = tk.font.Font(font = text_editor['font'])
    if text_property.actual()['slant'] == 'roman':
        text_editor.configure(font=(current_font_family, current_font_size, 'italic'))
    
    if text_property.actual()['slant'] == 'italic' :
        text_editor.configure(font = (current_font_family, current_font_size, 'roman'))

italic_btn.configure(command = change_italic)

###################### Underline Button Function ###############

def underline():
    text_property = tk.font.Font(font = text_editor['font'])
    if text_property.actual()['underline'] == 0:
        text_editor.configure(font =(current_font_family, current_font_size, 'underline'))

    if text_property.actual()['underline'] == 1:
        text_editor.configure(font =(current_font_family, current_font_size, 'normal'))

underline_btn.configure(command = underline)

########################### Color Chooser Function ####################
def change_fontcolor():
    color_var = tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])

font_color_btn.configure(command = change_fontcolor)

############################ Align Left function ################
def align_left():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('left', justify = tk.LEFT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'left')

align_left_btn.configure(command = align_left)

############################## Align Center Function ################

def align_center():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('center', justify = tk.CENTER)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'center')

align_centre_btn.configure(command = align_center)

################################### Align Right Function ####################

def align_right():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('right', justify = tk.RIGHT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'right')

align_right_btn.configure(command = align_right)





text_editor.configure(font=('Arial', 12))

##################################################### MAIN STATUS BAR ##########################################
status_bar = ttk.Label(win, text = 'Status Bar')
status_bar.pack(side = tk.BOTTOM)

text_changed = False

def changed(event = None):
    global text_changed
    if text_editor.edit_modified():
        text_changed = True
        words = len(text_editor.get(1.0, 'end-1c').split())
        characters = len(text_editor.get(1.0, 'end-1c'))
        status_bar.config(text = f"Character {characters} : word {words}")
    text_editor.edit_modified(False)
    
text_editor.bind("<<Modified>>", changed)


#################################################### MAIN MENU FUNCTIONALITY #################################################
# new file function
url = ''
def new_file(event = None):
    global url
    url = ''
    text_editor.delete(1.0, tk.END)

file_menu.add_command(label = 'New', image = new_icon, compound = tk.LEFT, accelerator = 'Ctrl+N', command = new_file)

# open function

def open_file(event = None):
    global url
    url= filedialog.askopenfilename(initialdir = os.getcwd(), title = 'Select File', filetypes = (('Text Files', '*.txt'),('All Files','*.*')))

    try:
        with open(url, 'r') as fr:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(1.0, fr.read())

    except FileNotFoundError:
        return

    except:
        return

    win.title(os.path.basename(url))

file_menu.add_command(label = 'Open', image = open_icon, compound = tk.LEFT, accelerator = 'Ctrl+O', command = open_file)

# save function

def save_file(event = None):
    global url
    try:
        if url:
            content = str(text_editor.get(1.0, tk.END))
            with open(url, 'w', encoding = 'utf-8') as fw:
                fw.write(content)
        else:
            url = filedialog.asksaveasfile(mode = 'w', defaultextension = '.txt', filetypes=(('Text File','*.txt'),('All Files', '*.*')))
            content2 = text_editor.get(1.0, tk.END)
            url.write(content2)
            url.close()

    except:
        return

file_menu.add_command(label = 'Save', image = save_icon, compound = tk.LEFT, accelerator = 'Ctrl+S', command = save_file)

# save_as_function

def save_as_file(event = None):
    global url
    try:
        content = text_editor.get(1.0, tk.END)
        url = filedialog.asksaveasfile(mode = 'w', defaultextension = '.txt', filetypes=(('Text File','*.txt'),('All Files', '*.*')))
        url.write(content)
        url.close()

    except:
        return

file_menu.add_command(label = 'Save As', image = save_as_icon, compound = tk.LEFT, accelerator = 'Ctrl+Alt+S', command = save_as_file)

# exit functionality

def exit_func(event=None):
    global text_changed, url
    try:
        if text_changed:
            mbox = messagebox.askyesnocancel('Warning', 'Do you want to save the file?')
            if mbox is True:
                if url:
                    content = text_editor.get(1.0, tk.END)
                    with open(url, 'w', encoding='utf-8') as fw:
                        fw.write(content)
                        win.destroy()
                else:
                    content2 = str(text_editor.get(1.0, tk.END))
                    url = filedialog.asksaveasfile(mode = 'w', defaultextension='.txt', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
                    url.write(content2)
                    url.close()
                    win.destroy()
            elif mbox is False:
                win.destroy()
        else:
            win.destroy()
    except:
        return 

file_menu.add_command(label = 'Exit', image = exit_icon, compound = tk.LEFT, accelerator = 'Ctrl+Q', command = exit_func)


edit_menu.add_command(label = 'Copy', image = copy_icon, compound = tk.LEFT, accelerator = 'Ctrl+C', command = lambda : text_editor.event_generate('<Control c>'))
edit_menu.add_command(label = 'Paste', image = paste_icon, compound = tk.LEFT, accelerator = 'Ctrl+V', command = lambda : text_editor.event_generate('<Control v>'))
edit_menu.add_command(label = 'Cut', image = cut_icon, compound = tk.LEFT, accelerator = 'Ctrl+X', command = lambda : text_editor.event_generate('<Control x>'))
edit_menu.add_command(label = 'Clear All', image = clear_all_icon, compound = tk.LEFT, accelerator = 'Ctrl+Atl+X', command = lambda : text_editor.event_delete(1.0, tk.END))

# find function
def find_func(event=None):

    def find():
        word = find_input.get()
        text_editor.tag_remove('match', '1.0', tk.END)
        matches = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = text_editor.search(word, start_pos, stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f"{start_pos}+{len(word)}c"
                text_editor.tag_add('match', start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                text_editor.tag_config('match', foreground = 'red', background = 'yellow')

    def replace():
        word = find_input.get()
        replace_text = replace_input.get()
        content = text_editor.get(1.0, tk.END)
        new_content = content.replace(word, replace_text)
        text_editor.delete(1.0, tk.END)
        text_editor.insert(1.0, new_content)


    find_dialogue = tk.Toplevel()
    find_dialogue.geometry('450x250+500+200')
    find_dialogue.title('Find')
    find_dialogue.resizable(0,0)

    #frame
    find_frame = ttk.LabelFrame(find_dialogue, text = 'Find/Replace')
    find_frame.pack(pady = 20)

    #label
    text_find_label = ttk.Label(find_frame, text = 'Find')
    text_replace_label = ttk.Label(find_frame, text = 'Replace')

    #entry
    find_input = ttk.Entry(find_frame, width = 30)
    replace_input = ttk.Entry(find_frame, width = 30) 

    #button
    #find button function
    
    find_button = ttk.Button(find_frame, text = "Find", command = find)
    replace_button = ttk.Button(find_frame, text = 'Replace', command = replace)
    
    #label grid
    text_find_label.grid(row = 0, column = 0, padx = 4, pady = 4)
    text_replace_label.grid(row = 1, column = 0, padx = 4, pady = 4)

    #entry grid
    find_input.grid(row = 0, column = 1, padx = 4, pady = 4)
    replace_input.grid(row = 1, column = 1, padx = 4, pady = 4)

    #button grid
    find_button.grid(row = 2, column = 0, padx = 8, pady = 4)
    replace_button.grid(row = 2, column = 1, padx = 8, pady = 4)

    find_dialogue.mainloop()

edit_menu.add_command(label = 'Find', image = find_icon, compound = tk.LEFT, accelerator = 'Ctrl+F', command = find_func)

######################### View function #######################

show_statusbar = tk.BooleanVar()
show_statusbar.set(True)
show_toolbar = tk.BooleanVar()
show_toolbar.set(True)

def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar = False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side = tk.TOP, fill = tk.X)
        text_editor.pack(fill = tk.BOTH, expand = True)
        status_bar.pack(side = tk.BOTTOM)
        show_toolbar = False

view_menu.add_checkbutton(label = 'Tool Bar', onvalue = True, offvalue = 0, variable = show_toolbar, image = tool_bar_icon, compound = tk.LEFT, command = hide_toolbar)

def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar = False

    else:
        status_bar.pack(side = tk.BOTTOM)
        show_statusbar = True
        
view_menu.add_checkbutton(label = 'Status Bar',onvalue = True, offvalue = 0, variable= show_statusbar, image = status_bar_icon, compound = tk.LEFT, command= hide_statusbar)

############## Color Theme ##################

def change_color():
    chosen_theme = theme_choice.get()
    color_tuple = color_dict.get(chosen_theme)
    fg_color, bg_color = color_tuple[0], color_tuple[1]
    text_editor.config(background = bg_color, foreground = fg_color)
count = 0
for i in color_dict:
    color_menu.add_radiobutton(label = i, image = color_icons[count], variable = theme_choice, compound = tk.LEFT, command = change_color)
    count += 1

win.config(menu = main_menu)

########## Bind Shortcut Keys ###################
win.bind('<Control-n>', new_file)
win.bind('<Control-o>', open_file)
win.bind('<Control-s >', save_file)
win.bind('Control-Alt-s', save_as_file)
win.bind('<Control-q>', exit_func)
win.bind('<Control-f>', find_func)


win.mainloop()