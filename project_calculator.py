from tkinter import *
import math

calculation = ""

window = Tk()
window.title('Calculator')
window.geometry('600x350+700+100')
window.configure(bg='lightgray')

def input_number(symbol):
    current_text = entry.get()
    if symbol == '.' and '.' in current_text:
        return
    if symbol == '^':
        symbol = '**'
    entry.insert(END, symbol)

def clear():
    entry.delete(0, END)

def delete_last():
    current_text = entry.get()
    entry.delete(len(current_text) - 1)

def calculate_trigonometric(func):
    try:
        text = entry.get()
        angle = float(text)
        result = func(math.radians(angle))
        clear()
        entry.insert(0, result)
    except Exception as e:
        clear()
        entry.insert(0, "Ошибка")

def calculate_logarithm(log_func):
    try:
        text = entry.get()
        num = float(text)
        result = log_func(num)
        clear()
        entry.insert(0, result)
    except Exception as e:
        clear()
        entry.insert(0, "Ошибка")

def count_result():
    try:
        text = entry.get()
        result = eval(text)
        clear()
        entry.insert(0, result)
    except Exception as e:
        clear()
        entry.insert(0, "Ошибка")


entry = Entry(window, bg='grey', width=20, font=('Arial', 35))
entry.place(x=50, y=50)

btn1 = Button(window, bg='white', fg='black', text='1', command = lambda : input_number('1'))
btn1.place(x=50, y=100, width=60, height=50)

btn2 = Button(window, bg='white', fg='black', text='2', command = lambda : input_number('2'))
btn2.place(x=100, y=100, width=60, height=50)

btn3 = Button(window, bg='white', fg='black', text='3', command = lambda : input_number('3'))
btn3.place(x=150, y=100, width=60, height=50)

btn4 = Button(window, bg='white', fg='black', text='4', command = lambda : input_number('4'))
btn4.place(x=50, y=150, width=60, height=50)

btn5 = Button(window, bg='white', fg='black', text='5', command = lambda : input_number('5'))
btn5.place(x=100, y=150, width=60, height=50)

btn6 = Button(window, bg='white', fg='black', text='6', command = lambda : input_number('6'))
btn6.place(x=150, y=150, width=60, height=50)

btn7 = Button(window, bg='white', fg='black', text='7', command = lambda : input_number('7'))
btn7.place(x=50, y=200, width=60, height=50)

btn8 = Button(window, bg='white', fg='black', text='8', command = lambda : input_number('8'))
btn8.place(x=100, y=200, width=60, height=50)

btn9 = Button(window, bg='white', fg='black', text='9', command = lambda : input_number('9'))
btn9.place(x=150, y=200, width=60, height=50)

btn0 = Button(window, bg='white', fg='black', text='0', command = lambda : input_number('0'))
btn0.place(x=100, y=250, width=60, height=50)

btnplus = Button(window, bg='white', fg='black', text='+', command = lambda : input_number('+'))
btnplus.place(x=208, y=100, width=60, height=50)

btndot = Button(window, bg='white', fg='black', text='.', command = lambda : input_number('.'))
btndot.place(x=150, y=250, width=60, height=50)

btnminus = Button(window, bg='white', fg='black', text='-', command = lambda : input_number('-'))
btnminus.place(x=208, y=200, width=60, height=50)

btnmultiply = Button(window, bg='white', fg='black', text='*', command = lambda : input_number('*'))
btnmultiply.place(x=208, y=150, width=60, height=50)

btndivide = Button(window, bg='white', fg='black', text='/', command = lambda : input_number('/'))
btndivide.place(x=208, y=250, width=60, height=50)

btnresult = Button(window, bg='white', fg='black', text='=', command = count_result)
btnresult.place(x=265, y=250, width=65, height=50)

btnclear = Button(window, bg='white', fg='black', text='CE', command = clear)
btnclear.place(x=50, y=250, width=55, height=50)

btn_sin = Button(window, bg='white', fg='black', text='sin', command=lambda: calculate_trigonometric(math.sin))
btn_sin.place(x=265, y=100, width=65, height=50)

btn_cos = Button(window, bg='white', fg='black', text='cos', command=lambda: calculate_trigonometric(math.cos))
btn_cos.place(x=330, y=100, width=65, height=50)

btn_tan = Button(window, bg='white', fg='black', text='tan', command=lambda: calculate_trigonometric(math.tan))
btn_tan.place(x=265, y=150, width=65, height=50)

btn_cot = Button(window, bg='white', fg='black', text='ctg', command=lambda: calculate_trigonometric(lambda x: 1 / math.tan(x)))
btn_cot.place(x=330, y=150, width=65, height=50)

btn_log10 = Button(window, bg='white', fg='black', text='log10', command=lambda: calculate_logarithm(math.log10))
btn_log10.place(x=265, y=200, width=65, height=50)

btn_ln = Button(window, bg='white', fg='black', text='log', command=lambda: calculate_logarithm(math.log))
btn_ln.place(x=330, y=200, width=65, height=50)

btn_power = Button(window, bg='white', fg='black', text='^', command=lambda: input_number('^'))
btn_power.place(x=330, y=250, width=65, height=50)

btn_backspace = Button(window, bg='white', fg='black', text='⌫', command=delete_last)
btn_backspace.place(x=395, y=250, width=65, height=50)
window.mainloop()