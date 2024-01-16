import time
from tkinter import*
from PIL import ImageTk, Image
import random
from tkinter import messagebox 

gameWindow=Tk()
gameWindow.title("Vienādie attēli")
count=0
correctAnswer=0
Answer=[]
Answer_dict={}
answerCount=0
#gw=Tk()
#gw.title('Memory game')
#gw.configure(bg="pink")
#gw.resizable(1,1)

myimg1=ImageTk.PhotoImage(Image.open("cat1.jpg").resize((100,120)))
myimg2=ImageTk.PhotoImage(Image.open("necat2.jpg").resize((100,120)))
myimg3=ImageTk.PhotoImage(Image.open("necat3.jpg").resize((100,120)))
myimg4=ImageTk.PhotoImage(Image.open("necat4.jpg").resize((100,120)))
myimg5=ImageTk.PhotoImage(Image.open("necat5.jpg").resize((100,120)))


bgImg=ImageTk.PhotoImage(Image.open("bg labaks.webp"))


btn0=Button(width=100,height=120,image=bgImg, command=lambda:btnClick(btn0,0))
btn1=Button(width=100,height=120,image=bgImg, command=lambda:btnClick(btn1,1))
btn2=Button(width=100,height=120,image=bgImg, command=lambda:btnClick(btn2,2))
btn3=Button(width=100,height=120,image=bgImg, command=lambda:btnClick(btn3,3))
btn4=Button(width=100,height=120,image=bgImg, command=lambda:btnClick(btn4,4))
btn5=Button(width=100,height=120,image=bgImg, command=lambda:btnClick(btn5,5))
btn6=Button(width=100,height=120,image=bgImg, command=lambda:btnClick(btn6,6))
btn7=Button(width=100,height=120,image=bgImg, command=lambda:btnClick(btn7,7))
btn8=Button(width=100,height=120,image=bgImg, command=lambda:btnClick(btn8,8))
btn9=Button(width=100,height=120,image=bgImg, command=lambda:btnClick(btn9,9))


btn0.grid(row=1,column=0)
btn1.grid(row=2,column=0)
btn2.grid(row=1,column=4)
btn3.grid(row=1,column=1)
btn4.grid(row=2,column=1)
btn5.grid(row=2,column=3)
btn6.grid(row=1,column=2)
btn7.grid(row=2,column=2)
btn8.grid(row=2,column=4)
btn9.grid(row=1,column=3)


count=0
correctAnswer=0
Answer=[]
Answer_dict={}
answerCount=0


def infoLogs():
   gameWindow =Toplevel()
   gameWindow.title('Info ')
   gameWindow.geometry("500x300")



       

def reset():
   global count, correctAnswer, Answer, Answer_dict
   btn0.config(state=NORMAL)
   btn1.config(state=NORMAL)
   btn2.config(state=NORMAL)
   btn3.config(state=NORMAL)
   btn4.config(state=NORMAL)
   btn5.config(state=NORMAL)
   btn6.config(state=NORMAL)
   btn7.config(state=NORMAL)
   btn8.config(state=NORMAL)
   btn9.config(state=NORMAL)

btn0["image"]="pyimage5"
btn1["image"]="pyimage5"
btn2["image"]="pyimage5"
btn3["image"]="pyimage5"
btn4["image"]="pyimage5"
btn5["image"]="pyimage5"
btn6["image"]="pyimage5"
btn7["image"]="pyimage5"
btn8["image"]="pyimage5"
btn9["image"]="pyimage5"

#random.shuffle(ImageList)

count=0
correctAnswer=0
Answer=[]
Answer_dict={}
answerCount=0


#def info():
  # gameWindow+Toplevel()
  # gameWindow.title('d')





#btn0=Button(width=200, height=300, image=bgImg)
#btn1=Button(width=200, height=300, image=bgImg)
#btn2=Button(width=200, height=300, image=bgImg)
#btn3=Button(width=200, height=300, image=bgImg)
#btn4=Button(width=200, height=300, image=bgImg)
#btn5=Button(width=200, height=300, image=bgImg)
#btn6=Button(width=200, height=300, image=bgImg)
#btn7=Button(width=200, height=300, image=bgImg)
#btn8=Button(width=200, height=300, image=bgImg)
#btn9=Button(width=200, height=300, image=bgImg)

ImageList=[myimg1,myimg1,myimg2,myimg2,myimg3,myimg3,myimg4,myimg4,myimg5,myimg5]
random.shuffle(ImageList)
#Label=Label(image=Img1)



def btnClick(btn, number):
    global count, correctAnswer,Answer, Answer_dict
   # if btn["image"]=="pyimage6" and count<2:
     #  btn["image"]=ImageList[number]
      # count+=1
      # Answer.append(number)
     #  Answer_dict[btn]=ImageList[number]


    if btn["image"] == "pyimage6" and count < 2:
        btn["image"] = ImageList[number]
        count += 1 
        Answer.append(number) 
        Answer_dict[btn]=ImageList[number]


    if len(Answer)==2:

      
     # if ImageList[Answer[0]]==ImageList[Answer[1]]:
        # for key in Answer_dict:
          # key["state"]=DISABLED
          # correctAnswer+=2
         #  if(correctAnswer==2):
          #    messagebox.showinfo("Vinē??")
           #   correctAnswer=0
            #  if(correctAnswer==6):
             #    messagebox.askquestion("ok")
            count=0
            correctAnswer=0
            Answer=[]
            Answer_dict={}
            answerCount=0


    if ImageList[Answer[0]]==ImageList[Answer[1]]:
            for key in answer_dict:
                key["state"]=DISABLED

            Answer= []
            answer_dict = {}
            answerCount = 0
            correctAnswers += 1 
            messagebox.showinfo("Vienādi attēli", "Esi uzminējis! Kopā uzminēti komplekti: " + str(correctAnswers))

   #else:
      # messagebox.showinfo("VIENāDI")
     #  for key in Answer_dict:
       #     key["image"]="pyimage6"
       #     count=0
        #    Answer=[]
        #    Answer_dict={}
         #   return 0
       
    else :
            Tk.update(btn)
            time.sleep(0.5)
            for key in answer_dict:
                key["image"] = "pyimage5"
            answerCount = 0
            Answer= []
            answer_dict = {}


            if correctAnswers == 4:
             messagebox.showinfo("Vine")

    return 0



izvele=Menu(gameWindow)    #Izveido opcijas
gameWindow.config(menu=izvele)

opcijas=Menu(izvele,tearoff=FALSE)
izvele.add_cascade(label="Opcijas")


gameWindow.mainloop()