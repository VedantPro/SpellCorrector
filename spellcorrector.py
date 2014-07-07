
#############Spell Corrector###################
############Using Damerau Levenshtein Distance Algorithm#########
from Tkinter import*
import ttk
import time
import tkMessageBox
import Image,ImageTk

wordlist=[]
#####initializing list###############
D=[[0 for x in range(20)] for y in range(20)]
for i in range(0,20):
        D[i][0]=i
for j in range(0,20):
        D[0][j]=j
######Finished initializing########

###accessing Dictionary#########
Dic=open('Dictionary.txt')
for line in Dic:
        wordlist.append(line.strip())
Dic.close()

####finished accessing##########

class spellcorrect(Tk):

        def __init__(self,parent):
                 Tk.__init__(self,parent)
                 self.parent = parent
                 self.initialize()
                 

        def suggestion(self,suggest):

                self.button.place(x=80,y=150)


                self.text=Text(self,width=34,height=6,spacing1=3,spacing2=3,spacing3=3,padx=17,pady=4,relief=RIDGE,borderwidth=8,font=('BOOKMAN OLD STYLE',15),fg='blue',wrap=WORD)
                self.text.place(x=22,y=280)
                
                self.scrollbar=ttk.Scrollbar(self,orient=VERTICAL)
                self.scrollbar.place(x=455,y=288,height=183)
                
                self.text.config(yscrollcommand=self.scrollbar.set)

                self.scrollbar.config(command=self.text.yview)


                self.text.configure(state=DISABLED)

                self.quit=ttk.Button(self,text="Quit",style='B.TButton',command=self.close)
                self.quit.place(x=280,y=150)
                
                for x in suggest:
                        self.canvas.delete(self.test)
                        if self.word_user==x:
                                self.test=self.canvas.create_text(245,230,text='You wrote a correct word\nsome Suggestions for you',font=('BOOKMAN OLD STYLE',20,'bold'),fill='red')
                                suggest.remove(self.word_user)
                                break
                        else:
                                self.test=self.canvas.create_text(260,230,text='Sorry its an incorrect word\nsome Suggestions for you',font=('BOOKMAN OLD STYLE',20,'bold'),fill='red')
                if not suggest:
                        self.canvas.delete(self.test)
                        self.test=self.canvas.create_text(260,230,text='Suggestions are not available',font=('BOOKMAN OLD STYLE',20,'bold'),fill='red')
                        return
                else:
                        self.text.configure(state=NORMAL)
                        i=1
                        self.text.delete('1.0',END)
                        for a in suggest:
                                a="%d"%(i) + "." + a + "  "
                                self.text.insert('1.end',a)
                                i=i+1
                        self.text.configure(state=DISABLED)
                        
                

        def count(self,event=None):
                self.word_user=self.entry.get()
                L1=len(self.word_user)
                self.calculation(L1)

        def calculation(self,L1):
                suggest=[]
                
                for x in wordlist:
                        L2=len(x)
                        if (L2<=(L1+1)) and (L2>=(L1-1)):
                                for i in range(1,L1+1):
                                        for j in range(1,L2+1):
                                                if self.word_user[i-1]==x[j-1]:
                                                        cost=0
                                                else:
                                                        cost=1
                                                D[i][j]= min(D[i-1][j]+1,D[i][j-1]+1,D[i-1][j-1]+cost)

                                                if (i>1 and j>1 and self.word_user[i-2]==x[j-1] and self.word_user[i-1]==x[j-2]):
                                                        D[i][j]=min(D[i][j],D[i-2][j-2]+ cost)

                                if D[L1][L2]<=1:
                                        suggest.append(x)

                self.suggestion(suggest)

        def main(self,event=None):
                self.canvas.delete(self.head,self.welcome,self.start)
                self.yes.destroy()
                self.no.destroy()

                self.test=self.canvas.create_text(230,300,justify=CENTER,text='Type a word to\ntest',font=('BOOKMAN OLD STYLE',25,'bold'),fill='red')

                self.entry=Entry(self,font=('BOOKMAN OLD STYLE',20),fg='blue')
                self.entry.place(x=76,y=100)

                self.button=ttk.Button(self,text="Check",style='B.TButton',command=self.count)
                self.button.place(x=180,y=150)

                self.entry.bind("<Return>",self.count)
                self.unbind('y')
                self.unbind('n')

                
                
        def close(self):
                if tkMessageBox.askyesno("Exit","Do you want to Quit?"):
                        self.destroy()
        def initialize(self):
                
                self.canvas=Canvas(self,width=500,height=500)
                self.pic=Image.open('Pic.jpg')
                self.Image=ImageTk.PhotoImage(self.pic)
                self.canvas.create_image([150,150],image=self.Image)
                self.canvas.image=Image
                self.canvas.pack()
                
                self.head=self.canvas.create_text(245,50,text="SPELL CORRECTOR",font=('BOOKMAN OLD STYLE',30,'bold'),fill='red')
                self.welcome=self.canvas.create_text(245,190,justify=CENTER,text="Welcome!\nConfused About Spellings?\nCheck Spelling of any word\nHERE",font=('BOOKMAN OLD STYLE',25,'bold'),fill='black')
                self.start=self.canvas.create_text(245,295,justify=CENTER,text='\n\nDo You want to\nContinue?',font=('BOOKMAN OLD STYLE',25,'bold'),fill='#0000FF')
                

                self.s=ttk.Style()
                self.s.configure('B.TButton',font=('Arial',15,'bold'),foreground='blue') 

                
                self.yes=ttk.Button(self,text="YES",style='B.TButton',command=self.main)
                self.yes.place(x=50,y=400)
                self.no=ttk.Button(self,text="NO",style='B.TButton',command=self.close)
                self.no.place(x=315,y=400)
                self.bind("y",self.main)
                self.bind("n",self.close)
                
                
                
if __name__ == "__main__":
        sc = spellcorrect(None)
        sc.title('Spell Corrector')
        sc.geometry('500x500')
        sc.resizable(0,0)
        sc.mainloop()

