from tkinter import *
from tkinter.filedialog import askopenfilename
from clustering import clusterPhotos
from html import (formatString, indexString)
import os
import shutil


class MyApp():
    def __init__(self):
        self.listTag = "<li><a href=\"{}\">{}</a></li>"
        self.elemTag = "<li><a href=\"{}\">{}</a></li>"
        self.root = Tk()
        self.root.wm_title("Photo Sorter")
        self.files = set([])
        self.listbox = Listbox(self.root)
        textvar = StringVar()
        label = Label(self.root, textvariable=textvar)
        textvar.set("Imported Photos")
        scrollbar = Scrollbar(self.root)
        sortButton = Button(self.root, text = 'Sort Photos', command = self.sortPhotos)
        chooseButton = Button(self.root, text = 'Add Photos', command = self.chooseFiles)

        self.listbox.grid(row=3, column=1, padx=(100, 10))
        scrollbar.grid(row=3, column=2, sticky=E+W) 
        self.listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listbox.yview)
        sortButton.grid(row=1, column=0, padx=(0, 0))
        chooseButton.grid(row=2, column=0, padx=(10, 10))
        label.grid(row=2, column=1, padx=(100, 10))

    def chooseFiles(self):
        newFiles = askopenfilename(multiple=True)
        self.files.update(newFiles)
        for filen in self.files:
            name = filen.split('/')[-1]
            self.listbox.insert(END, name)

    def sortPhotos(self):
        home = os.getcwd()+"/output/index.html"
        clusters = clusterPhotos(self.files)
        if os.path.isdir(os.getcwd()+"/output"):
            shutil.rmtree(os.getcwd()+"/output")
        os.makedirs(os.getcwd()+"/output")
        indexLinks = ""
        for filename in clusters:
            name = filename.split('/')[-1]
            sname = name.split('.')[0]
            outfilename = os.getcwd()+"/output/{}.html".format(sname)
            newFile = open(outfilename, 'w')
            listString = ""
            for assocFile in clusters[filename]:
                f = assocFile.split('/')[-1]
                newstr = self.listTag.format(assocFile,f)
                listString += newstr
            newIndexStr = self.elemTag.format(outfilename, sname)
            indexLinks += newIndexStr
            fileStr = formatString.format(home, home, filename, name, listString)
            newFile.write(fileStr)
            newFile.close()
        indexfile = open(home, 'w')
        indextext = indexString.format(home, home, indexLinks)
        indexfile.write(indextext)
        indexfile.close()
        print("Done")
        

app = MyApp()
app.root.mainloop()
