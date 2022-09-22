import tkinter
from tkinter import *
import math

root = Tk()

def btn_click1():
    newWindow = tkinter.Toplevel(root)
    newWindow['bg']='lightblue'
    newWindow.geometry('300x200')
    labelExample = tkinter.Label(newWindow, text="Завдання 1", fg='blue', bg='lightblue')
    labelExample.pack()
    inputX = Entry(newWindow, bg='white')
    inputX.pack()
    inputY = Entry(newWindow, bg='white')
    inputY.pack()


    def lb2_command():
        x = int(inputX.get())
        y = int(inputY.get())
        rez1 = x + y
        rez2 = x * y
        lb2 = Label(newWindow, text=("Сумма=",rez1), fg="black", bg="lightblue")
        lb2.pack()
        lb2 = Label(newWindow, text=('Произведение=',rez2), fg="black", bg="lightblue")
        lb2.pack()

    buttonExample = tkinter.Button(newWindow, text="Ввести", command=lb2_command, bg="white")


    buttonExample.pack()

def btn_click2():
    newWindow = tkinter.Toplevel(root)
    newWindow['bg'] = 'lightblue'
    newWindow.geometry('450x200')
    frame1 = Frame(newWindow, bg='#9966CC')
    frame1.place(relx=0.04, rely=0.055, relwidth=0.916, relheight=0.90)
    labelExample = tkinter.Label(newWindow, text="Завдання 2", fg='blue', bg='lightblue')
    labelExample.pack()
    inputX = Entry(frame1, bg='white')
    inputX.place(x=20, y=30)
    inputY = Entry(frame1, bg='white')
    inputY.place(x=20,y=60)
    inputZ= Entry(frame1, bg='white')
    inputZ.place(x=20, y=90)
    label0= Label(frame1, text="x", fg='lightblue', bg='#9966CC' )
    label0.place(x=5, y=30)
    label1 = Label(frame1, text="y", fg='lightblue', bg='#9966CC')
    label1.place(x=5, y=60)
    label2 = Label(frame1, text="z", fg='lightblue', bg='#9966CC')
    label2.place(x=5, y=90)

    def click():
        x = int(inputX.get())
        y = int(inputY.get())
        z = int(inputZ.get())
        rez1 = x * 2
        rez2 = y+3
        rez3 = math.pow(z, 2)
        rez4= rez1+ rez2+rez3
        lb2 = Label(frame1, text=("Первое число=", rez1), fg="black", bg="lightblue")
        lb2.place(x=170, y=30)
        lb3 = Label(frame1, text=('Второе число=', rez2), fg="black", bg="lightblue")
        lb3.place(x=170, y=60)
        lb3 = Label(frame1, text=('Третье число=', rez3), fg="black", bg="lightblue")
        lb3.place(x=170, y=90)
        lb3 = Label(frame1, text=('Сумма чисел=', rez4), fg="black", bg="lightblue")
        lb3.place(x=170, y=120)

    buttonExample = tkinter.Button(frame1, text="Ввести", command=click, bg="white")

    buttonExample.place(x=50, y=140)

def btn_click3():
    newWindow = tkinter.Toplevel(root)
    newWindow['bg'] = 'lightblue'
    newWindow.geometry('350x200')
    frame1 = Frame(newWindow, bg='#9966CC')
    frame1.place(relx=0.04, rely=0.055, relwidth=0.916, relheight=0.90)
    labelExample = tkinter.Label(newWindow, text="Завдание 3", fg='blue', bg='lightblue')
    labelExample.pack()
    inputX = Entry(frame1, bg='white')
    inputX.place(x=170, y=30)

    label0= Label(frame1, text="Введите сторону квадрата:", font="ProunX 8 bold", fg='lightblue', bg='#9966CC' )
    label0.place(x=5, y=30)


    def click():
        x = int(inputX.get())

        rez1 = x * 4
        rez2 = math.pow(x, 2)

        lb2 = Label(frame1, text=("Периметр квадрата=", rez1), fg="black", bg="lightblue")
        lb2.place(x=5, y=60)
        lb3 = Label(frame1, text=("Площадь квадрата=", rez2), fg="black", bg="lightblue")
        lb3.place(x=170, y=60)


    buttonExample = tkinter.Button(frame1, text="Расчитать", command=click, bg="white")

    buttonExample.place(x=120, y=100)

def btn_click4():
    newWindow = tkinter.Toplevel(root)
    newWindow['bg'] = 'lightblue'
    newWindow.geometry('350x200')
    frame1 = Frame(newWindow, bg='#9966CC')
    frame1.place(relx=0.04, rely=0.055, relwidth=0.916, relheight=0.90)
    labelExample = tkinter.Label(newWindow, text="Завдание 4", fg='blue', bg='lightblue')
    labelExample.pack()
    label01 = Label(frame1, text=""" 
    """, font="ProunX 9 bold", bg='#9966CC')
    label01.pack()
    label0 = Label(frame1, text="километров в час", font="ProunX 9 bold", fg='lightblue', bg='#9966CC')
    label0.pack()
    inputX = Entry(frame1, bg='white')
    inputX.pack()





    def click():
        x = int(inputX.get())
        rez1 = (x * 5)/18


        lb2 = Label(frame1, text=("Метры в секунду=", rez1, "м/сек"), fg="black", bg="lightblue")
        lb2.place(x=50, y=130)



    buttonExample = tkinter.Button(frame1, text="Перевести в метры за секунду", command=click, bg="white")

    buttonExample.place(x=75, y=100)

def btn_click5():
    newWindow = tkinter.Toplevel(root)
    newWindow['bg'] = 'lightblue'
    newWindow.geometry('350x200')
    frame1 = Frame(newWindow, bg='#9966CC')
    frame1.place(relx=0.04, rely=0.055, relwidth=0.916, relheight=0.90)
    labelExample = tkinter.Label(newWindow, text="Завдання 5", fg='blue', bg='lightblue')
    labelExample.pack()
    inputX = Entry(frame1, bg='white')
    inputX.place(x=100, y=30)
    inputY = Entry(frame1, bg='white')
    inputY.place(x=150,y=60)
    inputZ= Entry(frame1, bg='white')
    inputZ.place(x=150, y=90)
    label0= Label(frame1, text="Введите сумму:", fg='lightblue', bg='#9966CC' )
    label0.place(x=5, y=30)
    label1 = Label(frame1, text="Введите количество дней:", fg='lightblue', bg='#9966CC')
    label1.place(x=5, y=60)
    label2 = Label(frame1, text="Введите процент скидки:", fg='lightblue', bg='#9966CC')
    label2.place(x=5, y=90)

    def click():
        x = int(inputX.get())
        y = int(inputY.get())
        z = int(inputZ.get())
        rez1 = ((y*(x+3))*z)+(((y*(x+3))*z)/100)

        lb2 = Label(frame1, text=("Прибыль=", rez1), fg="black", bg="lightblue")
        lb2.place(x=130, y=140)


    buttonExample = tkinter.Button(frame1, text="Ввести", command=click, bg="white")

    buttonExample.place(x=50, y=140)

def btn_click6():
    newWindow = tkinter.Toplevel(root)
    newWindow['bg'] = 'lightblue'
    newWindow.geometry('550x220')
    frame1 = Frame(newWindow, bg='#9966CC')
    frame1.place(relx=0.04, rely=0.055, relwidth=0.916, relheight=0.90)
    labelExample = tkinter.Label(newWindow, text="Завдання 5", fg='blue', bg='lightblue')
    labelExample.pack()
    inputX = Entry(frame1, bg='white')
    inputX.place(x=120, y=30)
    inputY = Entry(frame1, bg='white')
    inputY.place(x=140,y=60)
    inputZ= Entry(frame1, bg='white')
    inputZ.place(x=145, y=90)
    label0= Label(frame1, text="Количество недель:", fg='lightblue', bg='#9966CC' )
    label0.place(x=5, y=30)
    label1 = Label(frame1, text="Количество месяцев:", fg='lightblue', bg='#9966CC')
    label1.place(x=5, y=60)
    label2 = Label(frame1, text="Количество лет(годов):", fg='lightblue', bg='#9966CC')
    label2.place(x=5, y=90)

    def click():
        x = int(inputX.get())
        y = int(inputY.get())
        z = int(inputZ.get())
        rez1 = x*7
        rez2= y*30
        rez3= z*365
        rez4=rez1+rez2+rez3

        lb2 = Label(frame1, text=("Дней за ", x," недель=", rez1), fg="black", bg="lightblue")
        lb2.place(x=300, y=30)
        lb3 = Label(frame1, text=('Дней за ', y," месяцев(а)=", rez2), fg="black", bg="lightblue")
        lb3.place(x=300, y=60)
        lb3 = Label(frame1, text=('Дней за', z," года(лет)=", rez3), fg="black", bg="lightblue")
        lb3.place(x=300, y=90)
        lb3 = Label(frame1, text=('Дней за весь период=', rez4), fg="black", bg="lightblue")
        lb3.place(x=300, y=120)


    buttonExample = tkinter.Button(frame1, text="Ввести", command=click, bg="white")

    buttonExample.place(x=50, y=140)

def btn_click7():
    newWindow = tkinter.Toplevel(root)
    newWindow['bg'] = 'lightblue'
    newWindow.geometry('450x200')
    frame1 = Frame(newWindow, bg='#9966CC')
    frame1.place(relx=0.04, rely=0.055, relwidth=0.916, relheight=0.90)
    labelExample = tkinter.Label(newWindow, text="Завдання 7", fg='blue', bg='lightblue')
    labelExample.pack()
    inputX = Entry(frame1, bg='white')
    inputX.place(x=100, y=30)
    inputY = Entry(frame1, bg='white')
    inputY.place(x=160,y=60)
    label1 = Label(frame1, text="Сумма вклада:", fg='lightblue', bg='#9966CC')
    label1.place(x=5, y=30)
    label2 = Label(frame1, text="Введите процент депозита:", fg='lightblue', bg='#9966CC')
    label2.place(x=5, y=60)

    def click():
        x = int(inputX.get())
        y = int(inputY.get())
        rez1=x
        rez1 +=((x*5)*y)/100
        rez2=x
        z=90
        for i in range(5):
            rez2=rez2+((rez2*y)/100)
            lb3 = Label(frame1, text=('Прибыль зa ', i+1,'год=', rez2), fg="black", bg="lightblue")
            lb3.place(x=300, y=z)
            z+=30


        lb2 = Label(frame1, text=("Прибыль=", rez1), fg="black", bg="lightblue")
        lb2.place(x=300, y=30)
        lb2 = Label(frame1, text=("Прибыль с ежегодным начислением=", rez2), fg="black", bg="lightblue")
        lb2.place(x=300, y=60)


    buttonExample = tkinter.Button(frame1, text="Ввести", command=click, bg="white")

    buttonExample.place(x=50, y=140)

def btn_click10():
    newWindow = tkinter.Toplevel(root)
    newWindow['bg']='lightblue'
    newWindow.geometry('500x300')
    labelExample = tkinter.Label(newWindow, text="""
1. Користувач вводить два числа. Знайти суму та добуток даних чисел
2. Користувач вводить три числа. Збільшіть перше число в два рази, друге
число зменшіть на 3, третє піднесіть до квадрату, а потім знайдіть суму усіх
трьох нових чисел.
3. Користувач вводить сторону квадрату. Знайдіть периметр та площу
квадрату.
4. Користувач вводить час в хвилинах та відстань в кілометрах. Знайдіть
швидкість в м/с
5. Користувач вводить кількість днів, вказує процент знижки та вводить
суму. Розрахувати прибуток, якщо за кожен день сума збільшується на 3грн а
потім застосовується знижка, тобто підсумок ще збільшується на дане число
відсотків.
6. Користувач вводить кількість тижнів, місяців, років та отримує кількість
 днів за цей час (по кожному окремо та по усім разом). Вважати, що місяць
має 30 днів
7. Користувач вводить суму вкладу в банк та річний процент. Знайдіть суму
вкладу через 5 років (розглянути два способи нарахування відсотків –
одноразово або щомісячно).

                                                 
                                                 """, fg='blue')


    labelExample.pack()

def exit():
    root.destroy()

root['bg']='#9966FF'
root.title('Practik 11')
root.geometry('320x350')
frame = Frame(root, bg='#9966CC')
frame.place(relx=0.04, rely=0.055, relwidth=0.916, relheight=0.90)
#title = Label(frame, text='Введіть х та у:', g='white', font= 40)
#title.place(x=20, y=60)

lab1= Label(frame, text='"Практическая работа tkinter"', fg='white', bg='#9966CC', font='terminal 15')
lab1.place(x=40, y=10)

btn1 = Button(frame, text='Завдання 1', bg='#FFEBCD', activebackground='#BDB76B', command=btn_click1)
btn1.place(x=10, y=50)

btn2 = Button(frame, text='Завдання 2', bg='#FFEBCD', activebackground='#BDB76B', command=btn_click2)
btn2.place(x=110, y=50)

btn3 = Button(frame, text='Завдання 3', bg='#FFEBCD', activebackground='#BDB76B', command=btn_click3)
btn3.place(x=210, y=50)

btn4 = Button(frame, text='Завдання 4', bg='#FFE4C4', activebackground='#BDB76B', command=btn_click4)
btn4.place(x=10, y=110)


btn5 = Button(frame, text='Завдання 5', bg='#FFE4C4', activebackground='#BDB76B', command=btn_click5)
btn5.place(x=110, y=110)

btn6 = Button(frame, text='Завдання 6', bg='#FFE4C4', activebackground='#BDB76B', command=btn_click6)
btn6.place(x=210, y=110)

btn7 = Button(frame, text='Завдання 7', bg='#FFDEAD', activebackground='black', command=btn_click7)
btn7.place(x=110, y=160)

btn7 = Button(frame, text='Вихід', bg='#FFDEAD', activebackground='black', command=exit)
btn7.place(x=230, y=260)

btn8 = Button(frame, text='  ?  ', bg='#FFDEAD', activebackground='black', command=btn_click10)
btn8.place(x=10, y=260)

#inputX=Entry(frame, bg= 'white')
#inputX.pack()

#inputY=Entry(frame, bg='white')
#inputY.pack()

root.mainloop()

