import tkinter as tk
import tkinter.messagebox
import functools as fc

root = tk.Tk()
root.title('TicTacToe')
root.resizable(width=False,height=False)
def main():
    global current,free 
    x = 0

    current = 'X'
    

    def initBoard():
        global board,t0,t1,t2,t3,t4,t5,t6,t7,t8 
        board = ['','','','','','','','','']

        t0 = tk.StringVar()
        t1 = tk.StringVar()
        t2 = tk.StringVar()
        t3 = tk.StringVar()
        t4 = tk.StringVar()
        t5 = tk.StringVar()
        t6 = tk.StringVar()
        t7 = tk.StringVar()
        t8 = tk.StringVar()

    initBoard()

    def winCheck():
        global current
        if (board[0] == 'X' and board[1] == 'X' and board[2] == 'X') or (board[3] == 'X' and board[4] == 'X' and board[5] == 'X') or (board[6] == 'X' and board[7] == 'X' and board[8] == 'X') or (board[0] == 'X' and board[3] == 'X' and board[6] == 'X') or (board[1] == 'X' and board[4] == 'X' and board[7] == 'X') or (board[2] == 'X' and board[5] == 'X' and board[8] == 'X') or (board[0] == 'X' and board[4] == 'X' and board[8] == 'X') or (board[6] == 'X' and board[4] == 'X' and board[2] == 'X'):
            tkinter.messagebox.showinfo('TicTacToe','Player 1 (X) wins !!!')
            main()
        if (board[0] == 'O' and board[1] == 'O' and board[2] == 'O') or (board[3] == 'O' and board[4] == 'O' and board[5] == 'O') or (board[6] == 'O' and board[7] == 'O' and board[8] == 'O') or (board[0] == 'O' and board[3] == 'O' and board[6] == 'O') or (board[1] == 'O' and board[4] == 'O' and board[7] == 'O') or (board[2] == 'O' and board[5] == 'O' and board[8] == 'O') or (board[0] == 'O' and board[4] == 'O' and board[8] == 'O') or (board[6] == 'O' and board[4] == 'O' and board[2] == 'O'):
            tkinter.messagebox.showinfo('TicTacToe','Player 2 (O) wins !!!')
            main()
        if board[0] != '' and board[1] != '' and board[2] != '' and board[3] != '' and board[4] != '' and board[5] != '' and board[6] != '' and board[7] != '' and board[8] != '':
            tkinter.messagebox.showinfo('TicTacToe',"It's a Draw !!")
            main()
    def updateVars():
        t0.set(board[0])
        t1.set(board[1])
        t2.set(board[2])
        t3.set(board[3])
        t4.set(board[4])
        t5.set(board[5])
        t6.set(board[6])
        t7.set(board[7])
        t8.set(board[8])

    updateVars()

    def switch():
        global current
        if current == 'X':
            current = 'O'
        else:
            current = 'X'

    def addSymbol(event,numb):
        if board[numb] != 'X' and board[numb] != 'O':
            board[numb] = current
            switch()
            updateVars()
            winCheck()
            

    labX = 10
    labY = 4
    bg='white'
    
    l0 = tk.Label(root,font='100',width=labX,height=labY,relief=tk.SUNKEN,textvariable=t0,bg=bg)
    l0.bind('<Button-1>',fc.partial(addSymbol, numb=0))
    l0.grid(row=0,column=0)
    l1 = tk.Label(root,font='100',width=labX,height=labY,relief=tk.SUNKEN,textvariable=t1,bg=bg)
    l1.bind('<Button-1>',fc.partial(addSymbol, numb=1))
    l1.grid(row=0,column=1)
    l2 = tk.Label(root,font='100',width=labX,height=labY,relief=tk.SUNKEN,textvariable=t2,bg=bg)
    l2.bind('<Button-1>',fc.partial(addSymbol, numb=2))
    l2.grid(row=0,column=2)
    l3 = tk.Label(root,font='100',width=labX,height=labY,relief=tk.SUNKEN,textvariable=t3,bg=bg)
    l3.bind('<Button-1>',fc.partial(addSymbol, numb=3))
    l3.grid(row=1,column=0)
    l4 = tk.Label(root,font='100',width=labX,height=labY,relief=tk.SUNKEN,textvariable=t4,bg=bg)
    l4.bind('<Button-1>',fc.partial(addSymbol, numb=4))
    l4.grid(row=1,column=1)
    l5 = tk.Label(root,font='100',width=labX,height=labY,relief=tk.SUNKEN,textvariable=t5,bg=bg)
    l5.bind('<Button-1>',fc.partial(addSymbol, numb=5))
    l5.grid(row=1,column=2)
    l6 = tk.Label(root,font='100',width=labX,height=labY,relief=tk.SUNKEN,textvariable=t6,bg=bg)
    l6.bind('<Button-1>',fc.partial(addSymbol, numb=6))
    l6.grid(row=2,column=0)
    l7 = tk.Label(root,font='100',width=labX,height=labY,relief=tk.SUNKEN,textvariable=t7,bg=bg)
    l7.bind('<Button-1>',fc.partial(addSymbol, numb=7))
    l7.grid(row=2,column=1)
    l8 = tk.Label(root,font='100',width=labX,height=labY,relief=tk.SUNKEN,textvariable=t8,bg=bg)
    l8.bind('<Button-1>',fc.partial(addSymbol, numb=8))
    l8.grid(row=2,column=2)

main()
root.mainloop()
input()
