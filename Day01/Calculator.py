
### Calculator using Tkinter

from tkinter import *

first_number=second_number=operator=None

def get_digit(digit):
    current = result_label['text']
    new = current + str(digit)
    result_label.config(text=new)

def clear():
    result_label.config(text='')

def get_operator(op):
    global first_number,operator

    first_number = int(result_label['text'])
    operator = op
    result_label.config(text='')

def get_result():
    global first_number,second_number,operator

    second_number = int(result_label['text'])

    if operator == '+':
        result_label.config(text=str(first_number+second_number))
    elif operator == '-':
        result_label.config(text=str(first_number - second_number))
    elif operator == '*':
        result_label.config(text=str(first_number * second_number))
    else:
        if second_number == 0:
            result_label.config(text='Error')
        else:
            result_label.config(text=str(round(first_number / second_number,2)))



# GUI intraction
window = Tk()
#  Add title to window
window.title("Calculator")
#  Add icon to the window
window.iconbitmap('calc_icon.ico')
#  size of the window
window.geometry("420x380")
window.resizable(0,0)
#background colour
window.configure(background='#F18853')

result_label = Label(window,text='',bg='#F18853',fg='white')
result_label.grid(row=0,column=0,columnspan=5,pady=(50,25),sticky='w')
result_label.config(font=('verdana',30,'bold'))


Button_7 = Button(window,text='7',bg='#00a65a',fg='white',width=8,height=2,command=lambda :get_digit(7))
Button_7.grid(row=1,column=0)
Button_7.config(font=('verdana',14))

Button_8 = Button(window,text='8',bg='#00a65a',fg='white',width=8,height=2,command=lambda :get_digit(8))
Button_8.grid(row=1,column=1)
Button_8.config(font=('verdana',14))

Button_9 = Button(window,text='9',bg='#00a65a',fg='white',width=8,height=2,command=lambda :get_digit(9))
Button_9.grid(row=1,column=2)
Button_9.config(font=('verdana',14))

Button_add = Button(window,text='+',bg='#EB7322',fg='white',width=8,height=2,command=lambda :get_operator('+'))
Button_add.grid(row=1,column=3)
Button_add.config(font=('verdana',14))

Button_4 = Button(window,text='4',bg='#00a65a',fg='white',width=8,height=2,command=lambda :get_digit(4))
Button_4.grid(row=2,column=0)
Button_4.config(font=('verdana',14))

Button_5 = Button(window,text='5',bg='#00a65a',fg='white',width=8,height=2,command=lambda :get_digit(5))
Button_5.grid(row=2,column=1)
Button_5.config(font=('verdana',14))

Button_6 = Button(window,text='6',bg='#00a65a',fg='white',width=8,height=2,command=lambda :get_digit(6))
Button_6.grid(row=2,column=2)
Button_6.config(font=('verdana',14))

Button_sub = Button(window,text='-',bg='#EB7322',fg='white',width=8,height=2,command=lambda :get_operator('-'))
Button_sub.grid(row=2,column=3)
Button_sub.config(font=('verdana',14))

Button_1 = Button(window,text='1',bg='#00a65a',fg='white',width=8,height=2,command=lambda :get_digit(1))
Button_1.grid(row=3,column=0)
Button_1.config(font=('verdana',14))

Button_2 = Button(window,text='2',bg='#00a65a',fg='white',width=8,height=2,command=lambda :get_digit(2))
Button_2.grid(row=3,column=1)
Button_2.config(font=('verdana',14))

Button_3 = Button(window,text='3',bg='#00a65a',fg='white',width=8,height=2,command=lambda :get_digit(3))
Button_3.grid(row=3,column=2)
Button_3.config(font=('verdana',14))

Button_mul = Button(window,text='*',bg='#EB7322',fg='white',width=8,height=2,command=lambda :get_operator('*'))
Button_mul.grid(row=3,column=3)
Button_mul.config(font=('verdana',14))

Button_clr = Button(window,text='C',bg='#DCDEDB',fg='white',width=8,height=2,command=lambda :clear())
Button_clr.grid(row=4,column=0)
Button_clr.config(font=('verdana',14))

Button_0 = Button(window,text='0',bg='#00a65a',fg='white',width=8,height=2,command=lambda :get_digit(0))
Button_0.grid(row=4,column=1)
Button_0.config(font=('verdana',14))

Button_equals = Button(window,text='=',bg='#EB7322',fg='white',width=8,height=2,command=get_result)
Button_equals.grid(row=4,column=2)
Button_equals.config(font=('verdana',14))

Button_div = Button(window,text='/',bg='#EB7322',fg='white',width=8,height=2,command=lambda :get_operator('/'))
Button_div.grid(row=4,column=3)
Button_div.config(font=('verdana',14))


window.mainloop()
