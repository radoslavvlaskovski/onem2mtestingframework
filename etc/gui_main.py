""" 

The main GUI function that organizes 
the strucute of the GUI and calls the 
frames

"""

try:
	from tkinter import *
except ImportError:
	from Tkinter import *
	import ttk
from etc import gui_frames as frames
from etc import gui_helper

def launch(sender ):
    root = Tk()
    root.maxsize(1366,768)
    root.minsize(1366,768)
    #root.attributes("-fullscreen", True)

    notebook = ttk.Notebook(root,)
    notebook.pack(fill=BOTH, expand=True)

    container1 = Frame(root)
    container1.pack(fill=BOTH, expand=True)
    container2 = Frame(root)
    container2.pack(fill=BOTH, expand=True)
    container3 = Frame(root)
    container3.pack(fill=BOTH, expand=True)
    container4 = Frame(root)
    container4.pack(fill=BOTH, expand=True)
    container5 = Frame(root)
    container5.pack(fill=BOTH, expand=True)    

    notebook.add(container1, text="Behaviour Tests", state="normal")
    notebook.add(container2, text="Functional Tests", state="normal")
    notebook.add(container3, text="Syntax Tests", state="normal")
    notebook.add(container4, text="Custom Behaviour Test", state="normal")
    notebook.add(container5, text="Functional Parameter Test", state="normal")

    sub1 = gui_helper.add_scroll(container1)
    sub2 = gui_helper.add_scroll(container3)
    sub3 = gui_helper.add_scroll(container4)

    frames.create_functional_frame(container2, sender)
    frames.create_behaviour_frame(sub1, sender)
    frames.create_syntax_frame(sub2, sender)
    frames.create_custom_behaviour_frames(sub3, sender)
    frames. create_response_functional_frame(container5, sender)

    root.mainloop()

