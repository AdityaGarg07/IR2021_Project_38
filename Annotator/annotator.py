import json
from tkinter import * 
from tkinter import filedialog
from tkinter import messagebox as box

file =  open('mayank.json','r',encoding="utf8")
# initialize startfrom to -1 for the first time
startfrom = 16  # update this at last accordingly as per the print statement 
# initially -1 indicates that I am at tweet number -1.
# press None first time everytime would take me to tweet number 0

opini = open('opinion.txt','a+',encoding="utf8")
true = open('fact.txt','a+',encoding="utf8")
false = open('fake.txt','a+',encoding="utf8")

allTweet = file.readlines()
n = len(allTweet)

file.close()


# gui part started
parent=Tk()
fr=Frame(parent,background="#edf")
fr.inputText=Text(parent)
parent.title("Tweet Annotator")



def getCurrTweet():
	tweet = allTweet[startfrom]
	injson = json.loads(tweet)
	text = injson['tweet']
	return text

def nextTweet():
	fr.inputText.delete(1.0,END)
	global startfrom
	startfrom += 1
	if( n > startfrom):
		fr.inputText.insert(index = INSERT, chars = getCurrTweet())

def fake():
	tweet = getCurrTweet()
	false.write(tweet+"\n")
	nextTweet()

def fact():
	tweet = getCurrTweet()
	true.write(tweet+"\n")
	nextTweet()

def opinion():
	tweet = getCurrTweet()
	opini.write(tweet+"\n")
	nextTweet()

def none():
	nextTweet()

def gui():
	fr.pack(fill=BOTH,expand=1)
	parent.geometry('500x500+%d+%d' % ((parent.winfo_screenwidth() - 500)/2, (parent.winfo_screenheight() - 500)/2))
	Button(fr, text = "Fact", command = fact).place(relx = 0.6, rely = 0.6, relwidth = 0.2)
	Button(fr, text = "Fake", command = fake).place(relx = 0.2, rely = 0.6, relwidth = 0.2)
	Button(fr, text = "Opinion", command = opinion).place(relx = 0.6, rely = 0.8, relwidth = 0.2)
	Button(fr, text = "None", command = none).place(relx = 0.2, rely = 0.8, relwidth = 0.2)

	fr.inputText.place(relx = 0.1, rely = 0.07, relwidth = 0.8, relheight = 0.35)

	Label(fr, text = "Tweet", background='#eed').place(relx = 0.35, rely = 0.02, relwidth = 0.3)

	parent.mainloop()

gui()

print("Update \"startfrom\" variable next time to",startfrom)
opini.close()
true.close()
false.close()