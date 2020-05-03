__author__ = 'Harsh'
# import send_f
# # import recieve_f
import tkinter as T
main=T.Tk()
main.geometry("420x300")
#main.resizable("500x500")
btn1=T.Button(main,text="SEND",relief="ridge",width="15")
btn1.place(x=70,y=150)
btn2=T.Button(main,text="RECIEVE",relief="solid",width="15")
btn2.place(x=290,y=150)
main.mainloop()

# choice=input("enter choice:")
# if choice==1:
#     send_f.send()
# if choice==2:
#     recieve_f.recieve()