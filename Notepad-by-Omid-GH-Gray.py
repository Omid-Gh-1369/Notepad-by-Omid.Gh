from tkinter import *

window_3=Tk()
window_3.title("Notepad_by_Omid-Gh")
window_3.geometry("800x600")
window_3.resizable(width=False, height=True)
menubar=Menu(window_3,bg='gray20',fg="white")

file=Menu(menubar,tearoff=0,bg="gray25",fg="white")  
file.add_command(label="New tab")  
file.add_command(label="New window")  

file.add_command(label="Open")  
file.add_command(label="Save")  
file.add_command(label="Save as...") 
file.add_command(label="Save all")

file.add_separator()
file.add_command(label="Page setup")  
file.add_command(label="Print")

file.add_separator()
file.add_command(label="Close tab") 
file.add_command(label="Close window") 
file.add_command(label="Exit")
menubar.add_cascade(label="File",menu=file,)

edit=Menu(menubar,tearoff=0,bg="gray25",fg="white",)
edit.add_command(label="Undo")
edit.add_separator()

edit.add_command(label="Cut")  
edit.add_command(label="Copy")  
edit.add_command(label="Paste")  
edit.add_command(label="Delete")  
edit.add_command(label="Select All")
menubar.add_cascade(label="Edit",menu=edit)

he=Menu(menubar,tearoff=0,bg="gray25",fg="white")
he.add_command(label="About")
menubar.add_cascade(label="Help",menu=he)

window_3.config(menu=menubar,bg="gray20")
scroll_bar=Scrollbar(window_3)
scroll_bar.pack(side="right",fill="both")
text=Text(window_3,background="gray20",yscrollcommand=scroll_bar.set,foreground="white",font=("Consolas",11))
text.pack(side="left",expand=True,fill="both")
scroll_bar.config(command=text.yview_moveto)
window_3.mainloop()
