from tkinter import *
import time


clk=Tk()
clk.title("Clock")
clk.geometry("700x450+550+300") # width, height , x-axis , y-axis we have kept 0 because we will start from left top corner
clk.config(bg='#000000')

def clock():
    month=str(time.strftime('%m'))
    day=str(time.strftime('%d'))
    year=str(time.strftime('%Y'))
    hr=str(time.strftime('%H'))
    min=str(time.strftime('%M'))
    sec=str(time.strftime('%S'))
    print(month,day,year,hr,min,sec)

    if int(hr)>12 and int(min)>0:
        lb_dn_txt.config(text='  PM')
    if int(hr)>12:
        hr=str(int(int(hr)-12))


    months=['Jan','Feb','Mar','April','May','June','July','Aug','Sept','Oct','Nov','Dec']    
    a=int(month.strip("0"))
    lb_month.config(text=(months[a-1]))
    lb_date_txt.config(text=f'{day} / {month} / {year}')
    lb_year_txt.config(text=f' Year \n{year}')
    



    
    lb_hr.config(text=hr)
    lb_min.config(text=min)
    lb_sec.config(text=sec)

    lb_hr.after(200,clock)    # To make clock exery second

# day Section
lb_day=Label(clk,text='  Day \n Monday',font=('Times 20 bold',20,'bold'),bg='#000000',fg='#FF0000')
lb_day.place(x=0,y=0,width=150,height=150)


# month Section
lb_month=Label(clk,text='  Month \n January',font=('Times 20 bold',20,'bold'),bg='#000000',fg='#FF0000')
lb_month.place(x=150,y=0,width=150,height=150)


# Year Section
lb_year_txt=Label(clk,text=' Year \n2022',font=('Times 20 bold',20,'bold'),bg='#000000',fg='#FF0000')
lb_year_txt.place(x=300,y=0,width=150,height=150)

#Date Section
lb_date_txt=Label(clk,text=' Date \n 01',font=('Times 20 bold',20,'bold'),bg='#000000',fg='#FF0000')
lb_date_txt.place(x=450,y=0,width=250,height=150)





# Hr section
lb_hr=Label(clk,text='12',font=('Times 20 bold',75,'bold'),bg='#000000',fg='#0099FF')
lb_hr.place(x=50,y=200,width=150,height=150)

lb_hr_txt=Label(clk,text='Hour',font=('Times 20 bold',20,'bold'),bg='#000000',fg='#0099FF')
lb_hr_txt.place(x=50,y=350,width=150,height=50)

# Min Section
lb_min=Label(clk,text='12',font=('Times 20 bold',75,'bold'),bg='#000000',fg='#0099FF')
lb_min.place(x=200,y=200,width=150,height=150)

lb_min_txt=Label(clk,text='Minute',font=('Times 20 bold',20,'bold'),bg='#000000',fg='#0099FF')
lb_min_txt.place(x=200,y=350,width=150,height=50)

# Min Section
lb_sec=Label(clk,text='12',font=('Times 20 bold',75,'bold'),bg='#000000',fg='#0099FF')
lb_sec.place(x=350,y=200,width=150,height=150)

lb_sec_txt=Label(clk,text='Second',font=('Times 20 bold',20,'bold'),bg='#000000',fg='#0099FF')
lb_sec_txt.place(x=350,y=350,width=150,height=50)

# Day night
lb_dn_txt=Label(clk,text='  AM',font=('Times 20 bold',50,'bold'),bg='#000000',fg='#0099FF')
lb_dn_txt.place(x=500,y=200,width=200,height=200)


clock()
clk.mainloop()





