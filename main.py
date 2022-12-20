import tkinter

#creating a window
window = tkinter.Tk()

window.title("first GUI Program")
window.minsize(width=500,height=300)
#adding padding to whole window
window.config(padx=20,pady=30)

#label

my_label = tkinter.Label(text = "I am a label", font=("Arial",24,"bold"))

#to get hold of this component on screen we need to use pack

#my_label.pack()
#we can change the text in maany ways
my_label["text"] = "new text"
my_label.config(text="new text")
#my_label.place(x=10,y=60)
my_label.grid(column=0,row=0)

#adding padding to a widget
my_label.config(pady=30,padx=30)


#button

#creating event listener so button actually works if we click it
def button_clicked():
    print("i got clicked")

def change_label():
    my_label["text"] = input.get()



button  = tkinter.Button(text="click me",command=change_label)

#button.pack()
button.grid(column=1,row=1)

new_button = tkinter.Button(text="new one")
new_button.grid(column=2,row=0)

#Entry(takes input)

input = tkinter.Entry(width=10)
#input.pack()
input.grid(column=3,row=3)
#to get the value entered by use we need to use get method
print(input.get())













#to keep the window on screen

window.mainloop()