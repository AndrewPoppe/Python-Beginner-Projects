import tkinter as tk
import tkinter.messagebox 
import random as rn
class ticTacToe:    
    def __init__(self,master):
        global isAi,COMBS,isWin,board,current,occ
        isAi,COMBS,board,current,occ=tkinter.messagebox.askquestion('TTT','Do you want to play against AI ?'),((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)),[tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar()],'X',0
        def switch():
            global current,occ
            if current=='X':
                current='O'
            else:
                current='X'
            occ+=1
        def opposite():
            global current
            if current=='X':
                return('O')
            else:
                return('X')
        def reset():
            global board,occ,current
            for i in range(0,9):
                board[i].set('')
            occ,current=0,'X'
        def winCheck():
            global combonations,board,occ
            for i in COMBS:
                if board[i[0]].get()=='X' and board[i[1]].get()=='X' and board[i[2]].get()=='X':
                    tkinter.messagebox.showinfo('TTT',"Player X wins !")
                    reset()
                    break
                if board[i[0]].get()=='O' and board[i[1]].get()=='O' and board[i[2]].get()=='O':
                    tkinter.messagebox.showinfo('TTT',"Player O wins !")
                    reset()
                    break
            if occ==9:
                tkinter.messagebox.showinfo('TTT',"It's a Draw !")
                reset()
        def AI():
            global board,occ,COMBS
            isSet=False
            for y in (current,opposite()):
                for i in COMBS:
                    if isSet:break
                    for x in ((0,1,2),(1,2,0),(0,2,1)):
                        if board[i[x[0]]].get()==y and board[i[x[1]]].get()==y and board[i[x[2]]].get()!='X' and board[i[x[2]]].get()!='O':
                            isSet=True
                            addSymbol(i[x[2]],False)
            while not isSet:
                aiChoice=rn.randint(0,8)
                if board[aiChoice].get()!='X' and board[aiChoice].get()!='O':
                    addSymbol(aiChoice,False)
                    break                  
        def addSymbol(num,ai):
            global board,current,isAi,occ      
            if board[num].get()!='X' and board[num].get()!='O':
                board[num].set(current)
                switch()
                if isAi=='yes' and ai and occ<9: 
                    AI()
                else:
                    winCheck()
        WID,HIG=10,4
        tk.Button(master,textvariable=board[0],width=WID,height=HIG,command=lambda:addSymbol(0,True)).grid(row=0,column=0)
        tk.Button(master,textvariable=board[1],width=WID,height=HIG,command=lambda:addSymbol(1,True)).grid(row=0,column=1)
        tk.Button(master,textvariable=board[2],width=WID,height=HIG,command=lambda:addSymbol(2,True)).grid(row=0,column=2)
        tk.Button(master,textvariable=board[3],width=WID,height=HIG,command=lambda:addSymbol(3,True)).grid(row=1,column=0)
        tk.Button(master,textvariable=board[4],width=WID,height=HIG,command=lambda:addSymbol(4,True)).grid(row=1,column=1)
        tk.Button(master,textvariable=board[5],width=WID,height=HIG,command=lambda:addSymbol(5,True)).grid(row=1,column=2)
        tk.Button(master,textvariable=board[6],width=WID,height=HIG,command=lambda:addSymbol(6,True)).grid(row=2,column=0)
        tk.Button(master,textvariable=board[7],width=WID,height=HIG,command=lambda:addSymbol(7,True)).grid(row=2,column=1)
        tk.Button(master,textvariable=board[8],width=WID,height=HIG,command=lambda:addSymbol(8,True)).grid(row=2,column=2)
root=tk.Tk()
root.title('TTT')
root.resizable(0,0)
main=ticTacToe(root)
root.mainloop()