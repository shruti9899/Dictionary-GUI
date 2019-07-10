from tkinter import *  #tkinter is python's library handles GUI
import json    #for parsing json files
import difflib 


#object of tkinter
#main element
root=Tk()

global name

#loading data from json file
data=json.load(open('dictionary.json'))

#function to retrieve meaning of word being searched
def retrieve_data(word):
	if word in data:
		return(data[word])
	else:
		return "not found"


#function to display search result
def Search():
	print(str(name.get()))
	frame2=Frame(root,height=15).pack()
	#calling retrieve function to search meaning of user input
	output=retrieve_data(str(name.get().lower()))  #lowering cases of word is necessary as json file have all words in lowe case
	
	#we get output in list form if word matches with any json file's word
	if type(output)==list:
		for d in output:
			label=Label(root,text='-> '+d,bg="black",fg="white",font=('ariel',10,'bold')).pack()
			frame=Frame(root,height=10).pack()
	else:
		label=Label(root,text="Not Found",fg="white",bg="black").pack()


#for storing user input
name=StringVar()

#font format and packing that individual element to main element
label_1=Label(root,text="DICTIONARY",font=('ariel',40,'bold'),fg="steelblue").pack()
frame=Frame(root,height=20).pack()
label_2=Label(root,text="Enter word to search..",font=('ariel',20,'bold')).pack()

#element for user input
entry_box=Entry(root,textvariable=name,width=50).pack()
#input stored in name
frame=Frame(root,height=15).pack()

#onclick calling search function
button_1=Button(root,text="search",command=Search).pack()

#continuous loop to display window
root.mainloop()