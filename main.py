from tkinter import *

root = Tk()
root.title('calculator')
root.geometry('550x550')
root.resizable(False,False)
root.configure(bg='#17161b')

equation = ''

def show(value):
    global equation
    equation+=value
    label_result.config(text=equation)
    
def clear():
    global equation
    equation = ''
    label_result.config(text=equation)
    
def calculate(value):
    global equation
    result = ''
    if equation != '':
        try:
            result=eval(equation)
        except:
            result = "error"
            equation = ''
    label_result.config(text=result)
    

label_result = Label(root,width=25,height=2,text='',font=('arial',30))
label_result.pack()

Button(root,text='C',width=4,height=1,font=('arial',30,'bold'),bd=1,fg='#fff',bg='#3697f5',command=lambda: clear()).place(x=10,y=100)
Button(root,text='/',width=4,height=1,font=('arial',30,'bold'),bd=1,fg='#fff',bg='#2a2d36',command=lambda:show('/')).place(x=150,y=100)
Button(root,text='%',width=4,height=1,font=('arial',30,'bold'),bd=1,fg='#fff',bg='#2a2d36',command=lambda:show('%')).place(x=290,y=100)
Button(root,text='*',width=4,height=1,font=('arial',30,'bold'),bd=1,fg='#fff',bg='#2a2d36',command=lambda:show('*')).place(x=420,y=100)

Button(root,text='7',width=4,height=1,font=('arial',30,'bold'),bd=1,fg='#fff',bg='#2a2d36',command=lambda:show('7')).place(x=10,y=180)
Button(root,text='8',width=4,height=1,font=('arial',30,'bold'),bd=1,fg='#fff',bg='#2a2d36',command=lambda:show('8')).place(x=150,y=180)
Button(root,text='9',width=4,height=1,font=('arial',30,'bold'),bd=1,fg='#fff',bg='#2a2d36',command=lambda:show('9')).place(x=290,y=180)
Button(root,text='-',width=4,height=1,font=('arial',30,'bold'),bd=1,fg='#fff',bg='#2a2d36',command=lambda:show('-')).place(x=420,y=180)

Button(root,text='4',width=4,height=1,font=('arial',30,'bold'),bd=1,fg='#fff',bg='#2a2d36',command=lambda:show('4')).place(x=10,y=260)
Button(root,text='5',width=4,height=1,font=('arial',30,'bold'),bd=1,fg='#fff',bg='#2a2d36',command=lambda:show('5')).place(x=150,y=260)
Button(root,text='6',width=4,height=1,font=('arial',30,'bold'),bd=1,fg='#fff',bg='#2a2d36',command=lambda:show('6')).place(x=290,y=260)
Button(root,text='+',width=4,height=1,font=('arial',30,'bold'),bd=1,fg='#fff',bg='#2a2d36',command=lambda:show('+')).place(x=420,y=260)

Button(root,text='1',width=4,height=1,font=('arial',30,'bold'),bd=1,fg='#fff',bg='#2a2d36',command=lambda:show('1')).place(x=10,y=340)
Button(root,text='2',width=4,height=1,font=('arial',30,'bold'),bd=1,fg='#fff',bg='#2a2d36',command=lambda:show('2')).place(x=150,y=340)
Button(root,text='3',width=4,height=1,font=('arial',30,'bold'),bd=1,fg='#fff',bg='#2a2d36',command=lambda:show('3')).place(x=290,y=340)
Button(root,text='0',width=10,height=1,font=('arial',30,'bold'),bd=1,fg='#fff',bg='#2a2d36',command=lambda:show('0')).place(x=10,y=420)

Button(root,text='.',width=4,height=1,font=('arial',30,'bold'),bd=1,fg='#fff',bg='#2a2d36',command=lambda:show('.')).place(x=285,y=420)
Button(root,text='=',width=4,height=3,font=('arial',30,'bold'),bd=1,fg='#fff',bg='#fe9037',command=lambda:calculate('=')).place(x=430,y=340)


root.mainloop()