import tkinter as tk 
import tkinter.messagebox
import random as rn
class ticTacToe:
    def __init__(self,master):
        global isAi,combinations,isWin
        isAi = tkinter.messagebox.askquestion('TTT','Do you want to play against AI ?')
        combinations=((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
        isWin=False
        def initBoard():
            global board,current,occ
            board=[tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar()]
            current='X'
            occ=0
        def switch():
            global current,occ
            if current=='X':
                current='O'
            else:
                current='X'
            occ+=1
        def reset():
            global board,occ,current,isWin
            for i in range(0,9):
                board[i].set('')
            occ=0
            current='X'
            isWin=False
        def winCheck():
            global combonations,board,occ
            for i in combinations:
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
        def AI(num):
            global board,occ
            corners=(0,2,6,8)
            sides=(1,3,5,7,4)
            isSet=False
            if occ<9:
                for i in corners:
                    if num == i:
                        for x in range(0,20):         
                            aiChoice=rn.choice(sides)
                            if board[aiChoice].get()!='X' and board[aiChoice].get()!='O':
                                addSymbol(aiChoice,False)
                                isSet=True
                                break
                for i in sides:
                    if num == i:
                        for x in range(0,20):
                            aiChoice=rn.choice(corners)
                            if board[aiChoice].get()!='X' and board[aiChoice].get()!='O':
                                addSymbol(aiChoice,False)
                                isSet=True
                                break
                while not isSet:
                    aiChoice=rn.randint(0,8)
                    if board[aiChoice].get()!='X' and board[aiChoice].get()!='O':
                        addSymbol(aiChoice,False)
                        isSet=True
        def addSymbol(num,ai):
            global board,current,isAi      
            if board[num].get()!='X' and board[num].get()!='O':
                board[num].set(current)
                switch()
                if isAi=='yes' and ai:
                    AI(num)
                winCheck()
                
        initBoard()
        wid,hig=10,4
        tk.Button(master,textvariable=board[0],width=wid,height=hig,command=lambda:addSymbol(0,True)).grid(row=0,column=0)
        tk.Button(master,textvariable=board[1],width=wid,height=hig,command=lambda:addSymbol(1,True)).grid(row=0,column=1)
        tk.Button(master,textvariable=board[2],width=wid,height=hig,command=lambda:addSymbol(2,True)).grid(row=0,column=2)
        tk.Button(master,textvariable=board[3],width=wid,height=hig,command=lambda:addSymbol(3,True)).grid(row=1,column=0)
        tk.Button(master,textvariable=board[4],width=wid,height=hig,command=lambda:addSymbol(4,True)).grid(row=1,column=1)
        tk.Button(master,textvariable=board[5],width=wid,height=hig,command=lambda:addSymbol(5,True)).grid(row=1,column=2)
        tk.Button(master,textvariable=board[6],width=wid,height=hig,command=lambda:addSymbol(6,True)).grid(row=2,column=0)
        tk.Button(master,textvariable=board[7],width=wid,height=hig,command=lambda:addSymbol(7,True)).grid(row=2,column=1)
        tk.Button(master,textvariable=board[8],width=wid,height=hig,command=lambda:addSymbol(8,True)).grid(row=2,column=2)
root=tk.Tk()
root.title('TTT')
main=ticTacToe(root)
root.mainloop()