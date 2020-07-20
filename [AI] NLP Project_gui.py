# Core Packages
from textblob import TextBlob
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import *



# NLP Packages
import nltk
import spacy
nlp = spacy.load('en')
import speech_recognition as sr
import pyttsx3

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

 # Structure and Layout
window = Tk()
window.title("AI Project - [Master TA, IDDLo]  - Sentiment Analysis")
window.geometry("700x400")
window.config(background='black')

# TAB LAYOUT
tab_control = ttk.Notebook(window)
 
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)

# ADD TABS TO NOTEBOOK
tab_control.add(tab1, text='Text Analysis')
tab_control.add(tab2, text='File Analysis')
tab_control.add(tab4, text='Voice Analysis')



label1 = Label(tab1, text= 'NLP',padx=5, pady=5)
label1.grid(column=0, row=0)
 
label2 = Label(tab2, text= 'File Analysis',padx=5, pady=5)
label2.grid(column=0, row=0)



label4 = Label(tab4, text= 'Voice Recognition and Sentiment Analysis',padx=5, pady=5)
label4.grid(column=0, row=0)

tab_control.pack(expand=1, fill='both')



# Functions FOR NLP  FOR TAB ONE
def get_tokens():
	raw_text = str(raw_entry.get())
	new_text = TextBlob(raw_text)
	final_text = list(str(new_text.words).split(" "))
	result = '\nTokens:{}'.format(final_text)
	tab1_display.insert(tk.END,result)

def get_pos_tags():
	raw_text = str(raw_entry.get())
	new_text = TextBlob(raw_text)
	final_text = new_text.tags
	result = '\nPOS of Speech : {}'.format(final_text)
	tab1_display.insert(tk.END,result)


def get_sentiment():
	raw_text = str(raw_entry.get())
	new_text = TextBlob(raw_text)
	final_text = new_text.sentiment
	result = '\nSubjectivity:{}, Polarity:{}'.format(new_text.sentiment.subjectivity,new_text.sentiment.polarity)
	tab1_display.insert(tk.END,result)
	if(new_text.sentiment.polarity > 0):
	    txt = "\n░░░░░░░░░░░░▄▄░░░░░░░░░\n\
░░░░░░░░░░░█░░█░░░░░░░░\n\
░░░░░░░░░░░█░░█░░░░░░░░\n\
░░░░░░░░░░█░░░█░░░░░░░░\n\
░░░░░░░░░█░░░░█░░░░░░░░\n\
███████▄▄█░░░░░██████▄░░\n\
▓▓▓▓▓▓█░░░░░░░░░░░░░░█░\n\
▓▓▓▓▓▓█░░░░░░░░░░░░░░█░\n\
▓▓▓▓▓▓█░░░░░░░░░░░░░░█░\n\
▓▓▓▓▓▓█░░░░░░░░░░░░░░█░\n\
▓▓▓▓▓▓█░░░░░░░░░░░░░░█░\n\
▓▓▓▓▓▓█████░░░░░░░░░█░░\n\
██████▀░░░░▀▀██████▀░░░░"
	elif(new_text.sentiment.polarity < 0):
	    txt = "\n███████▄▄███████████▄\n\
▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n\
▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n\
▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n\
▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n\
▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n\
▓▓▓▓▓▓███░░░░░░░░░░░░█\n\
██████▀░░█░░░░██████▀\n\
░░░░░░░░░█░░░░█\n\
░░░░░░░░░░█░░░█\n\
░░░░░░░░░░░█░░█\n\
░░░░░░░░░░░█░░█\n\
░░░░░░░░░░░░▀▀ "
	tab1_display.insert(tk.END,txt)

def get_entities():
	raw_text = str(raw_entry.get())
	docx = nlp(raw_text)
	final_text = [(entity.text,entity.label_) for entity in docx.ents ]
	result = '\nEntities:{}'.format(final_text)
	tab1_display.insert(tk.END,result)



# Clear entry widget
def clear_entry_text():
	entry1.delete(0,END)

def clear_display_result():
	tab1_display.delete('1.0',END)


# Clear Text  with position 1.0
def clear_text_file():
	displayed_file.delete('1.0',END)

# Clear Result of Functions
def clear_result():
	tab2_display_text.delete('1.0',END)

# Clear Result of voice
def clear_result_Voice():
	tab4_display_result.delete('1.0',END)

# Functions for TAB 2 FILE PROCESSER
# Open File to Read and Process
def openfiles():
	file1 = tk.filedialog.askopenfilename(filetypes=(("Text Files",".txt"),("All files","*")))
	read_text = open(file1).read()
	displayed_file.insert(tk.END,read_text)


def get_file_tokens():
	raw_text = displayed_file.get('1.0',tk.END)
	new_text = TextBlob(raw_text)
	final_text = list(str(new_text.words).split(" "))
	result = '\nTokens:{}'.format(final_text)
	tab2_display_text.insert(tk.END,result)


def get_file_pos_tags():
	raw_text = displayed_file.get('1.0',tk.END)
	new_text = TextBlob(raw_text)
	final_text = new_text.tags
	result = '\nPOS of Speech : {}'.format(final_text)
	tab2_display_text.insert(tk.END,result)


def get_file_sentiment():
	raw_text = displayed_file.get('1.0',tk.END)
	new_text = TextBlob(raw_text)
	final_text = new_text.sentiment
	result = '\nSubjectivity:{}, Polarity:{}'.format(new_text.sentiment.subjectivity,new_text.sentiment.polarity)
	tab2_display_text.insert(tk.END,result)
	if(new_text.sentiment.polarity > 0):
	    txt = "\n░░░░░░░░░░░░▄▄░░░░░░░░░\n\
░░░░░░░░░░░█░░█░░░░░░░░\n\
░░░░░░░░░░░█░░█░░░░░░░░\n\
░░░░░░░░░░█░░░█░░░░░░░░\n\
░░░░░░░░░█░░░░█░░░░░░░░\n\
███████▄▄█░░░░░██████▄░░\n\
▓▓▓▓▓▓█░░░░░░░░░░░░░░█░\n\
▓▓▓▓▓▓█░░░░░░░░░░░░░░█░\n\
▓▓▓▓▓▓█░░░░░░░░░░░░░░█░\n\
▓▓▓▓▓▓█░░░░░░░░░░░░░░█░\n\
▓▓▓▓▓▓█░░░░░░░░░░░░░░█░\n\
▓▓▓▓▓▓█████░░░░░░░░░█░░\n\
██████▀░░░░▀▀██████▀░░░░"
	elif(new_text.sentiment.polarity < 0):
	    txt = "\n███████▄▄███████████▄\n\
▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n\
▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n\
▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n\
▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n\
▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n\
▓▓▓▓▓▓███░░░░░░░░░░░░█\n\
██████▀░░█░░░░██████▀\n\
░░░░░░░░░█░░░░█\n\
░░░░░░░░░░█░░░█\n\
░░░░░░░░░░░█░░█\n\
░░░░░░░░░░░█░░█\n\
░░░░░░░░░░░░▀▀ "
	tab2_display_text.insert(tk.END,txt)
        


def get_file_entities():
	raw_text = displayed_file.get('1.0',tk.END)
	docx = nlp(raw_text)
	final_text = [(entity.text,entity.label_) for entity in docx.ents ]
	result = '\nEntities:{}'.format(final_text)
	tab2_display_text.insert(tk.END,result)


def nlpiffy_file():
	raw_text = displayed_file.get('1.0',tk.END)
	docx = nlp(raw_text)
	final_text = [ (token.text,token.shape_,token.lemma_,token.pos_) for token in docx ]
	result = '\nSummary:{}'.format(final_text)
	tab2_display_text.insert(tk.END,result)

#Functions for TAB 3 Voice Recognition
def speak(message):
    engine=pyttsx3.init()
    rate=engine.getProperty('rate')
    engine.setProperty('rate',rate-10)
    engine.say('{}'.format(message))
    engine.runAndWait()

def Voice_recognition():
    r = sr.Recognizer()
    tab4_display_result.insert(tk.END,'\nSay Something, and I will analyze it for you..\n')
    with sr.Microphone() as source:
        print()
        print('Say Something...') 
        audio = r.listen(source, timeout=3)
        try:
            text = r.recognize_google(audio)
            tb = TextBlob(text)
            txt = 'You said : {} '.format(text)
            tab4_display_result.insert(tk.END,txt)
            txt_1 = '\nSubjectivity:{}, Polarity:{}'.format(tb.sentiment.subjectivity,tb.sentiment.polarity)
            tab4_display_result.insert(tk.END,txt_1)
            speak(text)

            if(tb.sentiment.polarity > 0):
                txt_2 = '\n{}'.format("░░░░░░░░░░░░▄▄░░░░░░░░░\n\
░░░░░░░░░░░█░░█░░░░░░░░\n\
░░░░░░░░░░░█░░█░░░░░░░░\n\
░░░░░░░░░░█░░░█░░░░░░░░\n\
░░░░░░░░░█░░░░█░░░░░░░░\n\
███████▄▄█░░░░░██████▄░░\n\
▓▓▓▓▓▓█░░░░░░░░░░░░░░█░\n\
▓▓▓▓▓▓█░░░░░░░░░░░░░░█░\n\
▓▓▓▓▓▓█░░░░░░░░░░░░░░█░\n\
▓▓▓▓▓▓█░░░░░░░░░░░░░░█░\n\
▓▓▓▓▓▓█░░░░░░░░░░░░░░█░\n\
▓▓▓▓▓▓█████░░░░░░░░░█░░\n\
██████▀░░░░▀▀██████▀░░░░")
            elif(tb.sentiment.polarity < 0):
                txt_2 = '\n{}'.format("███████▄▄███████████▄\n\
▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n\
▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n\
▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n\
▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n\
▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n\
▓▓▓▓▓▓███░░░░░░░░░░░░█\n\
██████▀░░█░░░░██████▀\n\
░░░░░░░░░█░░░░█\n\
░░░░░░░░░░█░░░█\n\
░░░░░░░░░░░█░░█\n\
░░░░░░░░░░░█░░█\n\
░░░░░░░░░░░░▀▀ ")
            tab4_display_result.insert(tk.END,txt_2)
              
        except:
            print('Sorry... Try again')



# MAIN NLP TAB
l1=Label(tab1,text="Enter Text To Analysis")
l1.grid(row=1,column=0)


raw_entry=StringVar()
entry1=Entry(tab1,textvariable=raw_entry,width=50)
entry1.grid(row=1,column=1)

# BUTTONS
button1=Button(tab1,text="Tokenize", width=12,command=get_tokens,bg='#03A9F4',fg='#fff')
button1.grid(row=4,column=0,padx=10,pady=10)


button2=Button(tab1,text="POS Tags", width=12,command=get_pos_tags,bg='#BB86FC')
button2.grid(row=4,column=1,padx=10,pady=10)


button3=Button(tab1,text="Sentiment", width=12,command=get_sentiment,bg="#b9f6ca")
button3.grid(row=4,column=2,padx=10,pady=10)


button5=Button(tab1,text="Reset", width=12,command=clear_entry_text,bg='#f44336',fg='#fff')
button5.grid(row=5,column=0,padx=10,pady=10)

button6=Button(tab1,text="Clear Result", width=12,command=clear_display_result)
button6.grid(row=5,column=2,padx=10,pady=10)

# Display Screen For Result
tab1_display = Text(tab1)
tab1_display.grid(row=7,column=0, columnspan=3,padx=5,pady=5)

# Allows you to edit
tab1_display.config(state=NORMAL)

########################################################################################
#Voice Recognition Tab
l4=Label(tab4,text="Press Button and Say Something in English")
l4.grid(row=1,column=0)

#Button Voice Recognition
btn1=Button(tab4,text="Press to talk", width=12,command=Voice_recognition,bg='#03A9F4',fg='#fff')
btn1.grid(row=4,column=0,padx=10,pady=10)

btn2=Button(tab4,text="Clear Result", width=12,command=clear_result_Voice)
btn2.grid(row=4,column=1,padx=10,pady=10)
# Display Screen For Result
tab4_display_result = ScrolledText(tab4)
tab4_display_result.grid(row=7,column=0, columnspan=3,padx=5,pady=5)
#########################################################################################

# FILE READING  AND PROCESSING TAB
l1=Label(tab2,text="Open File To Process")
l1.grid(row=1,column=1)


displayed_file = ScrolledText(tab2,height=7)# Initial was Text(tab2)
displayed_file.grid(row=2,column=0, columnspan=3,padx=5,pady=3)


# BUTTONS FOR SECOND TAB/FILE READING TAB
b0=Button(tab2,text="Open File", width=12,command=openfiles,bg='#c5cae9')
b0.grid(row=3,column=0,padx=10,pady=10)

b1=Button(tab2,text="Reset ", width=12,command=clear_text_file,bg="#f44336",fg='#fff')
b1.grid(row=3,column=1,padx=10,pady=10)

b4=Button(tab2,text="Sentiment", width=12,command=get_file_sentiment,bg='#b9f6ca')
b4.grid(row=3,column=2,padx=10,pady=10)


b6=Button(tab2,text="Clear Result", width=12,command=clear_result)
b6.grid(row=4,column=2,padx=10,pady=10)

b7=Button(tab2,text="Close", width=12,command=window.destroy)
b7.grid(row=4,column=0,padx=10,pady=10)

# Display Screen

# tab2_display_text = Text(tab2)
tab2_display_text = ScrolledText(tab2)
tab2_display_text.grid(row=6,column=0, columnspan=3,padx=5,pady=5)

# Allows you to edit
tab2_display_text.config(state=NORMAL)

window.mainloop()



