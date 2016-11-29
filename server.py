from tkinter import *
from tkinter import filedialog
from clustering import clusterPhotos
from html_template import (formatString, indexString)
import os
import shutil
from flask import Flask, request, send_file
app = Flask(__name__)

class MyApp():
    def __init__(self):
        self.listTag = "<li><a href=\"{}\">{}</a></li>" 
        self.elemTag = "<option value=\"{}\">{}</option>"

        self.files = set([])

    def chooseFiles(self):
        root = Tk()
        root.withdraw()
        newFiles = filedialog.askopenfilename(multiple=True)
        self.files.update(newFiles)

    def sortPhotos(self):
        home = os.getcwd()+"/static/output/cluster_page.html"
        clusters = clusterPhotos(self.files)
        if os.path.isdir(os.getcwd()+"/static/output"):
            shutil.rmtree(os.getcwd()+"/static/output")
        os.makedirs(os.getcwd()+"/static/output")
        indexLinks = ""
        for filename in clusters:
            name = filename.split('/')[-1]
            sname = name.split('.')[0]
            outfilename = os.getcwd()+"/static/output/{}.html".format(sname)
            newFile = open(outfilename, 'w')
            listString = ""
            for assocFile in clusters[filename]:
                f = assocFile.split('/')[-1]
                url_vals = assocFile.split('/')[-2:]
                url = "/static/" + url_vals[0] + "/" + url_vals[1]
                newstr = self.listTag.format(url,f)
                listString += newstr
            required_val = outfilename.split('/')[-2:]
            page_val = required_val[0] + "/" + required_val[1]
            newIndexStr = self.elemTag.format(page_val, sname)
            indexLinks += newIndexStr
            url_vals = filename.split('/')[-2:]
            url = "/static/" + url_vals[0] + "/" + url_vals[1]
            fileStr = formatString.format(url, name, listString)
            newFile.write(fileStr)
            newFile.close()
        indexfile = open(home, 'w')
        indextext = indexString.format(indexLinks)
        indexfile.write(indextext)
        indexfile.close()
        print("Done")

@app.route("/")
def index():
    return app.send_static_file('index.html')

@app.route('/cluster_page/')
def my_link():
    clustering = MyApp()
    clustering.chooseFiles()
    clustering.sortPhotos()
    print("got clicked")
    return app.send_static_file('output/cluster_page.html')


@app.route('/detail_page/', methods=['GET', 'POST'])
def detail_page():
    if request.method == "POST":
        cluster_file = request.form["cluster"]
        print(cluster_file)
        return app.send_static_file(cluster_file)
    else:
        return 'Error!'
if __name__ == "__main__":
    app.run()
