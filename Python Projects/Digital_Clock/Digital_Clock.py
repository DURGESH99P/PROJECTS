from tkinter import *
import time

clk=Tk()
clk.title("Clock")
clk.geometry("600x200+550+300") # width, height , x-axis , y-axis we have kept 0 because we will start from left top corner
clk.config(bg='#000000')

def clock():
    hr=str(time.strftime('%H'))
    min=str(time.strftime('%M'))
    sec=str(time.strftime('%S'))
    print(hr,min,sec)

    if int(hr)>12 and int(min)>0:
        lb_dn_txt.config(text='PM')
    if int(hr)>12:
        hr=str(int(int(hr)-12))
    lb_hr.config(text=hr)
    lb_min.config(text=min)
    lb_sec.config(text=sec)

    lb_hr.after(200,clock)    # To make clock exery second

# Hr section
lb_hr=Label(clk,text='12',font=('Times 20 bold',75,'bold'),bg='#000000',fg='#0099FF')
lb_hr.place(x=0,y=0,width=150,height=150)

lb_hr_txt=Label(clk,text='Hour',font=('Times 20 bold',20,'bold'),bg='#000000',fg='#0099FF')
lb_hr_txt.place(x=0,y=150,width=150,height=50)

# Min Section
lb_min=Label(clk,text='12',font=('Times 20 bold',75,'bold'),bg='#000000',fg='#0099FF')
lb_min.place(x=150,y=0,width=150,height=150)

lb_min_txt=Label(clk,text='Minute',font=('Times 20 bold',20,'bold'),bg='#000000',fg='#0099FF')
lb_min_txt.place(x=150,y=150,width=150,height=50)

# Min Section
lb_sec=Label(clk,text='12',font=('Times 20 bold',75,'bold'),bg='#000000',fg='#0099FF')
lb_sec.place(x=300,y=0,width=150,height=150)

lb_sec_txt=Label(clk,text='Second',font=('Times 20 bold',20,'bold'),bg='#000000',fg='#0099FF')
lb_sec_txt.place(x=300,y=150,width=150,height=50)



lb_dn_txt=Label(clk,text='AM',font=('Times 20 bold',50,'bold'),bg='#000000',fg='#0099FF')
lb_dn_txt.place(x=450,y=0,width=150,height=150)


clock()
clk.mainloop()





