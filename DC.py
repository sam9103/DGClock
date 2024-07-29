from datetime import datetime
from tkinter import *
from tkinter.messagebox import showinfo
from time import sleep
from PIL import Image,ImageTk
import winsound 
import pytz

mw = Tk()
mw.title("Digital Clock")
mw.geometry("1000x1000+100+100")
mw.configure(bg='black')
f=("Arial",40,"bold")
f1=("Calibri",20,"italic")
f2=("Arial",5,"italic")


img = ImageTk.PhotoImage(Image.open("dc.png"))
panel = Label(mw, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")

# Time

def update_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S %p")
    time_display.config(text=current_time)
    mw.after(1000, update_time)

time_display = Label(mw, font=f,fg="white",bg="black")
time_display.place(x=350,y=380)
update_time()


# date 
now = datetime.now()
current_date = now.strftime("%d/%m/%Y")

date_display = Label(mw, text=current_date, font=f1,fg="dark blue",bg="light blue")
date_display.place(x=425,y=470)
             

def f1():
	sw.deiconify()
	mw.withdraw()
	
def f2():
	mw.deiconify()
	sw.withdraw()
def f3():
	tw.deiconify()
	sw.withdraw()
def f4():
	mw.deiconify()
	tw.withdraw()
	
#world clock

wd_btn=Button(mw,text="World Clock",font=f2,bg="gray",fg="black",command=f1)
wd_btn.place(x=540,y=330)

sw=Toplevel(mw)
sw.title("World Clock")
sw.geometry("1000x1000+100+100")
btn2=Button(sw,text="Back",font=f2,command=f2,bg="blue",fg="light green")
btn2.pack(pady=100)
sw.withdraw()

img1 = ImageTk.PhotoImage(Image.open("wc.png"))
panel1 = Label(sw, image = img1)
panel1.pack(side = "bottom", fill = "both", expand = "yes")


lab_wc=Label(sw,text="World Clock",font=f2,bg="black",fg="SlateBlue2")
lab_wc.place(x=430,y=420)


country_time_zone = pytz.timezone('Europe/London')
country_time = datetime.now(country_time_zone)
LD=country_time.strftime(" Date:%d-%m-%y \n Time: %H:%M:%S %p")
LD_name=Label(sw,text="London:",font=f2,fg="deep pink",bg="white")
LD_name.place(x=350,y=450)
LD_time=Label(sw,text=LD,font=f2,fg="gray",bg="black")
LD_time.place(x=350,y=475)


country_time_zone = pytz.timezone('Australia/Sydney')
country_time = datetime.now(country_time_zone)
SY=country_time.strftime(" Date:%d-%m-%y \n Time: %H:%M:%S %p")
SY_name=Label(sw,text="Sydney:",font=f2,fg="red",bg="white")
SY_name.place(x=540,y=450)
SY_time=Label(sw,text=SY,font=f2,fg="gray",bg="black")
SY_time.place(x=540,y=475)

country_time_zone = pytz.timezone('Asia/Kolkata')
country_time = datetime.now(country_time_zone)
KK=country_time.strftime(" Date:%d-%m-%y \n Time: %H:%M:%S %p")
KK_name=Label(sw,text="Kolkata:",font=f2,fg="dark blue",bg="white")
KK_name.place(x=350,y=535)
KK_time=Label(sw,text=KK,font=f2,fg="gray",bg="black")
KK_time.place(x=350,y=560)


country_time_zone = pytz.timezone('Japan')
country_time = datetime.now(country_time_zone)
JP=country_time.strftime(" Date:%d-%m-%y \n Time: %H:%M:%S%p")
JP_name=Label(sw,text="Japan:",font=f2,fg="brown",bg="white")
JP_name.place(x=540,y=535)
JP_time=Label(sw,text=JP,font=f2,fg="gray",bg="black")
JP_time.place(x=540,y=560)


#countdown timer

tw_btn=Button(mw,text="Countdown Timer",font=f2,bg="gray",fg="black",command=f3)
tw_btn.place(x=350,y=330)

tw=Toplevel(mw)
tw.title("Countdown Timer")
tw.geometry("1000x1000+100+100")
tw_btn=Button(tw,text="Back",font=f2,command=f2,bg="blue",fg="light green")
tw_btn.pack(pady=100)
tw.withdraw()
img2 = ImageTk.PhotoImage(Image.open("cd.png"))
panel2 = Label(tw, image = img2)
panel2.pack(side = "bottom", fill = "both", expand = "yes")


spw=Label(tw,text="Countdown Timer",font=f1,fg="pink",bg="black")
spw.place(x=450,y=430)


hourString = StringVar()
minuteString = StringVar()
secondString = StringVar()

hourString.set("00")
minuteString.set("00")
secondString.set("00")

hourTextbox = Entry(tw, font=f, width=3, textvariable=hourString)
minuteTextbox = Entry(tw, font=f, width=3, textvariable=minuteString)
secondTextbox = Entry(tw, font=f, width=3, textvariable=secondString)

hourTextbox.place(x=350, y=490)
minuteTextbox.place(x=450, y=490)
secondTextbox.place(x=550, y=490)

def runTimer():
    try:
        clockTime = int(hourString.get()) * 3600 + int(minuteString.get()) * 60 + int(secondString.get())
    except ValueError:
        print("Incorrect values")

    while clockTime > -1:
        totalMinutes, totalSeconds = divmod(clockTime, 60)
        totalHours, totalMinutes = divmod(totalMinutes, 60)

        hourString.set("{0:02d}".format(totalHours))
        minuteString.set("{0:02d}".format(totalMinutes))
        secondString.set("{0:02d}".format(totalSeconds))

        tw.update()
        sleep(1)

        if clockTime == 0:
        	winsound.PlaySound("alarm sound.wav",winsound.SND_ASYNC)
        	showinfo("", "Time's Up!")

        clockTime -= 1
	
setTimeButton = Button(tw, text='Set Time', font=f2, command=runTimer)
setTimeButton.place(x=460, y=590)





mw.mainloop()





