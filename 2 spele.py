import time
from tkinter import*
from PIL import ImageTk, Image
import random
from tkinter import messagebox 

#gameWindow=Tk()
#gameWindow.title("Vienādie attēli")
#count=0
#correctAnswer=0
#Answer=[]
#Answer_dict={}
#answerCount=0
gw=Tk()
gw.title('Memory game')
gw.configure(bg="pink")
gw.resizable(1,1)


bgImages = [ImageTk.PhotoImage(Image.open("bg labaks.webp").resize((100, 120))) for _ in range(10)]

myimg0=ImageTk.PhotoImage(Image.open("cat1.jpg").resize((100,120)))
myimg1=ImageTk.PhotoImage(Image.open("necat2.jpg").resize((100,120)))
myimg2=ImageTk.PhotoImage(Image.open("necat3.jpg").resize((100,120)))
myimg3=ImageTk.PhotoImage(Image.open("necat4.jpg").resize((100,120)))
myimg4=ImageTk.PhotoImage(Image.open("necat5.jpg").resize((100,120)))
#myimg5=ImageTk.PhotoImage(Image.open("necat1.jpg").resize((100,120)))

ImageList = [myimg1, myimg2, myimg3, myimg0, myimg4] * 2
myLabel=Label(image=myimg1)


bgImg=ImageTk.PhotoImage(Image.open("bg labaks.webp"))

btn0=Button(width=100,height=120,image=bgImages[0], command=lambda:btnClick(btn0,0))
btn1=Button(width=100,height=120,image=bgImages[1], command=lambda:btnClick(btn1,1))
btn2=Button(width=100,height=120,image=bgImages[2], command=lambda:btnClick(btn2,2))
btn3=Button(width=100,height=120,image=bgImages[3], command=lambda:btnClick(btn3,3))
btn4=Button(width=100,height=120,image=bgImages[4], command=lambda:btnClick(btn4,4))
btn5=Button(width=100,height=120,image=bgImages[5], command=lambda:btnClick(btn5,5))
btn6=Button(width=100,height=120,image=bgImages[6], command=lambda:btnClick(btn6,6))
btn7=Button(width=100,height=120,image=bgImages[7], command=lambda:btnClick(btn7,7))
btn8=Button(width=100,height=120,image=bgImages[8], command=lambda:btnClick(btn8,8))
btn9=Button(width=100,height=120,image=bgImages[9], command=lambda:btnClick(btn9,9))


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

random.shuffle(ImageList)

count=0
correctAnswer=0
Answer=[]
Answer_dict={}
answerCount=0





       

def reset():
  global count, correctAnswer, Answer, Answer_dict, answerCount
  btn0.config(image=bgImages[0],state=NORMAL)
  btn1.config(image=bgImages[1],state=NORMAL)
  btn2.config(image=bgImages[2],state=NORMAL)
  btn3.config(image=bgImages[3],state=NORMAL)
  btn4.config(image=bgImages[4],state=NORMAL)
  btn5.config(image=bgImages[5],state=NORMAL)
  btn6.config(image=bgImages[6],state=NORMAL)
  btn7.config(image=bgImages[7],state=NORMAL)
  btn8.config(image=bgImages[8],state=NORMAL)
  btn9.config(image=bgImages[9],state=NORMAL)

  count = 0
  correctAnswer = 0
  Answer = []
  Answer_dict = {}
  answerCount = 0

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

random.shuffle(ImageList)

count=0
correctAnswer=0
Answer=[]
Answer_dict={}
answerCount=0


#def info():
  # gameWindow+Toplevel()
  # gameWindow.title('d')


def infoLogs():
   gw =Toplevel()
   gw.title('Informacija par programu!! ')
   gw.geometry("800x130")
   speleinfo=Label(gw,text="Griežot kartītes otrādāk, atmini 2 vienādas kartītes. Šādi turpināt līdz visas ir atvērtas. Lūdzu atļauj bildēm ielādēties, iedot viņām dažas sekundes")
   speleinfo.grid(row=5,column=6)
   return 0


def btnClick(btn, number):
    global count, correctAnswer, Answer, Answer_dict, answerCount

    if btn["image"] == "pyimage5" and count < 2:
        btn["image"] = ImageList[number]
        count += 1
        Answer.append(number)
        Answer_dict[btn] = ImageList[number]

    if len(Answer) == 2:
        if ImageList[Answer[0]] == ImageList[Answer[1]]:
            for key in Answer_dict:
                key["state"] = DISABLED
                correctAnswer += 2
                if correctAnswer == 2:
                    correctAnswer = 0
                    answerCount += 1
        else:
            gw.update()
            time.sleep(1.5)
            for key in Answer_dict:
                key["image"] = "pyimage5"

        count = 0
        Answer = []
        Answer_dict = {}

    if answerCount == 10:
        messagebox.showinfo("Tu vinē!")
    
        reset()



    #if btn["image"] == "pyimage6" and count < 2:
       # btn["image"] = ImageList[number]
        #count += 1 
        #Answer.append(number) 
        #Answer_dict[btn]=ImageList[number]


    #if len(Answer)==2:
            

      
     # if ImageList[Answer[0]]==ImageList[Answer[1]]:
        # for key in Answer_dict:
          # key["state"]=DISABLED
          # correctAnswer+=2
         #  if(correctAnswer==2):
          #    messagebox.showinfo("Vinē??")
           #   correctAnswer=0
            #  if(correctAnswer==6):
             #    messagebox.askquestion("ok")
           # count=0
            #correctAnswer=0
          # # Answer=[]
          #  Answer_dict={}
          #  answerCount=0


   # if ImageList[Answer[0]]==ImageList[Answer[1]]:
          #  for key in answer_dict:
          #      key["state"]=DISABLED

          #  Answer= []
        #    answer_dict = {}
         #   answerCount = 0
        # 3   correctAnswers += 1 
           # messagebox.showinfo("Vienādi attēli", "Esi uzminējis! Kopā uzminēti komplekti: " + str(correctAnswers))

   #else:
      # messagebox.showinfo("VIENāDI")
     #  for key in Answer_dict:
       #     key["image"]="pyimage6"
       #     count=0
        #    Answer=[]
        #    Answer_dict={}
         #   return 0
       
    #else :
          #  Tk.update(btn)
          #  time.sleep(0.5)
           # for key in answer_dict:
          #      key["image"] = "pyimage5"
           # answerCount = 0
         #   Answer= []
          #  answer_dict = {}


          #  if correctAnswers == 4:
          #   messagebox.showinfo("Vine")

   # return 0
def newGame():
    result = messagebox.askyesno("Jauna spele", "Vai tu esi pārliecināts, ka vēlies sākt jaunu spēli?")
   #if result:
    reset()


izvele=Menu(gw)    #Izveido opcijas
gw.config(menu=izvele)

opcijas=Menu(izvele,tearoff=FALSE)
izvele.add_cascade(label="Opcijas",menu=opcijas)
opcijas.add_command(label="Jauna spēle",command=newGame)
opcijas.add_command(label="Iziet",command=gw.quit)

izvele.add_command(label="Par programmu",command=infoLogs)




  

gw.mainloop()




#gameWindow.mainloop()