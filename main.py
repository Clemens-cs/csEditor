from os import name
from tkinter import *
from tkinter import messagebox #for Debugging 
from tkinter import filedialog
from tkinter import font
from tkinter import colorchooser
import tkinter

TK_SILENCE_DEPRECATION=1
root = Tk()
root.title('csEditor - file')
root.iconbitmap('logo.png')
root.geometry("1440x825")

global openFileName
openFileName = "untitled"

global selectedText
selectedText = False

############################################Functions##############################################

#a popupwindow to show an error message
def popupWindow():
    tkinter.messagebox.showinfo('Error Message', 'This function has not been added so far!')

#new File
def newFile():
    mainText.delete("1.0", END)
    root.title('csEditor - New File')
    statusBar.config(text="New File      ")

    global openFileName
    openFileName = False

#open File
def openFile():
    mainText.delete("1.0", END)

    textFile = filedialog.askopenfilename(title="Open File", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("CSS Files", "*.css"), ("Javascript Files", "*.js") ,("CSharp Files", "*.cs"), ("Unity Files", "*.unity"), ("Meta Files", "*.meta"),("Python Files", "*.py"), ("Other Files", "*.*")) )

    if textFile:
        global openFileName
        openFileName = textFile
    
    name = textFile
    statusBar.config(text=f'{name}        ')
    root.title(f'csEditor - {name}')

    textFile = open(textFile, 'r')
    textFileWords = textFile.read()
    mainText.insert(END, textFileWords)
    textFile.close()

#saveFile
def saveFile(e):
    global openFileName
    if openFileName:
        textFile = open(openFileName, 'w')
        textFile.write(mainText.get(1.0, END))
        textFile.close()
        statusBar.config(text=f'Saved: {openFileName}     ')
    else:
        saveAsFile()
    
#saveAsFile
def saveAsFile():
    textFile = filedialog.asksaveasfilename(defaultextension=".*", title="Save File", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("CSS Files", "*.css"), ("Javascript Files", "*.js") ,("CSharp Files", "*.cs"), ("Unity Files", "*.unity"), ("Meta Files", "*.meta"),("Python Files", "*.py"), ("Other Files", "*.*")) )
    if textFile:
        name = textFile
        statusBar.config(text=f'Saved: {name}        ')
        root.title(f'csEditor - {name}')

        textFile = open(textFile, 'w')
        textFile.write(mainText.get(1.0, END))
        textFile.close()

#cut text
def cutText(e):
    global selectedText
    if mainText.selection_get():
        selectedText = mainText.selection_get()
        mainText.delete("sel.first", "sel.last")

#copy text
def copyText(e):
    global selectedText
    if mainText.selection_get():
        selectedText = mainText.selection_get()

#paste text
def pasteText(e):
    if selectedText:
        position = mainText.index(INSERT)
        mainText.insert(position, selectedText)

#bold text
def boldText():
    boldFont = font.Font(mainText, mainText.cget("font"))
    boldFont.configure(weight="bold")

    mainText.tag_configure("bold", font=boldFont)

    currentTags = mainText.tag_names("sel.first")

    if "bold" in currentTags:
        mainText.tag_remove("bold", "sel.first", "sel.last")
    else:
        mainText.tag_add("bold", "sel.first", "sel.last")

#italics text
def italicsText():
    italicFont = font.Font(mainText, mainText.cget("font"))
    italicFont.configure(slant="italic")
    mainText.tag_configure("italic", font=italicFont)

    currentTags = mainText.tag_names("sel.first")

    if "italic" in currentTags:
        mainText.tag_remove("italic", "sel.first", "sel.last")
    else:
        mainText.tag_add("italic", "sel.first", "sel.last")

#text color
def textColor():
    myColor = colorchooser.askcolor()[1]
    if myColor:
        statusBar.config(text=myColor)
        colorFont = font.Font(mainText, mainText.cget("font"))
        colorFont.configure(slant="italic")
        mainText.tag_configure("colored", font=colorFont, foreground=myColor)
        currentTags = mainText.tag_names("sel.first")
        if "colored" in currentTags:
            mainText.tag_remove("colored", "sel.first", "sel.last")
        else:
            mainText.tag_add("colored", "sel.first", "sel.last")

#all text color
def allTextColor():
    myColor = colorchooser.askcolor()[1]
    if myColor:
        mainText.config(fg=myColor)

#background color
def bgColor():
    myColor = colorchooser.askcolor()[1]
    if myColor:
        mainText.config(bg=myColor)

#print file
def printFile():
    popupWindow()

#insert table
def insertTable():
    popupWindow()

#insert Equation
def insertEquation():
    popupWindow()

#insert Symbols
def insertSymbols():
    popupWindow()

#insert Links
def insertLinks():
    popupWindow()

#use Code Mode
def insertCode():
    popupWindow()

#layout Margins
def layoutMargins():
    popupWindow()

#layout Orientation
def layoutOrientation():
    popupWindow()

#layout Breaks
def layoutBreaks():
    popupWindow()

#layout Size
def layoutSize():
    popupWindow()

#layout Columns
def layoutColumns():
    popupWindow()

#layout Bulletpoints
def layoutBulletpoints():
    popupWindow()   

#window Minimise
def windowMinimise():
    popupWindow()   

#window Zoom
def windowZoom():
    popupWindow()   

#window File-Information
def windowTextInformation():
    popupWindow()   

############################################UI###############################################

#toolbar frame
toolbarFrame = Frame(root)
toolbarFrame.pack(fill=X)

#main frame
mainFrame = Frame(root)
mainFrame.pack(pady=5)

#scroll bar for the text
textScroll = Scrollbar(mainFrame)
textScroll.pack(side=RIGHT, fill=Y)

#horizontal scroll bar
horizontalScroll = Scrollbar(mainFrame, orient="horizontal")
horizontalScroll.pack(side=BOTTOM, fill=X)

#text box
mainText = Text(mainFrame, width=1200, padx=5,height=550, font=("Helvetia", 14), selectbackground="yellow", selectforeground="black",undo=True, yscrollcommand=textScroll.set, xscrollcommand=horizontalScroll.set,wrap="none")
mainText.pack()

#config scrollbar
textScroll.config(command=mainText.yview)
horizontalScroll.config(command=mainText.xview)

#Menu
mainMenu = Menu(root)
root.config(menu=mainMenu)

#file Menu
fileMenu = Menu(mainMenu, tearoff=False)
mainMenu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="New", command=newFile)
fileMenu.add_command(label="Open", command=openFile)
fileMenu.add_command(label="Save", command=lambda: saveFile(False))
fileMenu.add_command(label="Save As", command=saveAsFile)
fileMenu.add_separator()
fileMenu.add_command(label="Print", command=printFile)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=root.quit)

#edit Menu
editMenu = Menu(mainMenu, tearoff=False)
mainMenu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Cut", command=lambda: cutText(False))
editMenu.add_command(label="Copy", command=lambda: copyText(False))
editMenu.add_command(label="Paste", command=lambda: pasteText(False))
editMenu.add_separator()
editMenu.add_command(label="Undo", command=mainText.edit_undo)
editMenu.add_command(label="Redo", command=mainText.edit_redo)

#color Menu
colorMenu = Menu(mainMenu, tearoff=False)
mainMenu.add_cascade(label="Colors", menu=colorMenu)
colorMenu.add_command(label="Change Selected Text Color", command=textColor)
colorMenu.add_command(label="Change All Text Color", command=allTextColor)
colorMenu.add_command(label="Change Background Color", command=bgColor)

#insert Menu
insertMenu = Menu(mainMenu, tearoff=False)
mainMenu.add_cascade(label="Insert", menu=insertMenu)
insertMenu.add_command(label="Table", command=insertTable)
insertMenu.add_command(label="Equation", command=insertEquation)
insertMenu.add_command(label="Symbols", command=insertSymbols)
insertMenu.add_command(label="Links", command=insertLinks)
insertMenu.add_separator()
insertMenu.add_command(label="Code", command=insertCode)

#layout Menu
layoutMenu = Menu(mainMenu, tearoff=False)
mainMenu.add_cascade(label="Layout", menu=layoutMenu)
layoutMenu.add_command(label="Margins", command=layoutMargins)
layoutMenu.add_command(label="Orientation", command=layoutOrientation)
layoutMenu.add_command(label="Breaks", command=layoutBreaks)
layoutMenu.add_separator()
layoutMenu.add_command(label="Size", command=layoutSize)
layoutMenu.add_command(label="Columns", command=layoutColumns)
layoutMenu.add_separator()
layoutMenu.add_command(label="Bulletpoints and Numbering", command=layoutBulletpoints)

#window Menu
windowMenu = Menu(mainMenu, tearoff=False)
mainMenu.add_cascade(label="Window", menu=windowMenu)
windowMenu.add_command(label="Minimise", command=windowMinimise)
windowMenu.add_command(label="Zoom", command=windowZoom)
windowMenu.add_separator()
windowMenu.add_command(label="Basic Information", command=windowTextInformation)

#status bar
statusBar = Label(root, text="Ready      ", anchor=E)
statusBar.pack(fill=X, side=BOTTOM, ipady=15)

#bindings
root.bind('<Control-s>', saveFile)
root.bind('<Control-x>', cutText)
root.bind('<Control-c>', copyText)
root.bind('<Control-v>', pasteText)

###########Toolbar################
#Buttons
boldButton = Button(toolbarFrame, text="Bold", command=boldText)
boldButton.grid(row=0, column=0, sticky=W, padx=5)
boldButton.config(background="black")
italicsButton = Button(toolbarFrame, text="Italics", command=italicsText)
italicsButton.grid(row=0, column=1, sticky=W, padx=5)
undoButton = Button(toolbarFrame, text="Undo", command=mainText.edit_undo)
undoButton.grid(row=0, column=2, sticky=W, padx=5)
redoButton = Button(toolbarFrame, text="Redo", command=mainText.edit_redo)
redoButton.grid(row=0, column=3, sticky=W, padx=5)
colorTextButton = Button(toolbarFrame, text="Color", command=textColor)
colorTextButton.grid(row=0, column=4, sticky=W, padx=5)
#Dropdown

root.mainloop()