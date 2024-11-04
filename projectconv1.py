import tkinter
from tkinter import *
import pymysql
from tkinter import messagebox
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
from PIL import ImageTk,Image
import os

def autherization():
    un=em1.get()
    ps=em2.get()
    
    if un=='' and ps== '':
        messagebox.showerror('LOGIN','Enter ID and PASSWORD')
    elif un=='ANKITA' and ps=='admin':
        messagebox.showinfo('LOGIN', 'LOGIN SUCCESSFUL')
        SCM.destroy()
        SC=tkinter.Tk()
        SC.geometry('1160x1160')
        SC.title('STOCK MAGANGEMENT')
        SC.maxsize(1160,1160)
        
        def scr():
            c4=Canvas(SC,height=1160,width=800,bg='lavender')
            c4.place(x=360,y=0)
            
            ax=Label(c4,text=' STOCK ',bg='purple',fg='lavender',font=('arial',50))
            ax.place(x=265,y=130)
            ay=Label(c4,text=' MANAGEMENT ',bg='purple',fg='lavender',font=('arial',50))
            ay.place(x=160,y=280)
            az=Label(c4,text=' SYSTEM ',bg='purple',fg='lavender',font=('arial',50))
            az.place(x=250,y=430)
           

        def deleteimg():
            if(os.path.exists('console_image')):
                os.rmdir('console_image')
            elif(os.path.exists('console_image1')):
                os.rmdir('console_image1')
             
        def com():
            c2=Canvas(SC,height=1160,width=180,bg='violet')
            c2.place(x=180,y=0)
            def cosavedatabt():
                c3=Canvas(SC,height=1160,width=800,bg='lavender')
                c3.place(x=360,y=0)
                def savedata():
                    if len(A.get())==0 or len(B.get())==0 or len(C.get())==0 or len(D.get())==0 or len(E.get())==0 or len(H.get())==0 :
                        messagebox.showerror('ERROR','ENTER VAILD DATA')
                    else:
                        db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                        cur=db.cursor()
                        xa=A.get()
                        xb=B.get()
                        xc=C.get()
                        xd=D.get()
                        xe=E.get()
                        xh=H.get()
                        sql="insert into company values('%s','%s','%s','%s','%s','%s')"%(xa,xb,xc,xd,xe,xh)
                        cur.execute(sql)
                        db.commit()
                        messagebox.showinfo('Screen','SAVED')
                        db.close()
                        A.delete(0,100)
                        B.delete(0,100)
                        C.delete(0,100)
                        D.delete(0,100)
                        E.delete(0,100)
                        H.delete(0,100)
                        c3.destroy()
                        scr()
                def closebt():
                    c3.destroy()
                    scr()
                
                a=Label(c3,text='COMPANY ID',font=('arial',15),bg='lavender')
                a.place(x=50,y=120)
                A=Entry(c3,width=50)
                A.place(x=200,y=125)
                b=Label(c3,text='NAME',font=('arial',15),bg='lavender')
                b.place(x=50,y=190)
                B=Entry(c3,width=50)
                B.place(x=200,y=195)
                c=Label(c3,text='ADDRESS',font=('arial',15),bg='lavender')
                c.place(x=50,y=260)
                C=Entry(c3,width=50)
                C.place(x=200,y=265)
                d=Label(c3,text='PHONE',font=('arial',15),bg='lavender')
                d.place(x=50,y=340)
                D=Entry(c3,width=50)
                D.place(x=200,y=345)
                e=Label(c3,text='EMAIL',font=('arial',15),bg='lavender')
                e.place(x=50,y=410)
                E=Entry(c3,width=50)
                E.place(x=200,y=415)
                h=Label(c3,text='REGNO',font=('arial',15),bg='lavender')
                h.place(x=50,y=480)
                H=Entry(c3,width=50)
                H.place(x=200,y=485)
                b1=Button(c3,text='SAVE',command=savedata,bg='green',font=('arial',15))
                b1.place(x=430,y=550)
                bt=Button(c3,text='Close',command=closebt,bg='red',font=('arial',15))
                bt.place(x=550,y=550)
            z=Label(c2,text='  COMPANY ',bg='purple',fg='white',font=('arial',21))
            z.place(x=3,y=3)
            b1=Button(c2,text='Insert',bg='white',fg='purple',font=('arial',14),command=cosavedatabt)
            b1.place(x=10,y=60)
            scr()

            def cofindbt():
                lt=[]
                c3=Canvas(SC,height=1160,width=800,bg='lavender')
                c3.place(x=360,y=0)
                def filldata():
                    
                    db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                    cur=db.cursor()
                    sql="select id from company"
                    cur.execute(sql)
                    data=cur.fetchall()
                    for res in data:
                        lt.append(res[0])
                    db.close()   
                def finddata():
                    db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                    cur=db.cursor()
                    xa=d.get()
                    sql="select cname,address,phone,email,regno from company where id='%s'"%(xa)
                    cur.execute(sql)
                    data=cur.fetchone()
                    f.delete(0,100)
                    h.delete(0,100)
                    k.delete(0,100)
                    u.delete(0,100)
                    r.delete(0,100)
                    f.insert(0,data[0])
                    h.insert(0,data[1])
                    k.insert(0,data[2])
                    r.insert(0,data[3])
                    u.insert(0,data[4])
                    db.close()
                def closebt():
                    c3.destroy()
                    scr()
                a=Label(c3,text='COMPANY ID',font=('arial',15),bg='lavender')
                a.place(x=50,y=70)
                d=Entry(c3,width=40)
                d=ttk.Combobox(c3,width=40)
                filldata()
                d['values']=lt
                d.place(x=500,y=70)
                bt=Button(c3,text='FIND',command=finddata,bg='blue',font=('arial',15))
                bt.place(x=400,y=110)
                e=Label(c3,text='COMPANY NAME',font=('arial',15),bg='lavender')
                e.place(x=50,y=150)
                f=Entry(c3,width=40)
                f.place(x=500,y=150)
                g=Label(c3,text='ADDRESS',font=('arial',15),bg='lavender')
                g.place(x=50,y=190)
                h=Entry(c3,width=40)
                h.place(x=500,y=190)
                j=Label(c3,text='PHONE NUMBER',font=('arial',15),bg='lavender')
                j.place(x=50,y=230)
                k=Entry(c3,width=40)
                k.place(x=500,y=230)
                p=Label(c3,text='EMAIL',font=('arial',15),bg='lavender')
                p.place(x=50,y=270)
                u=Entry(c3,width=40)
                u.place(x=500,y=270)
                v=Label(c3,text='REGISTRATION NUMBER',font=('arial',15),bg='lavender')
                v.place(x=50,y=310)
                r=Entry(c3,width=40)
                r.place(x=500,y=310)
                bt=Button(c3,text='CLOSE',command=closebt,bg='red',font=('arial',15))
                bt.place(x=400,y=450)
                
                
                def codata():
                    B1=[]
                    B2=[]
                    B3=[]
                    B4=[]
                    B5=[]
                    B6=[]
                    i=0
                    c3=Canvas(SC,height=1160,width=800,bg='lavender')
                    c3.place(x=360,y=0)
                    def filldata():
                        db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                        cur=db.cursor()
                        sql="select * from company"
                        cur.execute(sql)
                        data=cur.fetchall()
                        for res in data:
                            B1.append(res[0])
                            B2.append(res[1])
                            B3.append(res[2])
                            B4.append(res[3])
                            B5.append(res[4])
                            B6.append(res[5])
                        db.close()
                    def firstdata():
                        global i
                        i=0
                        A1.config(text='')
                        A2.config(text='')
                        A3.config(text='')
                        A4.config(text='')
                        A5.config(text='')
                        A6.config(text='')
                        
                        A1.config(text=B1[i])
                        A2.config(text=B2[i])
                        A3.config(text=B3[i])
                        A4.config(text=B4[i])
                        A5.config(text=B5[i])
                        A6.config(text=B6[i])
                    def nextdata():
                        global i
                        if i<len(B1)-1:
                            i=i+1
                            A1.config(text='')
                            A2.config(text='')
                            A3.config(text='')
                            A4.config(text='')
                            A5.config(text='')
                            A6.config(text='')
                            
                            A1.config(text=B1[i])
                            A2.config(text=B2[i])
                            A3.config(text=B3[i])
                            A4.config(text=B4[i])
                            A5.config(text=B5[i])
                            A6.config(text=B6[i])
                
                        else:
                            messagebox.showinfo('Screen',"last record")
                    def lastdata():
                        global i
                        i=len(B1)-1
                        A1.config(text='')
                        A2.config(text='')
                        A3.config(text='')
                        A4.config(text='')
                        A5.config(text='')
                        A6.config(text='')
                        
                        A1.config(text=B1[i])
                        A2.config(text=B2[i])
                        A3.config(text=B3[i])
                        A4.config(text=B4[i])
                        A5.config(text=B5[i])
                        A6.config(text=B6[i])
                    def prevdata():
                        global i
                        if i>0:
                            i=i-1
                            A1.config(text='')
                            A2.config(text='')
                            A3.config(text='')
                            A4.config(text='')
                            A5.config(text='')
                            A6.config(text='')
                            
                            A1.config(text=B1[i])
                            A2.config(text=B2[i])
                            A3.config(text=B3[i])
                            A4.config(text=B4[i])
                            A5.config(text=B5[i])
                            A6.config(text=B6[i])
                        else:
                            messagebox.showinfo('Screen',"Already done")
                    def exitdata():
                        c3.destroy()
                        scr()
                    
                    A=Label(c3,text='COMPANY ID',font=('arial',15),bg='lavender')
                    A.place(x=50,y=40)
                    A1=Label(c3,width=35)
                    A1.place(x=500,y=40)
                    B=Label(c3,text='COMPANY NAME',font=('arial',15),bg='lavender')
                    B.place(x=50,y=110)
                    A2=Label(c3,width=35)
                    A2.place(x=500,y=110)
                    C=Label(c3,text='ADDRESS',font=('arial',15),bg='lavender')
                    C.place(x=50,y=170)
                    A3=Label(c3,width=35)
                    A3.place(x=500,y=170)
                    D=Label(c3,text='PHONE',font=('arial',15),bg='lavender')
                    D.place(x=50,y=230)
                    A4=Label(c3,width=35)
                    A4.place(x=500,y=230)
                    E=Label(c3,text='EMAIL',font=('arial',15),bg='lavender')
                    E.place(x=50,y=290)
                    A5=Label(c3,width=35)
                    A5.place(x=500,y=290)
                    F=Label(c3,text='REGISTRATION NUMBER',font=('arial',15),bg='lavender')
                    F.place(x=50,y=350)
                    A6=Label(c3,width=35)
                    A6.place(x=500,y=350)
                    BT1=Button(c3,text='FIRST',command=firstdata,bg='orange',font=('arial',15))
                    BT1.place(x=50,y=455)
                    BT2=Button(c3,text='NEXT',command=nextdata,bg='pink',font=('arial',15))
                    BT2.place(x=200,y=455)
                    BT3=Button(c3,text='LAST',command=lastdata,bg='green',font=('arial',15))
                    BT3.place(x=350,y=455)
                    BT4=Button(c3,text='PREVIOUS',command=prevdata,bg='blue',font=('arial',15))
                    BT4.place(x=500,y=455)
                    BT5=Button(c3,text='CLOSE',command=exitdata,bg='red',font=('arial',15))
                    BT5.place(x=650,y=455)
                    filldata()
                
                b5=Button(c3,text='Records',bg='white',fg='purple',font=('arial',14),command=codata)
                b5.place(x=650,y=450)
                

            b2=Button(c2,text='Find',bg='white',fg='purple',font=('arial',14),command=cofindbt)
            b2.place(x=10,y=110)
            scr()
            
            def coupdatebt():
                lt=[]
                c3=Canvas(SC,height=1160,width=800,bg='lavender')
                c3.place(x=360,y=0)
                def filldata():
                    db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                    cur=db.cursor()
                    sql="select id from company"
                    cur.execute(sql)
                    data=cur.fetchall()
                    for res in data:
                        lt.append(res[0])
                    db.close()   
                def finddata():
                    db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                    cur=db.cursor()
                    xa=d.get()
                    sql="select cname,address,phone,email,regno from company where id='%s'"%(xa)
                    cur.execute(sql)
                    data=cur.fetchone()
                    f.delete(0,100)
                    h.delete(0,100)
                    k.delete(0,100)
                    u.delete(0,100)
                    r.delete(0,100)
                    f.insert(0,data[0])
                    h.insert(0,data[1])
                    k.insert(0,data[2])
                    r.insert(0,data[3])
                    u.insert(0,data[4])
                    db.close()
                    
                def updatedata():
                    if len(d.get())==0 or len(f.get())==0 or len(h.get())==0 or len(k.get())==0 or len(u.get())==0 or len(r.get())==0 :
                        messagebox.showerror('ERROR','ENTER VAILD DATA')
                    else:
                        db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                        cur=db.cursor()
                        xa=d.get()
                        xb=f.get()
                        xc=h.get()
                        xd=k.get()
                        xe=u.get()
                        xh=r.get()
                        sql="update company set cname='%s',address='%s',phone='%s',email='%s',regno='%s' where id='%s'"%(xb,xc,xd,xe,xh,xa)
                        cur.execute(sql)
                        db.commit()
                        messagebox.showinfo('Screen','Updated')
                        db.close()
                        d.delete(0,100)
                        f.delete(0,100)
                        h.delete(0,100)
                        k.delete(0,100)
                        u.delete(0,100)
                        r.delete(0,100)
                        c3.destroy()
                        scr()
                def closebt():
                    c3.destroy()
                    scr()
                
                a=Label(c3,text='COMPANY ID',font=('arial',15),bg='lavender')
                a.place(x=50,y=70)
                d=Entry(c3,width=40)
                d=ttk.Combobox(c3,width=40)
                filldata()
                d['values']=lt
                d.place(x=500,y=70)
                bt=Button(c3,text='FIND',command=finddata,bg='blue',font=('arial',15))
                bt.place(x=400,y=110)
                e=Label(c3,text='COMPANY NAME',font=('arial',15),bg='lavender')
                e.place(x=50,y=150)
                f=Entry(c3,width=40)
                f.place(x=500,y=150)
                g=Label(c3,text='ADDRESS',font=('arial',15),bg='lavender')
                g.place(x=50,y=190)
                h=Entry(c3,width=40)
                h.place(x=500,y=190)
                j=Label(c3,text='PHONE NUMBER',font=('arial',15),bg='lavender')
                j.place(x=50,y=230)
                k=Entry(c3,width=40)
                k.place(x=500,y=230)
                p=Label(c3,text='EMAIL',font=('arial',15),bg='lavender')
                p.place(x=50,y=270)
                u=Entry(c3,width=40)
                u.place(x=500,y=270)
                v=Label(c3,text='REGISTRATION NUMBER',font=('arial',15),bg='lavender')
                v.place(x=50,y=310)
                r=Entry(c3,width=40)
                r.place(x=500,y=310)
                btt=Button(c3,text='UPDATE',command=updatedata,bg='green',font=('arial',15))
                btt.place(x=300,y=450)
                bt=Button(c3,text='CLOSE',command=closebt,bg='red',font=('arial',15))
                bt.place(x=400,y=450)
            b3=Button(c2,text='Update',bg='white',fg='purple',font=('arial',14),command=coupdatebt)
            b3.place(x=10,y=160)
            scr()
            
            def codeletebt():
                lt=[]
                c3=Canvas(SC,height=1160,width=800,bg='lavender')
                c3.place(x=360,y=0)
                def filldata():
                    db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                    cur=db.cursor()
                    sql="select id from company"
                    cur.execute(sql)
                    data=cur.fetchall()
                    for res in data:
                        lt.append(res[0])
                    db.close()
                def deletedata():
                    db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                    cur=db.cursor()
                    xa=d.get()
                    sql="delete from company where id='%s'"%(xa)
                    cur.execute(sql)
                    db.commit()
                    messagebox.showinfo('Screen','Data Deleted')
                    d.delete(0,100)
                    c3.destroy()
                    scr()
                def closebt():
                    c3.destroy()
                    scr()
                
                a=Label(c3,text=' COMPANY ID',font=('arial',15),bg='lavender')
                a.place(x=200,y=70)
                d=Entry(c3,width=10)
                d=ttk.Combobox(c3,width=40)
                filldata()
                d['values']=lt
                d.place(x=500,y=70)
                bt=Button(c3,text='DELETE',command=deletedata,bg='blue',font=('arial',15))
                bt.place(x=400,y=110)
                bt=Button(c3,text='CLOSE',command=closebt,bg='red',font=('arial',15))
                bt.place(x=400,y=160)
            b4=Button(c2,text='Delete',bg='white',fg='purple',font=('arial',14),command=codeletebt)
            b4.place(x=10,y=210)
            scr()
            
        def cat():
            c2=Canvas(SC,height=1160,width=180,bg='violet')
            c2.place(x=180,y=0)
            z=Label(c2,text='CATEGORY ',bg='purple',fg='white',font=('arial',21))
            z.place(x=3,y=3)
            def catsavebt():
                c3=Canvas(SC,height=1160,width=800,bg='lavender')
                c3.place(x=360,y=0)
                def savedata():
                    if len(A.get())==0 or len(B.get())==0 or len(C.get())==0 :
                        messagebox.showerror('ERROR','ENTER VAILD DATA')
                    else:
                        db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                        cur=db.cursor()
                        xa=A.get()
                        xb=B.get()
                        xc=C.get()
                        sql="insert into category values('%s','%s','%s')"%(xa,xb,xc)
                        cur.execute(sql)
                        db.commit()
                        messagebox.showinfo('Screen','SAVED')
                        db.close()
                        A.delete(0,100)
                        B.delete(0,100)
                        C.delete(0,100)
                        c3.destroy()
                        scr()
                def closebt():
                    c3.destroy()  
                    scr()
                
                a=Label(c3,text='CATEGORY ID',font=('arial',15),bg='lavender')
                a.place(x=50,y=50)
                A=Entry(c3,width=50)
                A.place(x=400,y=50)
                b=Label(c3,text='NAME',font=('arial',15),bg='lavender')
                b.place(x=50,y=120)
                B=Entry(c3,width=50)
                B.place(x=400,y=120)
                c=Label(c3,text='DESCRIPTION',font=('arial',15),bg='lavender')
                c.place(x=50,y=190)
                C=Entry(c3,width=50)
                C.place(x=400,y=190)
                b1=Button(c3,text='SAVE',command=savedata,bg='green',font=('arial',15))
                b1.place(x=200,y=250)
                bt=Button(c3,text='CLOSE',command=closebt,bg='red',font=('arial',15))
                bt.place(x=400,y=250)
            
            b6=Button(c2,text='Insert',bg='white',fg='purple',font=('arial',14),command=catsavebt)
            b6.place(x=10,y=60)
            scr()
            
            def catfindbt():
                lt=[]
                c3=Canvas(SC,height=1160,width=800,bg='lavender')
                c3.place(x=360,y=0)
                def filldata():
                    db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                    cur=db.cursor()
                    sql="select catid from category"
                    cur.execute(sql)
                    data=cur.fetchall()
                    for res in data:
                        lt.append(res[0])
                    db.close()   
                def finddata():
                    db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                    cur=db.cursor()
                    xa=d.get()
                    sql="select catname,description from category where catid='%s'"%(xa)
                    cur.execute(sql)
                    data=cur.fetchone()
                    f.delete(0,100)
                    h.delete(0,100)
                    f.insert(0,data[0])
                    h.insert(0,data[1])
                    db.close()
                def closebt():
                    c3.destroy()
                    scr()
                
                a=Label(c3,text='CATEGORY ID',font=('arial',15),bg='lavender')
                a.place(x=50,y=70)
                d=Entry(c3,width=40)
                d=ttk.Combobox(c3,width=40)
                filldata()
                d['values']=lt
                d.place(x=500,y=70)
                bt=Button(c3,text='FIND',command=finddata,bg='blue',font=('arial',15))
                bt.place(x=400,y=110)
                e=Label(c3,text='CATEGORY NAME',font=('arial',15),bg='lavender')
                e.place(x=50,y=150)
                f=Entry(c3,width=40)
                f.place(x=500,y=150)
                g=Label(c3,text='DESCRIPTION',font=('arial',15),bg='lavender')
                g.place(x=50,y=190)
                h=Entry(c3,width=40)
                h.place(x=500,y=190)
                bt=Button(c3,text='CLOSE',command=closebt,bg='red',font=('arial',15))
                bt.place(x=400,y=250)
                
                def catdata():
                    B1=[]
                    B2=[]
                    B3=[]
                    
                    i=0
                    
                    c3=Canvas(SC,height=1160,width=800,bg='lavender')
                    c3.place(x=360,y=0)
                    def filldata():
                        db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                        cur=db.cursor()
                        sql="select * from category"
                        cur.execute(sql)
                        data=cur.fetchall()
                        for res in data:
                            B1.append(res[0])
                            B2.append(res[1])
                            B3.append(res[2])
                        db.close()
                    def firstdata():
                        global i
                        i=0
                        A1.config(text='')
                        A2.config(text='')
                        A3.config(text='')
                        
                        A1.config(text=B1[i])
                        A2.config(text=B2[i])
                        A3.config(text=B3[i])
                        
                    def nextdata():
                        global i
                        if i<len(B1)-1:
                            i=i+1
                            A1.config(text='')
                            A2.config(text='')
                            A3.config(text='')
                            
                            A1.config(text=B1[i])
                            A2.config(text=B2[i])
                            A3.config(text=B3[i])
                            
                
                        else:
                            messagebox.showinfo('Screen',"last record")
                    def lastdata():
                        global i
                        i=len(B1)-1
                        A1.config(text='')
                        A2.config(text='')
                        A3.config(text='')
                        
                        A1.config(text=B1[i])
                        A2.config(text=B2[i])
                        A3.config(text=B3[i])
                        
                    def prevdata():
                        global i
                        if i>0:
                            i=i-1
                            A1.config(text='')
                            A2.config(text='')
                            A3.config(text='')
                            
                            A1.config(text=B1[i])
                            A2.config(text=B2[i])
                            A3.config(text=B3[i])
                            
                        else:
                            messagebox.showinfo('Screen',"Already done")
                    def exitdata():
                        c3.destroy()
                        scr()
                    
                    A=Label(c3,text='CATEGORY ID',font=('arial',15),bg='lavender')
                    A.place(x=50,y=40)
                    A1=Label(c3,width=35)
                    A1.place(x=500,y=40)
                    B=Label(c3,text='CATEGORY NAME',font=('arial',15),bg='lavender')
                    B.place(x=50,y=110)
                    A2=Label(c3,width=35)
                    A2.place(x=500,y=110)
                    C=Label(c3,text='DESCRIPTION',font=('arial',15),bg='lavender')
                    C.place(x=50,y=170)
                    A3=Label(c3,width=35)
                    A3.place(x=500,y=170)
                    BT1=Button(c3,text='FIRST',command=firstdata,bg='orange',font=('arial',15))
                    BT1.place(x=50,y=455)
                    BT2=Button(c3,text='NEXT',command=nextdata,bg='pink',font=('arial',15))
                    BT2.place(x=200,y=455)
                    BT3=Button(c3,text='LAST',command=lastdata,bg='green',font=('arial',15))
                    BT3.place(x=350,y=455)
                    BT4=Button(c3,text='PREVIOUS',command=prevdata,bg='blue',font=('arial',15))
                    BT4.place(x=500,y=455)
                    BT5=Button(c3,text='CLOSE',command=exitdata,bg='red',font=('arial',15))
                    BT5.place(x=650,y=455)
                    filldata()
                
                b10=Button(c3,text='Records',bg='white',fg='purple',font=('arial',15),command=catdata)
                b10.place(x=600,y=250)
                
            
            b7=Button(c2,text='Find',bg='white',fg='purple',font=('arial',14),command=catfindbt)
            b7.place(x=10,y=110)
            scr()
            
            def catupdatebt():
                lt=[]
                c3=Canvas(SC,height=1160,width=800,bg='lavender')
                c3.place(x=360,y=0)
                def filldata():
                    db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                    cur=db.cursor()
                    sql="select catid from category"
                    cur.execute(sql)
                    data=cur.fetchall()
                    for res in data:
                        lt.append(res[0])
                    db.close()   
                def finddata():
                    db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                    cur=db.cursor()
                    xa=d.get()
                    sql="select catname,description from category where catid='%s'"%(xa)
                    cur.execute(sql)
                    data=cur.fetchone()
                    f.delete(0,100)
                    h.delete(0,100)
                    f.insert(0,data[0])
                    h.insert(0,data[1])
                    db.close()
                def updatedata():
                    if len(d.get())==0 or len(f.get())==0 or len(h.get())==0 :
                        messagebox.showerror('ERROR','ENTER VAILD DATA')
                    else:
                        db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                        cur=db.cursor()
                        xa=d.get()
                        xb=f.get()
                        xc=h.get()
                        sql="update category set catname='%s',description='%s' where catid='%s'"%(xb,xc,xa)
                        cur.execute(sql)
                        db.commit()
                        messagebox.showinfo('Screen','Updated')
                        db.close()
                        d.delete(0,100)
                        f.delete(0,100)
                        h.delete(0,100) 
                        c3.destroy()
                        scr()
                def closebt():
                    c3.destroy()
                    scr()
                
                a=Label(c3,text='CATEGORY ID',font=('arial',15),bg='lavender')
                a.place(x=50,y=70)
                d=Entry(c3,width=40)
                d=ttk.Combobox(c3,width=40)
                filldata()
                d['values']=lt
                d.place(x=500,y=70)
                bt=Button(c3,text='FIND',command=finddata,bg='blue',font=('arial',15))
                bt.place(x=400,y=110)
                e=Label(c3,text='CATEGORY NAME',font=('arial',15),bg='lavender')
                e.place(x=50,y=150)
                f=Entry(c3,width=40)
                f.place(x=500,y=150)
                g=Label(c3,text='DESCRIPTION',font=('arial',15),bg='lavender')
                g.place(x=50,y=190)
                h=Entry(c3,width=40)
                h.place(x=500,y=190)
                btt=Button(c3,text='UPDATE',command=updatedata,bg='green',font=('arial',15))
                btt.place(x=300,y=250)
                bt=Button(c3,text='CLOSE',command=closebt,bg='red',font=('arial',15))
                bt.place(x=400,y=250)
            
            b8=Button(c2,text='Update',bg='white',fg='purple',font=('arial',14),command=catupdatebt)
            b8.place(x=10,y=160)
            scr()
            
            def catdeletebt():
                lt=[]
                c3=Canvas(SC,height=1160,width=800,bg='lavender')
                c3.place(x=360,y=0)
                def filldata():
                    db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                    cur=db.cursor()
                    sql="select catid from category"
                    cur.execute(sql)
                    data=cur.fetchall()
                    for res in data:
                        lt.append(res[0])
                    db.close() 
                def deletedata():
                    db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                    cur=db.cursor()
                    xa=d.get()
                    sql="delete from category where catid='%s'"%(xa)
                    cur.execute(sql)
                    db.commit()
                    messagebox.showinfo('Screen','Data Deleted')
                    d.delete(0,100)
                    c3.destroy()
                    scr()
                def closebt():
                    c3.destroy()
                    scr()
                
                a=Label(c3,text='CATEGORY ID',font=('arial',15),bg='lavender')
                a.place(x=50,y=70)
                d=Entry(c3,width=40)
                d=ttk.Combobox(c3,width=40)
                filldata()
                d['values']=lt
                d.place(x=500,y=70)
                bt=Button(c3,text='DELETE',command=deletedata,bg='blue',font=('arial',15))
                bt.place(x=400,y=110)
                bt=Button(c3,text='CLOSE',command=closebt,bg='red',font=('arial',15))
                bt.place(x=400,y=250)
            
            b9=Button(c2,text='Delete',bg='white',fg='purple',font=('arial',15),command=catdeletebt)
            b9.place(x=10,y=210)
            scr()
            
        def pro():
            c2=Canvas(SC,height=1160,width=180,bg='violet')
            c2.place(x=180,y=0)
            z=Label(c2,text=' PRODUCT  ',bg='purple',fg='white',font=('arial',21))
            z.place(x=3,y=3)
            def prosavebt():
                c3=Canvas(SC,height=1160,width=800,bg='lavender')
                c3.place(x=360,y=0)
                def savedata():
                    if len(a.get())==0 or len(b.get())==0 or len(c.get())==0 or len(d.get())==0 or len(e.get())==0 or len(f.get())==0 :
                        messagebox.showerror('ERROR','ENTER VAILD DATA')
                    else:
                        db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                        cur=db.cursor()
                        xid=a.get()
                        xcatid=b.get()
                        xpname=c.get()
                        xpr=d.get()
                        xun=int(e.get())
                        xqty=int(f.get())
                        sql="insert into products values('%s','%s','%s','%s',%d,%d)"%(xid,xcatid,xpname,xpr,xun,xqty)
                        cur.execute(sql)
                        db.commit()
                        messagebox.showinfo('Hi','saved')
                        db.close()
                        a.delete(0,100)
                        b.delete(0,100)
                        c.delete(0,100)
                        d.delete(0,100)
                        e.delete(0,100)
                        f.delete(0,100)
                        c3.destroy()
                        scr()
                def closed():
                    c3.destroy()
                    scr()
                
                idi=Label(c3,text='Product id',font=('arial',15),bg='lavender')
                idi.place(x=50,y=70)
                a=Entry(c3,width=40)
                a.place(x=400,y=70)
                catid=Label(c3,text='Category id',font=('arial',15),bg='lavender')
                catid.place(x=50,y=110)
                b=Entry(c3,width=40)
                b.place(x=400,y=110)
                pname=Label(c3,text='Product Name',font=('arial',15),bg='lavender')
                pname.place(x=50,y=150)
                c=Entry(c3,width=40)
                c.place(x=400,y=150)
                pr=Label(c3,text='Price',font=('arial',15),bg='lavender')
                pr.place(x=50,y=190)
                d=Entry(c3,width=40)
                d.place(x=400,y=190)
                un=Label(c3,text='Unit',font=('arial',15),bg='lavender')
                un.place(x=50,y=230)
                e=Entry(c3,width=40)
                e.place(x=400,y=230)
                qty=Label(c3,text='Quantity',font=('arial',15),bg='lavender')
                qty.place(x=50,y=270)
                f=Entry(c3,width=40)
                f.place(x=400,y=270)
                bt=Button(c3,text='Save',command=savedata,bg='green',font=('arial',15))
                bt.place(x=50,y=310)
                cl=Button(c3,text='Close',command=closed,bg='red',font=('arial',15))
                cl.place(x=400,y=310)
                
            b11=Button(c2,text='Insert',bg='white',fg='purple',font=('arial',14),command=prosavebt)
            b11.place(x=10,y=60)
            scr()
            
            def profindbt():
                c3=Canvas(SC,height=1160,width=800,bg='lavender')
                c3.place(x=360,y=0)
                def closed():
                    c3.destroy()
                    scr()
                lt=[]
                def filldata():
                    db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                    cur=db.cursor()
                    sql="select prodid from products"
                    cur.execute(sql)
                    data=cur.fetchall()
                    for res in data:
                        lt.append(res[0])
                    db.close()
                def finddata():
                    db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                    cur=db.cursor()
                    xid=a.get()
                    sql="select catid,pname,price,unit,qty from products where prodid=('%s')"%(xid)
                    cur.execute(sql) 
                    data=cur.fetchone()
                    b.delete(0,100)
                    c.delete(0,100)
                    d.delete(0,100)
                    e.delete(0,100)
                    f.delete(0,100)
                    b.insert(0,data[0])
                    c.insert(0,data[1])
                    d.insert(0,data[2])
                    e.insert(0,str(data[3]))
                    f.insert(0,str(data[4]))
                    db.close()
                
                idi=Label(c3,text='Product id',font=('arial',15),bg='lavender')
                idi.place(x=50,y=30)
                a=ttk.Combobox(c3,width=20)
                filldata()
                a['values']=lt
                a.place(x=400,y=30)
                bt=Button(c3,text='Find',command=finddata,bg='blue',font=('arial',15))
                bt.place(x=100,y=70)
                catid=Label(c3,text='Category id',font=('arial',15),bg='lavender')
                catid.place(x=50,y=110)
                b=Entry(c3,width=40)
                b.place(x=400,y=110)
                pname=Label(c3,text='Product Name',font=('arial',15),bg='lavender')
                pname.place(x=50,y=150)
                c=Entry(c3,width=40)
                c.place(x=400,y=150)
                pr=Label(c3,text='Price',font=('arial',15),bg='lavender')
                pr.place(x=50,y=190)
                d=Entry(c3,width=40)
                d.place(x=400,y=190)
                un=Label(c3,text='Unit',font=('arial',15),bg='lavender')
                un.place(x=50,y=230)
                e=Entry(c3,width=40)
                e.place(x=400,y=230)
                qty=Label(c3,text='Quantity',font=('arial',15),bg='lavender')
                qty.place(x=50,y=270)
                f=Entry(c3,width=40)
                f.place(x=400,y=270)
                bt=Button(c3,text='Close',command=closed,bg='red',font=('arial',15))
                bt.place(x=100,y=310)
                
                
                def prodata() :
                    B1=[]
                    B2=[]
                    B3=[]
                    B4=[]
                    B5=[]
                    B6=[]
                    i=0
                    c3=Canvas(SC,height=1160,width=800,bg='lavender')
                    c3.place(x=360,y=0)
                    def filldata():
                        db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                        cur=db.cursor()
                        sql="select * from products"
                        cur.execute(sql)
                        data=cur.fetchall()
                        for res in data:
                            B1.append(res[0])
                            B2.append(res[1])
                            B3.append(res[2])
                            B4.append(res[3])
                            B5.append(res[4])
                            B6.append(res[5])
                        db.close()
                    def firstdata():
                        global i
                        i=0
                        A1.config(text='')
                        A2.config(text='')
                        A3.config(text='')
                        A4.config(text='')
                        A5.config(text='')
                        A6.config(text='')
                        A1.config(text=B1[i])
                        A2.config(text=B2[i])
                        A3.config(text=B3[i])
                        A4.config(text=B4[i])
                        A5.config(text=B5[i])
                        A6.config(text=B6[i])
                    def nextdata():
                        global i
                        if i<len(B1)-1:
                            i=i+1
                            A1.config(text='')
                            A2.config(text='')
                            A3.config(text='')
                            A4.config(text='')
                            A5.config(text='')
                            A6.config(text='')
                            A1.config(text=B1[i])
                            A2.config(text=B2[i])
                            A3.config(text=B3[i])
                            A4.config(text=B4[i])
                            A5.config(text=B5[i])
                            A6.config(text=B6[i])
                
                        else:
                            messagebox.showinfo('Screen',"last record")
                    def lastdata():
                        global i
                        i=len(B1)-1
                        A1.config(text='')
                        A2.config(text='')
                        A3.config(text='')
                        A4.config(text='')
                        A5.config(text='')
                        A6.config(text='')
                        A1.config(text=B1[i])
                        A2.config(text=B2[i])
                        A3.config(text=B3[i])
                        A4.config(text=B4[i])
                        A5.config(text=B5[i])
                        A6.config(text=B6[i])
                    def prevdata():
                        global i
                        if i>0:
                            i=i-1
                            A1.config(text='')
                            A2.config(text='')
                            A3.config(text='')
                            A4.config(text='')
                            A5.config(text='')
                            A6.config(text='')
                            A1.config(text=B1[i])
                            A2.config(text=B2[i])
                            A3.config(text=B3[i])
                            A4.config(text=B4[i])
                            A5.config(text=B5[i])
                            A6.config(text=B6[i])
                        else:
                            messagebox.showinfo('Screen',"Already done")
                    def exitdata():
                        c3.destroy()
                        scr()
                    
                    A=Label(c3,text='PRODUCT ID',font=('arial',15),bg='lavender')
                    A.place(x=50,y=40)
                    A1=Label(c3,width=35)
                    A1.place(x=390,y=40)
                    B=Label(c3,text='CATEGORY ID',font=('arial',15),bg='lavender')
                    B.place(x=50,y=110)
                    A2=Label(c3,width=35)
                    A2.place(x=390,y=110)
                    C=Label(c3,text='PRODUCT NAME',font=('arial',15),bg='lavender')
                    C.place(x=50,y=170)
                    A3=Label(c3,width=35)
                    A3.place(x=390,y=170)
                    D=Label(c3,text='PRICE',font=('arial',15),bg='lavender')
                    D.place(x=50,y=230)
                    A4=Label(c3,width=35)
                    A4.place(x=390,y=230)
                    E=Label(c3,text='UNIT',font=('arial',15),bg='lavender')
                    E.place(x=50,y=290)
                    A5=Label(c3,width=35)
                    A5.place(x=390,y=290)
                    F=Label(c3,text='QUANTITY',font=('arial',15),bg='lavender')
                    F.place(x=50,y=350)
                    A6=Label(c3,width=35)
                    A6.place(x=390,y=350)
                    BT1=Button(c3,text='FIRST RECORD',command=firstdata,bg='orange',font=('arial',15))
                    BT1.place(x=50,y=455)
                    BT2=Button(c3,text='NEXT RECORD',command=nextdata,bg='pink',font=('arial',15))
                    BT2.place(x=200,y=455)
                    BT3=Button(c3,text='LAST RECORD',command=lastdata,bg='green',font=('arial',15))
                    BT3.place(x=350,y=455)
                    BT4=Button(c3,text='PREVIOUS',command=prevdata,bg='blue',font=('arial',15))
                    BT4.place(x=500,y=455)
                    BT5=Button(c3,text='CLOSE',command=exitdata,bg='red',font=('arial',15))
                    BT5.place(x=650,y=455)
                    filldata()
                    
                b15=Button(c3,text='Records',bg='white',fg='purple',font=('arial',15),command=prodata)
                b15.place(x=600,y=310)

                
                
            b12=Button(c2,text='Find',bg='white',fg='purple',font=('arial',14),command=profindbt)
            b12.place(x=10,y=110)
            scr()
              
            def prodelete():
                lt=[]
                c3=Canvas(SC,height=1160,width=800,bg='lavender')
                c3.place(x=360,y=0)
                def filldata():
                    db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                    cur=db.cursor()
                    sql="select prodid from products"
                    cur.execute(sql)
                    data=cur.fetchall()
                    for res in data:
                        lt.append(res[0])
                    db.close()
                def deletedata():
                    db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                    cur=db.cursor()
                    xa=d.get()
                    sql="delete from products where prodid=('%s')"%(xa)
                    cur.execute(sql)
                    db.commit()
                    messagebox.showinfo('Hi','Data Delete')
                    d.delete(0,100)
                    c3.destroy()
                    scr()
                def closed():
                    c3.destroy()
                    scr()
                
                a=Label(c3,text='Product id',font=('arial',15),bg='lavender')
                a.place(x=50,y=70)
                d=ttk.Combobox(c3,width=20)
                filldata()
                d['values']=lt
                d.place(x=500,y=70)
                bt=Button(c3,text='Delete',command=deletedata,bg='blue',font=('arial',15))
                bt.place(x=300,y=150)
                bt=Button(c3,text='Close',command=closed,bg='red',font=('arial',15))
                bt.place(x=300,y=200)
                
            b14=Button(c2,text='Delete',bg='white',fg='purple',font=('arial',14),command=prodelete)
            b14.place(x=10,y=210)
            scr()

            def proupdatebt():
                lt=[]
                c3=Canvas(SC,height=1160,width=800,bg='lavender')
                c3.place(x=360,y=0)
                def filldata():
                    db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                    cur=db.cursor()
                    sql="select prodid from products"
                    cur.execute(sql)
                    data=cur.fetchall()
                    for res in data:
                        lt.append(res[0])
                    db.close()
                def finddata():
                    db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                    cur=db.cursor()
                    xid=a.get()
                    sql="select catid,pname,price,unit,qty from products where prodid=('%s')"%(xid)
                    cur.execute(sql) 
                    data=cur.fetchone()
                    b.delete(0,100)
                    c.delete(0,100)
                    d.delete(0,100)
                    e.delete(0,100)
                    f.delete(0,100)
                    b.insert(0,data[0])
                    c.insert(0,data[1])
                    d.insert(0,data[2])
                    e.insert(0,str(data[3]))
                    f.insert(0,str(data[4]))
                    db.close()
                def dataupdate():
                    if len(a.get())==0 or len(b.get())==0 or len(c.get())==0 or len(d.get())==0 or len(e.get())==0 or len(f.get())==0 :
                        messagebox.showerror('ERROR','ENTER VAILD DATA')
                    else:
                         db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                         cur=db.cursor()
                         xid=a.get()
                         xcatid=b.get()
                         xpname=c.get()
                         xprice=d.get()
                         xun=int(e.get())
                         xqty=int(f.get())
                         sql="update products set catid='%s',pname='%s',price='%s',unit=%d,qty=%d where prodid=('%s')"%(xcatid,xpname,xprice,xun,xqty,xid)
                         cur.execute(sql)
                         db.commit()
                         messagebox.showinfo('Hi','Update Done')
                         db.close()
                         a.delete(0,100)
                         b.delete(0,100)
                         c.delete(0,100)
                         d.delete(0,100)
                         e.delete(0,100)
                         f.delete(0,100)
                         c3.destroy()
                         scr()
                def closed():
                    c3.destroy()
                    scr()
                
                idi=Label(c3,text='Product id',font=('arial',15),bg='lavender')
                idi.place(x=50,y=30)
                a=ttk.Combobox(c3,width=20)
                filldata()
                a['values']=lt
                a.place(x=400,y=30)
                bt=Button(c3,text='Find',command=finddata,bg='blue',font=('arial',15))
                bt.place(x=100,y=70)
                catid=Label(c3,text='Category id',font=('arial',15),bg='lavender')
                catid.place(x=50,y=110)
                b=Entry(c3,width=40)
                b.place(x=400,y=110)
                pname=Label(c3,text='Product Name',font=('arial',15),bg='lavender')
                pname.place(x=50,y=150)
                c=Entry(c3,width=40)
                c.place(x=400,y=150)
                pr=Label(c3,text='Price',font=('arial',15),bg='lavender')
                pr.place(x=50,y=190)
                d=Entry(c3,width=40)
                d.place(x=400,y=190)
                un=Label(c3,text='Unit',font=('arial',15),bg='lavender')
                un.place(x=50,y=230)
                e=Entry(c3,width=40)
                e.place(x=400,y=230)
                qty=Label(c3,text='Quantity',font=('arial',15),bg='lavender')
                qty.place(x=50,y=270)
                f=Entry(c3,width=40)
                f.place(x=400,y=270)
                btt=Button(c3,text='Update',command=dataupdate,bg='green',font=('arial',15))
                btt.place(x=300,y=310)
                bt=Button(c3,text='Close',command=closed,bg='red',font=('arial',15))
                bt.place(x=100,y=310)
            
            b13=Button(c2,text='Update',bg='white',fg='purple',font=('arial',14),command=proupdatebt)
            b13.place(x=10,y=160)
            scr()
            
            def proccographdatabt():
                
                def procharts():
                    deleteimg()
                    if int(ww.get())==0:
                        
                        def prolinegraphdata():
                            
                            deleteimg()
                            db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                            cur=db.cursor()
                            a=[]
                            b=[]
                            sql="select prodid, price  from products"
                            cur.execute(sql)
                            dt=cur.fetchall()
                            for i in dt:
                                a.append(i[0])
                                b.append(int(i[1]))
                                
                            plt.scatter(b,a)
                            plt.savefig('console_image.png')
                            plt.show()
                           
                            image = Image.open('console_image.png')
                            image.paste(image)
                            image.show()
                            scr()
                            
                        deleteimg()
                        prolinegraphdata() 
                        
                        
                        
                    elif int(ww.get())==1:
                                        
                        def probargraphdata():
                            
                            db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                            cur=db.cursor()
                            c=[]
                            d=[]
                            sql="select prodid, price  from products"
                            cur.execute(sql)
                            df=cur.fetchall()
                            for i in df:
                                c.append(i[0])
                                d.append(int(i[1]))
                                
                            plt.bar(d,c)
                            plt.savefig('console_image1.png')
                            plt.show()
                            
                            image1 = Image.open('console_image1.png')
                            image1.paste(image1)
                            image1.show()
                            scr()
            
                        deleteimg()
                        probargraphdata()
                        
                    elif int(ww.get())==2:
                                        
                        def prodbargraaphdata():
                            
                            db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                            cur=db.cursor()
                            c=[]
                            d=[]
                            sql="select prodid , unit from products"
                            cur.execute(sql)
                            df=cur.fetchall()
                            for i in df:
                                c.append(i[0])
                                d.append(int(i[1]))
                                
                            plt.scatter(d,c)
                            plt.savefig('console_image1.png')
                            plt.show()
                            
                            image1 = Image.open('console_image1.png')
                            image1.paste(image1)
                            image1.show()
                            scr()
            
                        deleteimg()
                        prodbargraaphdata()
                    
                    
                    elif int(ww.get())==3:
                                        
                        def proodbargraphdata():
                            
                            db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                            cur=db.cursor()
                            c=[]
                            d=[]
                            sql="select prodid , unit  from products"
                            cur.execute(sql)
                            df=cur.fetchall()
                            for i in df:
                                c.append(i[0])
                                d.append(int(i[1]))
                                
                            plt.bar(d,c)
                            plt.savefig('console_image1.png')
                            plt.show()
                            
                            image1 = Image.open('console_image1.png')
                            image1.paste(image1)
                            image1.show()
                            scr()
            
                        deleteimg()
                        proodbargraphdata()
                        
                    elif int(ww.get())==4:
                                        
                        def prorrdbargraphdata():
                            
                            db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                            cur=db.cursor()
                            c=[]
                            d=[]
                            sql="select prodid , qty  from products"
                            cur.execute(sql)
                            df=cur.fetchall()
                            for i in df:
                                c.append(i[0])
                                d.append(int(i[1]))
                                
                            plt.scatter(d,c)
                            plt.savefig('console_image1.png')
                            plt.show()
                            
                            image1 = Image.open('console_image1.png')
                            image1.paste(image1)
                            image1.show()
                            scr()
            
                        deleteimg()
                        prorrdbargraphdata()
                    
                    elif int(ww.get())==5:
                                        
                        def prroddbbargraphdata():
                            
                            db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                            cur=db.cursor()
                            c=[]
                            d=[]
                            sql="select prodid , qty  from products"
                            cur.execute(sql)
                            df=cur.fetchall()
                            for i in df:
                                c.append(i[0])
                                d.append(int(i[1]))
                                
                            plt.bar(d,c)
                            plt.savefig('console_image1.png')
                            plt.show()
                            
                            image1 = Image.open('console_image1.png')
                            image1.paste(image1)
                            image1.show()
                            scr()
            
                        deleteimg()
                        prroddbbargraphdata()
                        
                    elif int(ww.get())==6:
                                        
                        def pprroddbbargraphdata():
                            
                            db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                            cur=db.cursor()
                            c=[]
                            d=[]
                            sql="select price , unit  from products"
                            cur.execute(sql)
                            df=cur.fetchall()
                            for i in df:
                                c.append(int(i[0]))
                                d.append(int(i[1]))
                                
                            plt.scatter(d,c)
                            plt.savefig('console_image1.png')
                            plt.show()
                            
                            image1 = Image.open('console_image1.png')
                            image1.paste(image1)
                            image1.show()
                            scr()
            
                        deleteimg()
                        pprroddbbargraphdata()
                        
                    elif int(ww.get())==7:
                                        
                        def ppprroddbbargraphdata():
                            
                            db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                            cur=db.cursor()
                            c=[]
                            d=[]
                            sql="select price , unit  from products"
                            cur.execute(sql)
                            df=cur.fetchall()
                            for i in df:
                                c.append(int(i[0]))
                                d.append(int(i[1]))
                                
                            plt.bar(d,c)
                            plt.savefig('console_image1.png')
                            plt.show()
                            
                            image1 = Image.open('console_image1.png')
                            image1.paste(image1)
                            image1.show()
                            scr()
            
                        deleteimg()
                        ppprroddbbargraphdata()
                        
                    elif int(ww.get())==8:
                        
                        def prolllinegraphdata():
                            
                            deleteimg()
                            db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                            cur=db.cursor()
                            a=[]
                            b=[]
                            sql="select price, qty  from products"
                            cur.execute(sql)
                            dt=cur.fetchall()
                            for i in dt:
                                a.append(int(i[0]))
                                b.append(int(i[1]))
                                
                            plt.scatter(b,a)
                            plt.savefig('console_image.png')
                            plt.show()
                           
                            image = Image.open('console_image.png')
                            image.paste(image)
                            image.show()
                            scr()
                            
                        deleteimg()
                        prolllinegraphdata() 
                        
                    elif int(ww.get())==9:
                                        
                        def probbbargraphdata():
                            
                            db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                            cur=db.cursor()
                            c=[]
                            d=[]
                            sql="select price,qty  from products"
                            cur.execute(sql)
                            df=cur.fetchall()
                            for i in df:
                                c.append(int(i[0]))
                                d.append(int(i[1]))
                                
                            plt.bar(d,c)
                            plt.savefig('console_image1.png')
                            plt.show()
                            
                            image1 = Image.open('console_image1.png')
                            image1.paste(image1)
                            image1.show()
                            scr()
            
                        deleteimg()
                        probbbargraphdata()
                
                    elif int(ww.get())==10:
                        
                        def prollliinegraphdata():
                            
                            deleteimg()
                            db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                            cur=db.cursor()
                            a=[]
                            b=[]
                            sql="select unit, qty  from products"
                            cur.execute(sql)
                            dt=cur.fetchall()
                            for i in dt:
                                a.append(int(i[0]))
                                b.append(int(i[1]))
                                
                            plt.scatter(b,a)
                            plt.savefig('console_image.png')
                            plt.show()
                           
                            image = Image.open('console_image.png')
                            image.paste(image)
                            image.show()
                            scr()
                            
                        deleteimg()
                        prollliinegraphdata() 
                             
                    elif int(ww.get())==11:
                                        
                        def probbbarggraphdata():
                            
                            db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                            cur=db.cursor()
                            c=[]
                            d=[]
                            sql="select unit,qty  from products"
                            cur.execute(sql)
                            df=cur.fetchall()
                            for i in df:
                                c.append(int(i[0]))
                                d.append(int(i[1]))
                                
                            plt.bar(d,c)
                            plt.savefig('console_image1.png')
                            plt.show()
                            
                            image1 = Image.open('console_image1.png')
                            image1.paste(image1)
                            image1.show()
                            scr()
            
                        deleteimg()
                        probbbarggraphdata()
                
                c3=Canvas(SC,height=1160,width=800,bg='lavender')
                c3.place(x=360,y=0)
                ww=IntVar()
                
                r7=Radiobutton(c3,text=' SCATTER CHART (price and unit)',variable=ww,value=6,font=('arial',15),bg='lavender')
                r8=Radiobutton(c3,text='BAR CHART (price and unit)',variable=ww,value=7,font=('arial',15),bg='lavender')
                
                r7.place(x=20,y=70)
                r8.place(x=400,y=70)
                
                r5=Radiobutton(c3,text=' SCATTER CHART (prodid and qty)',variable=ww,value=4,font=('arial',15),bg='lavender')
                r6=Radiobutton(c3,text='BAR CHART (prodid and qty)',variable=ww,value=5,font=('arial',15),bg='lavender')
                
                r5.place(x=20,y=170)
                r6.place(x=400,y=170)
                
                r1=Radiobutton(c3,text=' SCATTER CHART (prodid and price )',variable=ww,value=0,font=('arial',15),bg='lavender')
                r2=Radiobutton(c3,text='BAR CHART (prodid and price)',variable=ww,value=1,font=('arial',15),bg='lavender')
                
                r1.place(x=20,y=270)
                r2.place(x=400,y=270)
                
                r3=Radiobutton(c3,text=' SCATTER CHART (prodid and unit)',variable=ww,value=2,font=('arial',15),bg='lavender')
                r4=Radiobutton(c3,text='BAR CHART (prodid and unit)',variable=ww,value=3,font=('arial',15),bg='lavender')
                
                r3.place(x=20,y=370)
                r4.place(x=400,y=370)
                
                r9=Radiobutton(c3,text=' SCATTER CHART (price and qty)',variable=ww,value=8,font=('arial',15),bg='lavender')
                r10=Radiobutton(c3,text='BAR CHART (price and qty)',variable=ww,value=9,font=('arial',15),bg='lavender')
                
                r9.place(x=20,y=470)
                r10.place(x=400,y=470)
                
                r11=Radiobutton(c3,text=' SCATTER CHART (unit and qty)',variable=ww,value=10,font=('arial',15),bg='lavender')
                r12=Radiobutton(c3,text='BAR CHART (unit and qty)',variable=ww,value=11,font=('arial',15),bg='lavender')
                
                r11.place(x=20,y=570)
                r12.place(x=400,y=570)
                
                deleteimg()
                bttt1=Button(c3,text='CREATE',command=procharts,font=('arial',15),bg='violet')
                bttt1.place(x=350,y=600)
                
            deleteimg()
            b102=Button(c2,text='Graph',bg='white',fg='purple',font=('arial',14),command=proccographdatabt)
            b102.place(x=10,y=260)
            scr()
            
        def sup():
            c2=Canvas(SC,height=1160,width=180,bg='violet')
            c2.place(x=180,y=0)
            z=Label(c2,text=' SUPPLIER  ',bg='purple',fg='white',font=('arial',21))
            z.place(x=3,y=3)
            def supsavebt():
                c3=Canvas(SC,height=1160,width=800,bg='lavender')
                c3.place(x=360,y=0)
                def savedata():
                    if len(a.get())==0 or len(b.get())==0 or len(c.get())==0 or len(d.get())==0 or len(e.get())==0 or len(f.get())==0 :
                        messagebox.showerror('ERROR','ENTER VAILD DATA')
                    else:
                        db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                        cur=db.cursor()
                        xid=a.get()
                        xname=b.get()
                        xadd=c.get()
                        xph=d.get()
                        xem=e.get()
                        xreg=f.get()
                        sql="insert into suppliers values('%s','%s','%s','%s','%s','%s')"%(xid,xname,xadd,xph,xem,xreg)
                        cur.execute(sql)
                        db.commit()
                        messagebox.showinfo('hi','datasaved')
                        db.close()
                        a.delete(0,100)
                        b.delete(0,100)
                        c.delete(0,100)
                        d.delete(0,100)
                        e.delete(0,100)
                        f.delete(0,100)
                        c3.destroy()
                        scr()
                def closed():
                    c3.destroy()
                    scr()
                
                idi=Label(c3,text='Suppliers id',font=('arial',15),bg='lavender')
                idi.place(x=50,y=70)
                a=Entry(c3,width=40)
                a.place(x=400,y=70)
                sname=Label(c3,text='Suppliers name',font=('arial',15),bg='lavender')
                sname.place(x=50,y=110)
                b=Entry(c3,width=40)
                b.place(x=400,y=110)
                add=Label(c3,text='Address',font=('arial',15),bg='lavender')
                add.place(x=50,y=150)
                c=Entry(c3,width=40)
                c.place(x=400,y=150)
                ph=Label(c3,text='Phone number',font=('arial',15),bg='lavender')
                ph.place(x=50,y=190)
                d=Entry(c3,width=40)
                d.place(x=400,y=190)
                em=Label(c3,text='Email id',font=('arial',15),bg='lavender')
                em.place(x=50,y=230)
                e=Entry(c3,width=40)
                e.place(x=400,y=230)
                reg=Label(c3,text='Registration number',font=('arial',15),bg='lavender')
                reg.place(x=50,y=270)
                f=Entry(c3,width=40)
                f.place(x=400,y=270)
                bt=Button(c3,text='Save',command=savedata,bg='green',font=('arial',15))
                bt.place(x=50,y=310)
                cl=Button(c3,text='Close',command=closed,bg='red',font=('arial',15))
                cl.place(x=400,y=310)
                
            b16=Button(c2,text='Insert',bg='white',fg='purple',font=('arial',14),command=supsavebt)
            b16.place(x=10,y=60)
            scr()

            def supfindbt():
                lt=[]
                c3=Canvas(SC,height=1160,width=800,bg='lavender')
                c3.place(x=360,y=0)
                def filldata():
                    db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                    cur=db.cursor()
                    sql="select supid from suppliers"
                    cur.execute(sql)
                    data=cur.fetchall()
                    for res in data:
                        lt.append(res[0])
                    db.close()
                def finddata():
                    db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                    cur=db.cursor()
                    xid=a.get()
                    sql="select sname,address,phone,email,regno from suppliers where supid=('%s')"%(xid)
                    cur.execute(sql) 
                    data=cur.fetchone()
                    b.delete(0,100)
                    c.delete(0,100)
                    d.delete(0,100)
                    e.delete(0,100)
                    f.delete(0,100)
                    b.insert(0,data[0])
                    c.insert(0,data[1])
                    d.insert(0,data[2])
                    e.insert(0,data[3])
                    f.insert(0,data[4])
                    db.close()
                def closed():
                    c3.destroy()
                    scr()
                
                idI=Label(c3,text='Suppliers id',font=('arial',15),bg='lavender')
                idI.place(x=50,y=30)
                a=ttk.Combobox(c3,width=20)
                filldata()
                a['values']=lt
                a.place(x=400,y=30)
                bt=Button(c3,text='Find',command=finddata,bg='blue',font=('arial',15))
                bt.place(x=100,y=70)
                sname=Label(c3,text='Suppliers name',font=('arial',15),bg='lavender')
                sname.place(x=50,y=110)
                b=Entry(c3,width=40)
                b.place(x=400,y=110)
                add=Label(c3,text='Address',font=('arial',15),bg='lavender')
                add.place(x=50,y=150)
                c=Entry(c3,width=40)
                c.place(x=400,y=150)
                ph=Label(c3,text='Phone number',font=('arial',15),bg='lavender')
                ph.place(x=50,y=190)
                d=Entry(c3,width=40)
                d.place(x=400,y=190)
                em=Label(c3,text='Email id',font=('arial',15),bg='lavender')
                em.place(x=50,y=230)
                e=Entry(c3,width=40)
                e.place(x=400,y=230)
                reg=Label(c3,text='Registration number',font=('arial',15),bg='lavender')
                reg.place(x=50,y=270)
                f=Entry(c3,width=40)
                f.place(x=400,y=270)
                cl=Button(c3,text='Close',command=closed,bg='red',font=('arial',15))
                cl.place(x=400,y=310)
                
                
                def supdata():
                    B1=[]
                    B2=[]
                    B3=[]
                    B4=[]
                    B5=[]
                    B6=[]
                    i=0
                    c3=Canvas(SC,height=1160,width=800,bg='lavender')
                    c3.place(x=360,y=0)
                    def filldata():
                        db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                        cur=db.cursor()
                        sql="select * from suppliers"
                        cur.execute(sql)
                        data=cur.fetchall()
                        for res in data:
                            B1.append(res[0])
                            B2.append(res[1])
                            B3.append(res[2])
                            B4.append(res[3])
                            B5.append(res[4])
                            B6.append(res[5])
                        db.close()
                    def firstdata():
                        global i
                        i=0
                        A1.config(text='')
                        A2.config(text='')
                        A3.config(text='')
                        A4.config(text='')
                        A5.config(text='')
                        A6.config(text='')
                        A1.config(text=B1[i])
                        A2.config(text=B2[i])
                        A3.config(text=B3[i])
                        A4.config(text=B4[i])
                        A5.config(text=B5[i])
                        A6.config(text=B6[i])
                    def nextdata():
                        global i
                        if i<len(B1)-1:
                            i=i+1
                            A1.config(text='')
                            A2.config(text='')
                            A3.config(text='')
                            A4.config(text='')
                            A5.config(text='')
                            A6.config(text='')
                            A1.config(text=B1[i])
                            A2.config(text=B2[i])
                            A3.config(text=B3[i])
                            A4.config(text=B4[i])
                            A5.config(text=B5[i])
                            A6.config(text=B6[i])
                
                        else:
                            messagebox.showinfo('Screen',"last record")
                    def lastdata():
                        global i
                        i=len(B1)-1
                        A1.config(text='')
                        A2.config(text='')
                        A3.config(text='')
                        A4.config(text='')
                        A5.config(text='')
                        A6.config(text='')
                        A1.config(text=B1[i])
                        A2.config(text=B2[i])
                        A3.config(text=B3[i])
                        A4.config(text=B4[i])
                        A5.config(text=B5[i])
                        A6.config(text=B6[i])
                    def prevdata():
                        global i
                        if i>0:
                            i=i-1
                            A1.config(text='')
                            A2.config(text='')
                            A3.config(text='')
                            A4.config(text='')
                            A5.config(text='')
                            A6.config(text='')
                            A1.config(text=B1[i])
                            A2.config(text=B2[i])
                            A3.config(text=B3[i])
                            A4.config(text=B4[i])
                            A5.config(text=B5[i])
                            A6.config(text=B6[i])
                        else:
                            messagebox.showinfo('Screen',"Already done")
                    def exitdata():
                        c3.destroy()
                        scr()
                    A=Label(c3,text='SUPPLIER ID',font=('arial',15),bg='lavender')
                    A.place(x=50,y=40)
                    A1=Label(c3,width=35)
                    A1.place(x=390,y=40)
                    B=Label(c3,text='SUPPLIER NAME',font=('arial',15),bg='lavender')
                    B.place(x=50,y=110)
                    A2=Label(c3,width=35)
                    A2.place(x=390,y=110)
                    C=Label(c3,text='ADDRESS',font=('arial',15),bg='lavender')
                    C.place(x=50,y=170)
                    A3=Label(c3,width=35)
                    A3.place(x=390,y=170)
                    D=Label(c3,text='PHONE NUMBER',font=('arial',15),bg='lavender')
                    D.place(x=50,y=230)
                    A4=Label(c3,width=35)
                    A4.place(x=390,y=230)
                    E=Label(c3,text='EMAIL',font=('arial',15),bg='lavender')
                    E.place(x=50,y=290)
                    A5=Label(c3,width=35)
                    A5.place(x=390,y=290)
                    F=Label(c3,text='REGISTRATION NUMBER',font=('arial',15),bg='lavender')
                    F.place(x=50,y=350)
                    A6=Label(c3,width=35)
                    A6.place(x=390,y=350)
                    BT1=Button(c3,text='FIRST',command=firstdata,bg='orange',font=('arial',15))
                    BT1.place(x=50,y=455)
                    BT2=Button(c3,text='NEXT',command=nextdata,bg='pink',font=('arial',15))
                    BT2.place(x=200,y=455)
                    BT3=Button(c3,text='LAST',command=lastdata,bg='green',font=('arial',15))
                    BT3.place(x=350,y=455)
                    BT4=Button(c3,text='PREVIOUS',command=prevdata,bg='blue',font=('arial',15))
                    BT4.place(x=500,y=455)
                    BT5=Button(c3,text='CLOSE',command=exitdata,bg='red',font=('arial',15))
                    BT5.place(x=650,y=455)
                    filldata()
                    
                b20=Button(c3,text='Records',bg='white',fg='purple',font=('arial',15),command=supdata)
                b20.place(x=600,y=310)
                

                
            b17=Button(c2,text='Find',bg='white',fg='purple',font=('arial',14),command=supfindbt)
            b17.place(x=10,y=110)
            scr()

            def supdeletebt():
                lt=[]
                c3=Canvas(SC,height=1160,width=800,bg='lavender')
                c3.place(x=360,y=0)
                def closed():
                    c3.destroy()
                    scr()
                def filldata():
                    db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                    cur=db.cursor()
                    sql="select supid from suppliers"
                    cur.execute(sql)
                    data=cur.fetchall()
                    for res in data:
                        lt.append(res[0])
                    db.close()
                def deletedata():
                    db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                    cur=db.cursor()
                    xa=d.get()
                    sql="delete from suppliers where supid=('%s')"%(xa)
                    cur.execute(sql)
                    db.commit()
                    messagebox.showinfo('Hi','Data Delete')
                    d.delete(0,100)
                    c3.destroy()
                    scr()
                a=Label(c3,text='supid',font=('arial',15),bg='lavender')
                a.place(x=50,y=70)
                d=ttk.Combobox(c3,width=20)
                filldata()
                d['values']=lt
                d.place(x=500,y=70)
                bt=Button(c3,text='Delete',command=deletedata,bg='blue',font=('arial',15))
                bt.place(x=300,y=150)
                bt=Button(c3,text='Close',command=closed,bg='red',font=('arial',15))
                bt.place(x=300,y=200)
                SC.mainloop()
            b19=Button(c2,text='Delete',bg='white',fg='purple',font=('arial',14),command=supdeletebt)
            b19.place(x=10,y=160)
            scr()

            def supupdatebt():
                lt=[]
                c3=Canvas(SC,height=1160,width=800,bg='lavender')
                c3.place(x=360,y=0)
            
                def filldata():
                    db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                    cur=db.cursor()
                    sql="select supid from suppliers"
                    cur.execute(sql)
                    data=cur.fetchall()
                    for res in data:
                        lt.append(res[0])
                    db.close()
                def finddata():
                    db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                    cur=db.cursor()
                    xid=a.get()
                    sql="select sname,address,phone,email,regno from suppliers where supid=('%s')"%(xid)
                    cur.execute(sql) 
                    data=cur.fetchone()
                    b.delete(0,100)
                    c.delete(0,100)
                    d.delete(0,100)
                    e.delete(0,100)
                    f.delete(0,100)
                    b.insert(0,data[0])
                    c.insert(0,data[1])
                    d.insert(0,data[2])
                    e.insert(0,data[3])
                    f.insert(0,data[4])
                    db.close()
                def updatedata():
                    if len(a.get())==0 or len(b.get())==0 or len(c.get())==0 or len(d.get())==0 or len(e.get())==0 or len(f.get())==0 :
                        messagebox.showerror('ERROR','ENTER VAILD DATA')
                    else:
                        db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                        cur=db.cursor()
                        xid=a.get()
                        xnm=b.get()
                        xadd=c.get()
                        xph=d.get()
                        xem=e.get()
                        xrg=f.get()
                        sql="update suppliers set sname='%s',address='%s',phone='%s',email='%s',regno='%s' where supid=('%s')"%(xnm,xadd,xph,xem,xrg,xid)
                        cur.execute(sql)
                        db.commit()
                        messagebox.showinfo('Hi','Update Done')
                        db.close()
                        a.delete(0,100)
                        b.delete(0,100)
                        c.delete(0,100)
                        d.delete(0,100)
                        e.delete(0,100)
                        f.delete(0,100)
                        c3.destroy()
                        scr()
                def closed():
                    c3.destroy()
                    scr()
                
                idI=Label(c3,text='Suppliers id',font=('arial',15),bg='lavender')
                idI.place(x=50,y=30)
                a=ttk.Combobox(c3,width=20)
                filldata()
                a['values']=lt
                a.place(x=400,y=30)
                bt=Button(c3,text='Find',command=finddata,bg='blue',font=('arial',15))
                bt.place(x=100,y=70)
                sname=Label(c3,text='Suppliers name',font=('arial',15),bg='lavender')
                sname.place(x=50,y=110)
                b=Entry(c3,width=40)
                b.place(x=400,y=110)
                add=Label(c3,text='Address',font=('arial',15),bg='lavender')
                add.place(x=50,y=150)
                c=Entry(c3,width=40)
                c.place(x=400,y=150)
                ph=Label(c3,text='Phone number',font=('arial',15),bg='lavender')
                ph.place(x=50,y=190)
                d=Entry(c3,width=40)
                d.place(x=400,y=190)
                em=Label(c3,text='Email id',font=('arial',15),bg='lavender')
                em.place(x=50,y=230)
                e=Entry(c3,width=40)
                e.place(x=400,y=230)
                reg=Label(c3,text='Registration number',font=('arial',15),bg='lavender')
                reg.place(x=50,y=270)
                f=Entry(c3,width=40)
                f.place(x=400,y=270)
                btt=Button(c3,text='Update',command=updatedata,bg='green',font=('arial',15))
                btt.place(x=300,y=310)
                cl=Button(c3,text='Close',command=closed,bg='red',font=('arial',15))
                cl.place(x=400,y=310)
            b18=Button(c2,text='Update',bg='white',fg='purple',font=('arial',14),command=supupdatebt)
            b18.place(x=10,y=210)
            scr()
            

        def stk():
            c2=Canvas(SC,height=1160,width=180,bg='violet')
            c2.place(x=180,y=0)
            z=Label(c2,text='    STOCK    ',bg='purple',fg='white',font=('arial',21))
            z.place(x=2,y=2)

            def stksavebt():
                c3=Canvas(SC,height=1160,width=800,bg='lavender')
                c3.place(x=360,y=0)
                def savedata():
                    if len(a.get())==0 or len(b.get())==0 or len(c.get())==0 or len(d.get())==0 or len(e.get())==0 or len(f.get())==0 or len(g.get())==0:
                        messagebox.showerror('ERROR','ENTER VAILD DATA')
                    else:
                        db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                        cur=db.cursor()
                        xsid=a.get()
                        xcatid=b.get()
                        xsupid=c.get()
                        xprodid=d.get()
                        xpname=e.get()
                        xqty=int(f.get())
                        xdate=g.get()
                        sql="insert into stockin values('%s','%s','%s','%s','%s',%d,'%s')"%(xsid,xcatid,xsupid,xprodid,xpname,xqty,xdate)
                        cur.execute(sql)
                        db.commit()
                        messagebox.showinfo('Hi','saved')
                        db.close()
                        a.delete(0,100)
                        b.delete(0,100)
                        c.delete(0,100)
                        d.delete(0,100)
                        e.delete(0,100)
                        f.delete(0,100)
                        g.delete(0,100)
                        c3.destroy()
                        scr()
                def closed():
                    c3.destroy()
                    scr()
                
                sid=Label(c3,text='Stock id',font=('arial',15),bg='lavender')
                sid.place(x=50,y=70)
                a=Entry(c3,width=40)
                a.place(x=400,y=70)
                catid=Label(c3,text='Category id',font=('arial',15),bg='lavender')
                catid.place(x=50,y=110)
                b=Entry(c3,width=40)
                b.place(x=400,y=110)
                supid=Label(c3,text='Supplier id',font=('arial',15),bg='lavender')
                supid.place(x=50,y=150)
                c=Entry(c3,width=40)
                c.place(x=400,y=150)
                prodid=Label(c3,text='Product id',font=('arial',15),bg='lavender')
                prodid.place(x=50,y=190)
                d=Entry(c3,width=40)
                d.place(x=400,y=190)
                pname=Label(c3,text='Product name',font=('arial',15),bg='lavender')
                pname.place(x=50,y=230)
                e=Entry(c3,width=40)
                e.place(x=400,y=230)
                qty=Label(c3,text='Quantity',font=('arial',15),bg='lavender')
                qty.place(x=50,y=270)
                f=Entry(c3,width=40)
                f.place(x=400,y=270)
                date=Label(c3,text='Date',font=('arial',15),bg='lavender')
                date.place(x=50,y=310)
                g=Entry(c3,width=40)
                g.place(x=400,y=310)
                bt=Button(c3,text='Save',command=savedata,bg='green',font=('arial',15))
                bt.place(x=50,y=350)
                cl=Button(c3,text='Close',command=closed,bg='red',font=('arial',15))
                cl.place(x=400,y=350)
            b21=Button(c2,text='Insert',bg='white',fg='purple',font=('arial',14),command=stksavebt)
            b21.place(x=10,y=60)
            scr()

            def stkfindbt():
                c3=Canvas(SC,height=1160,width=800,bg='lavender')
                c3.place(x=360,y=0)
                def closed():
                    c3.destroy()
                    scr()
                lt=[]
                def filldata():
                    db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                    cur=db.cursor()
                    sql="select sid from stockin"
                    cur.execute(sql)
                    data=cur.fetchall()
                    for res in data:
                        lt.append(res[0])
                    db.close()
                def finddata():
                    db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                    cur=db.cursor()
                    xid=a.get()
                    sql="select catid,supid,prodid,pname,qty, datein from stockin where sid=('%s')"%(xid)
                    cur.execute(sql) 
                    data=cur.fetchone()
                    b.delete(0,100)
                    c.delete(0,100)
                    d.delete(0,100)
                    e.delete(0,100)
                    f.delete(0,100)
                    g.delete(0,100)
                    b.insert(0,data[0])
                    c.insert(0,data[1])
                    d.insert(0,data[2])
                    e.insert(0,data[3])
                    f.insert(0,str(data[4]))
                    g.insert(0,data[5])
                    db.close()
            
                
                sid=Label(c3,text='Stock id',font=('arial',15),bg='lavender')
                sid.place(x=50,y=30)
                a=ttk.Combobox(c3,width=20)
                filldata()
                a['values']=lt
                a.place(x=400,y=30)
                bt=Button(c3,text='Find',command=finddata,bg='blue',font=('arial',15))
                bt.place(x=100,y=70)
                catid=Label(c3,text='Category id',font=('arial',15),bg='lavender')
                catid.place(x=50,y=110)
                b=Entry(c3,width=40)
                b.place(x=400,y=110)
                supid=Label(c3,text='Supplier id',font=('arial',15),bg='lavender')
                supid.place(x=50,y=150)
                c=Entry(c3,width=40)
                c.place(x=400,y=150)
                prodid=Label(c3,text='Product id',font=('arial',15),bg='lavender')
                prodid.place(x=50,y=190)
                d=Entry(c3,width=40)
                d.place(x=400,y=190)
                pname=Label(c3,text='Product name',font=('arial',15),bg='lavender')
                pname.place(x=50,y=230)
                e=Entry(c3,width=40)
                e.place(x=400,y=230)
                qty=Label(c3,text='Quantity',font=('arial',15),bg='lavender')
                qty.place(x=50,y=270)
                f=Entry(c3,width=40)
                f.place(x=400,y=270)
                date=Label(c3,text='Date',font=('arial',15),bg='lavender')
                date.place(x=50,y=310)
                g=Entry(c3,width=40)
                g.place(x=400,y=310)
                ba=Button(c3,text='Close',command=closed,bg='red',font=('arial',15))
                ba.place(x=400,y=350)
                def stkdata():
                    B1=[]
                    B2=[]
                    B3=[]
                    B4=[]
                    B5=[]
                    B6=[]
                    B7=[]
                    i=0
                    c3=Canvas(SC,height=1160,width=800,bg='lavender')
                    c3.place(x=360,y=0)
                    def filldata():
                        db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                        cur=db.cursor()
                        sql="select * from stockin"
                        cur.execute(sql)
                        data=cur.fetchall()
                        for res in data:
                            B1.append(res[0])
                            B2.append(res[1])
                            B3.append(res[2])
                            B4.append(res[3])
                            B5.append(res[4])
                            B6.append(res[5])
                            B7.append(res[6])
                        db.close()
                    def firstdata():
                        global i
                        i=0
                        A1.config(text='')
                        A2.config(text='')
                        A3.config(text='')
                        A4.config(text='')
                        A5.config(text='')
                        A6.config(text='')
                        A7.config(text='')
                        A1.config(text=B1[i])
                        A2.config(text=B2[i])
                        A3.config(text=B3[i])
                        A4.config(text=B4[i])
                        A5.config(text=B5[i])
                        A6.config(text=B6[i])
                        A7.config(text=B7[i])
                    def nextdata():
                        global i
                        if i<len(B1)-1:
                            i=i+1
                            A1.config(text='')
                            A2.config(text='')
                            A3.config(text='')
                            A4.config(text='')
                            A5.config(text='')
                            A6.config(text='')
                            A7.config(text='')
                            A1.config(text=B1[i])
                            A2.config(text=B2[i])
                            A3.config(text=B3[i])
                            A4.config(text=B4[i])
                            A5.config(text=B5[i])
                            A6.config(text=B6[i])
                            A7.config(text=B7[i])
                
                        else:
                            messagebox.showinfo('Screen',"last record")
                    def lastdata():
                        global i
                        i=len(B1)-1
                        A1.config(text='')
                        A2.config(text='')
                        A3.config(text='')
                        A4.config(text='')
                        A5.config(text='')
                        A6.config(text='')
                        A7.config(text='')
                        A1.config(text=B1[i])
                        A2.config(text=B2[i])
                        A3.config(text=B3[i])
                        A4.config(text=B4[i])
                        A5.config(text=B5[i])
                        A6.config(text=B6[i])
                        A7.config(text=B7[i])
                    def prevdata():
                        global i
                        if i>0:
                            i=i-1
                            A1.config(text='')
                            A2.config(text='')
                            A3.config(text='')
                            A4.config(text='')
                            A5.config(text='')
                            A6.config(text='')
                            A7.config(text='')
                            A1.config(text=B1[i])
                            A2.config(text=B2[i])
                            A3.config(text=B3[i])
                            A4.config(text=B4[i])
                            A5.config(text=B5[i])
                            A6.config(text=B6[i])
                            A7.config(text=B7[i])
                        else:
                            messagebox.showinfo('Screen',"Already done")
                    def exitdata():
                        c3.destroy()
                        scr()
                    
                    A=Label(c3,text='STOCK ID',font=('arial',15),bg='lavender')
                    A.place(x=50,y=40)
                    A1=Label(c3,width=35)
                    A1.place(x=390,y=40)
                    B=Label(c3,text='CATEGORY ID',font=('arial',15),bg='lavender')
                    B.place(x=50,y=110)
                    A2=Label(c3,width=35)
                    A2.place(x=390,y=110)
                    C=Label(c3,text='SUPPLIER ID',font=('arial',15),bg='lavender')
                    C.place(x=50,y=170)
                    A3=Label(c3,width=35)
                    A3.place(x=390,y=170)
                    D=Label(c3,text='PRODUCT ID',font=('arial',15),bg='lavender')
                    D.place(x=50,y=230)
                    A4=Label(c3,width=35)
                    A4.place(x=390,y=230)
                    E=Label(c3,text='PRODUCT NAME',font=('arial',15),bg='lavender')
                    E.place(x=50,y=290)
                    A5=Label(c3,width=35)
                    A5.place(x=390,y=290)
                    F=Label(c3,text='QUANTITY',font=('arial',15),bg='lavender')
                    F.place(x=50,y=350)
                    A6=Label(c3,width=35)
                    A6.place(x=390,y=350)
                    G=Label(c3,text='DATE IN',font=('arial',15),bg='lavender')
                    G.place(x=50,y=410)
                    A7=Label(c3,width=35)
                    A7.place(x=390,y=410)
                    BT1=Button(c3,text='FIRST',command=firstdata,bg='orange',font=('arial',15))
                    BT1.place(x=50,y=455)
                    BT2=Button(c3,text='NEXT',command=nextdata,bg='pink',font=('arial',15))
                    BT2.place(x=200,y=455)
                    BT3=Button(c3,text='LAST',command=lastdata,bg='green',font=('arial',15))
                    BT3.place(x=350,y=455)
                    BT4=Button(c3,text='PREVIOUS',command=prevdata,bg='blue',font=('arial',15))
                    BT4.place(x=500,y=455)
                    BT5=Button(c3,text='CLOSE',command=exitdata,bg='red',font=('arial',15))
                    BT5.place(x=650,y=455)
                    filldata()
                    
                    
                b25=Button(c3,text='Records',bg='white',fg='purple',font=('arial',15),command=stkdata)
                b25.place(x=600,y=350)
                

            b22=Button(c2,text='Find',bg='white',fg='purple',font=('arial',14),command=stkfindbt)
            b22.place(x=10,y=110)
            scr()
            def stkdeletebt():
                lt=[]
                c3=Canvas(SC,height=1160,width=800,bg='lavender')
                c3.place(x=360,y=0)
                def filldata():
                    db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                    cur=db.cursor()
                    sql="select sid from stockin"
                    cur.execute(sql)
                    data=cur.fetchall()
                    for res in data:
                        lt.append(res[0])
                    db.close()
                def deletedata():
                    db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                    cur=db.cursor()
                    xa=d.get()
                    sql="delete from stockin where sid=('%s')"%(xa)
                    cur.execute(sql)
                    d.delete(0,100)
                    db.commit()
                    messagebox.showinfo('Hi','Data Delete')
                    c3.destroy()
                    scr()
                def closed():
                    c3.destroy()
                    scr()
                
                a=Label(c3,text='Stock id',font=('arial',15),bg='lavender')
                a.place(x=50,y=70)
                d=ttk.Combobox(c3,width=20)
                filldata()
                d['values']=lt
                d.place(x=500,y=70)
                bt=Button(c3,text='Delete',command=deletedata,bg='blue',font=('arial',15))
                bt.place(x=300,y=150)
                bt=Button(c3,text='Close',command=closed,bg='red',font=('arial',15))
                bt.place(x=300,y=200)
            
            b24=Button(c2,text='Delete',bg='white',fg='purple',font=('arial',14),command=stkdeletebt)
            b24.place(x=10,y=210)

            
            def stkupdatebt():
                c3=Canvas(SC,height=1160,width=800,bg='lavender')
                c3.place(x=360,y=0)
                def closed():
                    c3.destroy()
                    scr()
                lt=[]
                def filldata():
                    db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                    cur=db.cursor()
                    sql="select sid from stockin"
                    cur.execute(sql)
                    data=cur.fetchall()
                    for res in data:
                        lt.append(res[0])
                    db.close()
                def finddata():
                    db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                    cur=db.cursor()
                    xid=a.get()
                    sql="select catid,supid,prodid,pname,qty, datein from stockin where sid=('%s')"%(xid)
                    cur.execute(sql) 
                    data=cur.fetchone()
                    b.delete(0,100)
                    c.delete(0,100)
                    d.delete(0,100)
                    e.delete(0,100)
                    f.delete(0,100)
                    g.delete(0,100)
                    b.insert(0,data[0])
                    c.insert(0,data[1])
                    d.insert(0,data[2])
                    e.insert(0,data[3])
                    f.insert(0,str(data[4]))
                    g.insert(0,data[5])
                    db.close()
                def dataupdate():
                    if len(a.get())==0 or len(b.get())==0 or len(c.get())==0 or len(d.get())==0 or len(e.get())==0 or len(f.get())==0 or len(g.get())==0:
                        messagebox.showerror('ERROR','ENTER VAILD DATA')
                    else:
                         db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                         cur=db.cursor()
                         xsid=a.get()
                         xcatid=b.get()
                         xsupid=c.get()
                         xprodid=d.get()
                         xpname=e.get()
                         xqty=int(f.get())
                         xdate=g.get()
                         sql="update stockin set catid='%s',supid='%s',prodid='%s',pname='%s',qty=%d,datein='%s' where sid=('%s')"%(xcatid,xsupid,xprodid,xpname,xqty,xdate,xsid)
                         cur.execute(sql)
                         db.commit()
                         messagebox.showinfo('Hi','Update Done')
                         db.close()
                         a.delete(0,100)
                         b.delete(0,100)
                         c.delete(0,100)
                         d.delete(0,100)
                         e.delete(0,100)
                         f.delete(0,100)
                         g.delete(0,100)
                         c3.destroy()
                         scr()
                
                sid=Label(c3,text='Stock id',font=('arial',15),bg='lavender')
                sid.place(x=50,y=30)
                a=ttk.Combobox(c3,width=20)
                filldata()
                a['values']=lt
                a.place(x=400,y=30)
                bt=Button(c3,text='Find',command=finddata,bg='blue',font=('arial',15))
                bt.place(x=100,y=70)
                catid=Label(c3,text='Category id',font=('arial',15),bg='lavender')
                catid.place(x=50,y=110)
                b=Entry(c3,width=40)
                b.place(x=400,y=110)
                supid=Label(c3,text='Supplier id',font=('arial',15),bg='lavender')
                supid.place(x=50,y=150)
                c=Entry(c3,width=40)
                c.place(x=400,y=150)
                prodid=Label(c3,text='Product id',font=('arial',15),bg='lavender')
                prodid.place(x=50,y=190)
                d=Entry(c3,width=40)
                d.place(x=400,y=190)
                pname=Label(c3,text='Product name',font=('arial',15),bg='lavender')
                pname.place(x=50,y=230)
                e=Entry(c3,width=40)
                e.place(x=400,y=230)
                qty=Label(c3,text='Quantity',font=('arial',15),bg='lavender')
                qty.place(x=50,y=270)
                f=Entry(c3,width=40)
                f.place(x=400,y=270)
                date=Label(c3,text='Date',font=('arial',15),bg='lavender')
                date.place(x=50,y=310)
                g=Entry(c3,width=40)
                g.place(x=400,y=310)
                cl=Button(c3,text='Close',command=closed,bg='red',font=('arial',15))
                cl.place(x=400,y=350)
                up=Button(c3,text='Update',command=dataupdate,bg='green',font=('arial',15))
                up.place(x=50,y=350)
                
            b23=Button(c2,text='Update',bg='white',fg='purple',font=('arial',14),command=stkupdatebt)
            b23.place(x=10,y=160)

            def stkccographdatabt():
                
                def stkcharts():
                    deleteimg()
                    if int(w.get())==0:
                        
                        def stklinegraphdata():
                            
                            deleteimg()
                            db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                            cur=db.cursor()
                            a=[]
                            b=[]
                            sql="select sid , qty   from stockin"
                            cur.execute(sql)
                            dt=cur.fetchall()
                            for i in dt:
                                a.append(i[0])
                                b.append(int(i[1]))
                                
                            plt.scatter(b,a)
                            plt.savefig('console_image.png')
                            plt.show()
                           
                            image = Image.open('console_image.png')
                            image.paste(image)
                            image.show()
                            scr()
                            
                        deleteimg()
                        stklinegraphdata() 
                        
                        
                        
                    elif int(w.get())==1:
                                        
                        def stkbargraphdata():
                            
                            db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                            cur=db.cursor()
                            c=[]
                            d=[]
                            sql="select sid,qty from stockin"
                            cur.execute(sql)
                            df=cur.fetchall()
                            for i in df:
                                c.append(i[0])
                                d.append(int(i[1]))
                                
                            plt.bar(d,c)
                            plt.savefig('console_image1.png')
                            plt.show()
                            
                            image1 = Image.open('console_image1.png')
                            image1.paste(image1)
                            image1.show()
                            scr()
            
                        deleteimg()
                        stkbargraphdata()
                        
                    elif int(w.get())==2:
                                        
                        def stkkbargraaphdata():
                            
                            db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                            cur=db.cursor()
                            c=[]
                            d=[]
                            sql="select sid, datein from stockin"
                            cur.execute(sql)
                            df=cur.fetchall()
                            for i in df:
                                c.append(i[0])
                                d.append(i[1])
                                
                            plt.scatter(d,c)
                            plt.savefig('console_image1.png')
                            plt.show()
                            
                            image1 = Image.open('console_image1.png')
                            image1.paste(image1)
                            image1.show()
                            scr()
            
                        deleteimg()
                        stkkbargraaphdata()
                    
                    
                    elif int(w.get())==3:
                                        
                        def stokbargraphdata():
                            
                            db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                            cur=db.cursor()
                            c=[]
                            d=[]
                            sql="select sid, datein from stockin"
                            cur.execute(sql)
                            df=cur.fetchall()
                            for i in df:
                                c.append(i[0])
                                d.append(i[1])
                                
                            plt.bar(d,c)
                            plt.savefig('console_image1.png')
                            plt.show()
                            
                            image1 = Image.open('console_image1.png')
                            image1.paste(image1)
                            image1.show()
                            scr()
            
                        deleteimg()
                        stokbargraphdata()
                        
                    elif int(w.get())==4:
                                        
                        def stookbargraphdata():
                            
                            db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                            cur=db.cursor()
                            c=[]
                            d=[]
                            sql="select pname,qty  from stockin"
                            cur.execute(sql)
                            df=cur.fetchall()
                            for i in df:
                                c.append(i[0])
                                d.append(int(i[1]))
                                
                            plt.scatter(d,c)
                            plt.savefig('console_image1.png')
                            plt.show()
                            
                            image1 = Image.open('console_image1.png')
                            image1.paste(image1)
                            image1.show()
                            scr()
            
                        deleteimg()
                        stookbargraphdata()
                    
                    elif int(w.get())==5:
                                        
                        def sstkbbargraphdata():
                            
                            db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                            cur=db.cursor()
                            c=[]
                            d=[]
                            sql="select pname,qty  from stockin"
                            cur.execute(sql)
                            df=cur.fetchall()
                            for i in df:
                                c.append(i[0])
                                d.append(int(i[1]))
                                
                            plt.bar(d,c)
                            plt.savefig('console_image1.png')
                            plt.show()
                            
                            image1 = Image.open('console_image1.png')
                            image1.paste(image1)
                            image1.show()
                            scr()
            
                        deleteimg()
                        sstkbbargraphdata()
                        
                    elif int(w.get())==6:
                                        
                        def ssstkbbargraphdata():
                            
                            db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                            cur=db.cursor()
                            c=[]
                            d=[]
                            sql="select datein ,qty  from stockin"
                            cur.execute(sql)
                            df=cur.fetchall()
                            for i in df:
                                c.append(i[0])
                                d.append(int(i[1]))
                                
                            plt.scatter(d,c)
                            plt.savefig('console_image1.png')
                            plt.show()
                            
                            image1 = Image.open('console_image1.png')
                            image1.paste(image1)
                            image1.show()
                            scr()
            
                        deleteimg()
                        ssstkbbargraphdata()
                        
                    elif int(w.get())==7:
                                        
                        def stttokbbargraphdata():
                            
                            db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                            cur=db.cursor()
                            c=[]
                            d=[]
                            sql="select datein ,qty  from stockin"
                            cur.execute(sql)
                            df=cur.fetchall()
                            for i in df:
                                c.append(i[0])
                                d.append(int(i[1]))
                                
                            plt.bar(d,c)
                            plt.savefig('console_image1.png')
                            plt.show()
                            
                            image1 = Image.open('console_image1.png')
                            image1.paste(image1)
                            image1.show()
                            scr()
            
                        deleteimg()
                        stttokbbargraphdata()
                        
                    
                c3=Canvas(SC,height=1160,width=800,bg='lavender')
                c3.place(x=360,y=0)
                w=IntVar()
                
                r7=Radiobutton(c3,text=' SCATTER CHART (datein and qty)',variable=w,value=6,font=('arial',15),bg='lavender')
                r8=Radiobutton(c3,text='BAR CHART (datein and qty)',variable=w,value=7,font=('arial',15),bg='lavender')
                
                r7.place(x=20,y=70)
                r8.place(x=400,y=70)
                
                r5=Radiobutton(c3,text=' SCATTER CHART (pname and qty)',variable=w,value=4,font=('arial',15),bg='lavender')
                r6=Radiobutton(c3,text='BAR CHART (pname and qty)',variable=w,value=5,font=('arial',15),bg='lavender')
                
                r5.place(x=20,y=170)
                r6.place(x=400,y=170)
                
                r1=Radiobutton(c3,text=' SCATTER CHART (sid and qty )',variable=w,value=0,font=('arial',15),bg='lavender')
                r2=Radiobutton(c3,text='BAR CHART (sid and qty)',variable=w,value=1,font=('arial',15),bg='lavender')
                
                r1.place(x=20,y=270)
                r2.place(x=400,y=270)
                
                r3=Radiobutton(c3,text=' SCATTER CHART (sid and datein)',variable=w,value=2,font=('arial',15),bg='lavender')
                r4=Radiobutton(c3,text='BAR CHART (sid and datein)',variable=w,value=3,font=('arial',15),bg='lavender')
                
                r3.place(x=20,y=370)
                r4.place(x=400,y=370)
                
                
                deleteimg()
                bttt1=Button(c3,text='CREATE',command=stkcharts,font=('arial',15),bg='violet')
                bttt1.place(x=350,y=500)
                
            deleteimg()
            b102=Button(c2,text='Graph',bg='white',fg='purple',font=('arial',14),command=stkccographdatabt)
            b102.place(x=10,y=260)
            scr()
            
        def cus():
            c2=Canvas(SC,height=1160,width=180,bg='violet')
            c2.place(x=180,y=0)
            z=Label(c2,text='CUSTOMER ',bg='purple',fg='white',font=('arial',21))
            z.place(x=3,y=3)
            def cussavebt():
                c3=Canvas(SC,height=1160,width=800,bg='lavender')
                c3.place(x=360,y=0)
                def savedata():
                    if len(a.get())==0 or len(b.get())==0 or len(c.get())==0 or len(d.get())==0 or len(e.get())==0 :
                        messagebox.showerror('ERROR','ENTER VAILD DATA')
                    else:
                        db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                        cur=db.cursor()
                        xid=a.get()
                        xname=b.get()
                        xadd=c.get()
                        xph=d.get()
                        xem=e.get()
                        sql="insert into customer values('%s','%s','%s','%s','%s')"%(xid,xname,xadd,xph,xem)
                        cur.execute(sql)
                        db.commit()
                        messagebox.showinfo('hi','datasaved')
                        db.close()
                        a.delete(0,100)
                        b.delete(0,100)
                        c.delete(0,100)
                        d.delete(0,100)
                        e.delete(0,100)
                        f.delete(0,100)
                        c3.destroy()
                        scr()
                def closed():
                    c3.destroy()
                    scr()
                
                idI=Label(c3,text='Customer id',font=('arial',15),bg='lavender')
                idI.place(x=50,y=70)
                a=Entry(c3,width=40)
                a.place(x=400,y=70)
                sname=Label(c3,text='Customer name',font=('arial',15),bg='lavender')
                sname.place(x=50,y=110)
                b=Entry(c3,width=40)
                b.place(x=400,y=110)
                add=Label(c3,text='Address',font=('arial',15),bg='lavender')
                add.place(x=50,y=150)
                c=Entry(c3,width=40)
                c.place(x=400,y=150)
                ph=Label(c3,text='Phone number',font=('arial',15),bg='lavender')
                ph.place(x=50,y=190)
                d=Entry(c3,width=40)
                d.place(x=400,y=190)
                em=Label(c3,text='Email id',font=('arial',15),bg='lavender')
                em.place(x=50,y=230)
                e=Entry(c3,width=40)
                e.place(x=400,y=230)
                bt=Button(c3,text='Save',command=savedata,bg='green',font=('arial',15))
                bt.place(x=50,y=310)
                cl=Button(c3,text='Close',command=closed,bg='red',font=('arial',15))
                cl.place(x=400,y=310)
                
            b26=Button(c2,text='Insert',bg='white',fg='purple',font=('arial',14),command=cussavebt)
            b26.place(x=10,y=60)
            scr()

            def cusfindbt():
                lt=[]
                c3=Canvas(SC,height=1160,width=800,bg='lavender')
                c3.place(x=360,y=0)
                def filldata():
                    db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                    cur=db.cursor()
                    sql="select custid from customer"
                    cur.execute(sql)
                    data=cur.fetchall()
                    for res in data:
                        lt.append(res[0])
                    db.close()
                def finddata():
                    db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                    cur=db.cursor()
                    xid=a.get()
                    sql="select name,address,email,phone from customer where custid=('%s')"%(xid)
                    cur.execute(sql) 
                    data=cur.fetchone()
                    db.close()
                    b.delete(0,100)
                    c.delete(0,100)
                    d.delete(0,100)
                    e.delete(0,100)
                    b.insert(0,data[0])
                    c.insert(0,data[1])
                    d.insert(0,data[2])
                    e.insert(0,data[3])
                def closed():
                    c3.destroy()
                    scr()
                
                idI=Label(c3,text='Customer id',font=('arial',15),bg='lavender')
                idI.place(x=50,y=30)
                a=ttk.Combobox(c3,width=20)
                filldata()
                a['values']=lt
                a.place(x=400,y=30)
                bt=Button(c3,text='Find',command=finddata,bg='green',font=('arial',15))
                bt.place(x=100,y=70)
                name=Label(c3,text='Customer name',font=('arial',15),bg='lavender')
                name.place(x=50,y=110)
                b=Entry(c3,width=40)
                b.place(x=400,y=110)
                add=Label(c3,text='Address',font=('arial',15),bg='lavender')
                add.place(x=50,y=150)
                c=Entry(c3,width=40)
                c.place(x=400,y=150)
                ph=Label(c3,text='Phone number',font=('arial',15),bg='lavender')
                ph.place(x=50,y=190)
                d=Entry(c3,width=40)
                d.place(x=400,y=190)
                em=Label(c3,text='Email id',font=('arial',15),bg='lavender')
                em.place(x=50,y=230)
                e=Entry(c3,width=40)
                e.place(x=400,y=230)
                cl=Button(c3,text='Close',command=closed,bg='red',font=('arial',15))
                cl.place(x=400,y=310)
                def cusdata():
                    B1=[]
                    B2=[]
                    B3=[]
                    B4=[]
                    B5=[]
                    i=0
                    c3=Canvas(SC,height=1160,width=800,bg='lavender')
                    c3.place(x=360,y=0)
                    def filldata():
                        db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                        cur=db.cursor()
                        sql="select * from customer"
                        cur.execute(sql)
                        data=cur.fetchall()
                        for res in data:
                            B1.append(res[0])
                            B2.append(res[1])
                            B3.append(res[2])
                            B4.append(res[3])
                            B5.append(res[4])
                            
                        db.close()
                    def firstdata():
                        global i
                        i=0
                        A1.config(text='')
                        A2.config(text='')
                        A3.config(text='')
                        A4.config(text='')
                        A5.config(text='')
                        
                        A1.config(text=B1[i])
                        A2.config(text=B2[i])
                        A3.config(text=B3[i])
                        A4.config(text=B4[i])
                        A5.config(text=B5[i])
                
                        
                    def nextdata():
                        global i
                        if i<len(B1)-1:
                            i=i+1
                            A1.config(text='')
                            A2.config(text='')
                            A3.config(text='')
                            A4.config(text='')
                            A5.config(text='')
                            
                            A1.config(text=B1[i])
                            A2.config(text=B2[i])
                            A3.config(text=B3[i])
                            A4.config(text=B4[i])
                            A5.config(text=B5[i])
                            
                
                        else:
                            messagebox.showinfo('Screen',"last record")
                    def lastdata():
                        global i
                        i=len(B1)-1
                        A1.config(text='')
                        A2.config(text='')
                        A3.config(text='')
                        A4.config(text='')
                        A5.config(text='')
                        
                        A1.config(text=B1[i])
                        A2.config(text=B2[i])
                        A3.config(text=B3[i])
                        A4.config(text=B4[i])
                        A5.config(text=B5[i])
                        
                    def prevdata():
                        global i
                        if i>0:
                            i=i-1
                            A1.config(text='')
                            A2.config(text='')
                            A3.config(text='')
                            A4.config(text='')
                            A5.config(text='')
                            
                            A1.config(text=B1[i])
                            A2.config(text=B2[i])
                            A3.config(text=B3[i])
                            A4.config(text=B4[i])
                            A5.config(text=B5[i])
                            
                        else:
                            messagebox.showinfo('Screen',"Already done")
                    def exitdata():
                        c3.destroy()
                        scr()
                    
                    A=Label(c3,text='CUSTOMER ID',font=('arial',15),bg='lavender')
                    A.place(x=50,y=40)
                    A1=Label(c3,width=35)
                    A1.place(x=390,y=40)
                    B=Label(c3,text='NAME',font=('arial',15),bg='lavender')
                    B.place(x=50,y=110)
                    A2=Label(c3,width=35)
                    A2.place(x=390,y=110)
                    C=Label(c3,text='ADDRESS',font=('arial',15),bg='lavender')
                    C.place(x=50,y=170)
                    A3=Label(c3,width=35)
                    A3.place(x=390,y=170)
                    D=Label(c3,text='EMAIL',font=('arial',15),bg='lavender')
                    D.place(x=50,y=230)
                    A4=Label(c3,width=35)
                    A4.place(x=390,y=230)
                    E=Label(c3,text='PHONE',font=('arial',15),bg='lavender')
                    E.place(x=50,y=290)
                    A5=Label(c3,width=35)
                    A5.place(x=390,y=290)
                    BT1=Button(c3,text='FIRST',command=firstdata,bg='orange',font=('arial',15))
                    BT1.place(x=50,y=455)
                    BT2=Button(c3,text='NEXT',command=nextdata,bg='pink',font=('arial',15))
                    BT2.place(x=200,y=455)
                    BT3=Button(c3,text='LAST',command=lastdata,bg='green',font=('arial',15))
                    BT3.place(x=350,y=455)
                    BT4=Button(c3,text='PREVIOUS',command=prevdata,bg='blue',font=('arial',15))
                    BT4.place(x=500,y=455)
                    BT5=Button(c3,text='CLOSE',command=exitdata,bg='red',font=('arial',15))
                    BT5.place(x=650,y=455)
                    filldata()
                    
                b30=Button(c3,text='Records',bg='white',fg='purple',font=('arial',15),command=cusdata)
                b30.place(x=600,y=310)
                scr()
            b27=Button(c2,text='Find',bg='white',fg='purple',font=('arial',14),command=cusfindbt)
            b27.place(x=10,y=110)
            scr()
            def cusdeletebt():
                lt=[]
                c3=Canvas(SC,height=1160,width=800,bg='lavender')
                c3.place(x=360,y=0)
                def filldata():
                    db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                    cur=db.cursor()
                    sql="select custid from customer"
                    cur.execute(sql)
                    data=cur.fetchall()
                    for res in data:
                        lt.append(res[0])
                    db.close()
                def deletedata():
                    db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                    cur=db.cursor()
                    xa=d.get()
                    sql="delete from customer where custid=('%s')"%(xa)
                    cur.execute(sql)
                    db.commit()
                    messagebox.showinfo('Hi','Data Delete')
                    d.delete(0,100)
                    c3.destroy()
                    scr()
                def closed():
                    c3.destroy()
                    scr()
                
                a=Label(c3,text='Customer id',font=('arial',15),bg='lavender')
                a.place(x=50,y=70)
                d=ttk.Combobox(c3,width=20)
                filldata()
                d['values']=lt
                d.place(x=500,y=70)
                bt=Button(c3,text='Delete',command=deletedata,bg='blue',font=('arial',15))
                bt.place(x=300,y=150)
                bt=Button(c3,text='Close',command=closed,bg='red',font=('arial',15))
                bt.place(x=300,y=200)
                
            b29=Button(c2,text='Delete',bg='white',fg='purple',font=('arial',14),command=cusdeletebt)
            b29.place(x=10,y=210)
            scr()
           
            def cusupdatebt():
                lt=[]
                c3=Canvas(SC,height=1160,width=800,bg='lavender')
                c3.place(x=360,y=0)
                def filldata():
                    db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                    cur=db.cursor()
                    sql="select custid from customer"
                    cur.execute(sql)
                    data=cur.fetchall()
                    for res in data:
                        lt.append(res[0])
                    db.close()
                def finddata():
                    db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                    cur=db.cursor()
                    xid=a.get()
                    sql="select name,address,email,phone from customer where custid=('%s')"%(xid)
                    cur.execute(sql) 
                    data=cur.fetchone()
                    db.close()
                    b.delete(0,100)
                    c.delete(0,100)
                    d.delete(0,100)
                    e.delete(0,100)
                    b.insert(0,data[0])
                    c.insert(0,data[1])
                    d.insert(0,data[2])
                    e.insert(0,data[3])
                def updatedata():
                    if len(a.get())==0 or len(b.get())==0 or len(c.get())==0 or len(d.get())==0 or len(e.get())==0 :
                        messagebox.showerror('ERROR','ENTER VAILD DATA')
                    else:
                        db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                        cur=db.cursor()
                        xid=a.get()
                        xnm=b.get()
                        xadd=c.get()
                        xph=d.get()
                        xem=e.get()
                        sql="update customer set name='%s',address='%s',phone='%s',email='%s' where custid=('%s')"%(xnm,xadd,xph,xem,xid)
                        cur.execute(sql)
                        db.commit()
                        messagebox.showinfo('Hi','Update Done')
                        db.close()
                        a.delete(0,100)
                        b.delete(0,100)
                        c.delete(0,100)
                        d.delete(0,100)
                        e.delete(0,100)
                        c3.destroy()
                        scr()
                def closed():
                    c3.destroy()
                    scr()
                
                idI=Label(c3,text='Customer id',font=('arial',15),bg='lavender')
                idI.place(x=50,y=30)
                a=ttk.Combobox(c3,width=20)
                filldata()
                a['values']=lt
                a.place(x=400,y=30)
                bt=Button(c3,text='Find',command=finddata,bg='blue',font=('arial',15))
                bt.place(x=100,y=70)
                name=Label(c3,text='Customer name',font=('arial',15),bg='lavender')
                name.place(x=50,y=110)
                b=Entry(c3,width=40)
                b.place(x=400,y=110)
                add=Label(c3,text='Address',font=('arial',15),bg='lavender')
                add.place(x=50,y=150)
                c=Entry(c3,width=40)
                c.place(x=400,y=150)
                ph=Label(c3,text='Phone number',font=('arial',15),bg='lavender')
                ph.place(x=50,y=190)
                d=Entry(c3,width=40)
                d.place(x=400,y=190)
                em=Label(c3,text='Email id',font=('arial',15),bg='lavender')
                em.place(x=50,y=230)
                e=Entry(c3,width=40)
                e.place(x=400,y=230)
                btt=Button(c3,text='Update',command=updatedata,bg='green',font=('arial',15))
                btt.place(x=300,y=270)
                cl=Button(c3,text='Close',command=closed,bg='red',font=('arial',15))
                cl.place(x=400,y=270)
                
            b28=Button(c2,text='Update',bg='white',fg='purple',font=('arial',14),command=cusupdatebt)
            b28.place(x=10,y=160)
            scr()

        def orde():
            c2=Canvas(SC,height=1160,width=180,bg='violet')
            c2.place(x=180,y=0)
            z=Label(c2,text='  ORDERS  ',bg='purple',fg='white',font=('arial',21))
            z.place(x=3,y=3)
            def ordsavebt():
                c3=Canvas(SC,height=1160,width=800,bg='lavender')
                c3.place(x=360,y=0)
                def savedata():
                    if len(A.get())==0 or len(B.get())==0 or len(C.get())==0 or len(D.get())==0 or len(E.get())==0 or len(H.get())==0 :
                        messagebox.showerror('ERROR','ENTER VAILD DATA')
                    else:
                        db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                        cur=db.cursor()
                        xa=A.get()
                        xb=B.get()
                        xc=C.get()
                        xd=D.get()
                        xe=int(E.get())
                        xh=H.get()
                        sql="insert into orders values('%s','%s','%s','%s',%d,'%s')"%(xa,xb,xc,xd,xe,xh)
                        cur.execute(sql)
                        db.commit()
                        messagebox.showinfo('Screen','SAVED')
                        db.close()
                        A.delete(0,100)
                        B.delete(0,100)
                        C.delete(0,100)
                        D.delete(0,100)
                        E.delete(0,100)
                        H.delete(0,100)
                        c3.destroy()
                        scr()
                def closebt():
                    c3.destroy()
                    scr()
            
                a=Label(c3,text='ORDER ID',font=('arial',15),bg='lavender')
                a.place(x=50,y=50)
                A=Entry(c3,width=50)
                A.place(x=600,y=50)
                b=Label(c3,text='CUSTOMER ID',font=('arial',15),bg='lavender')
                b.place(x=50,y=120)
                B=Entry(c3,width=50)
                B.place(x=600,y=120)
                c=Label(c3,text='CATEGORY ID',font=('arial',15),bg='lavender')
                c.place(x=50,y=190)
                C=Entry(c3,width=50)
                C.place(x=600,y=190)
                d=Label(c3,text='PRODUCT ID',font=('arial',15),bg='lavender')
                d.place(x=50,y=260)
                D=Entry(c3,width=50)
                D.place(x=600,y=260)
                e=Label(c3,text='QUANTITY',font=('arial',15),bg='lavender')
                e.place(x=50,y=340)
                E=Entry(c3,width=50)
                E.place(x=600,y=340)
                h=Label(c3,text='DATE OF ORDER',font=('arial',15),bg='lavender')
                h.place(x=50,y=410)
                H=Entry(c3,width=50)
                H.place(x=600,y=410)
                b1=Button(c3,text='SAVE',command=savedata,bg='green',font=('arial',15))
                b1.place(x=430,y=500)
                bt=Button(c3,text='CLOSE',command=closebt,bg='red',font=('arial',15))
                bt.place(x=500,y=500)
            
            b31=Button(c2,text='Insert',bg='white',fg='purple',font=('arial',14),command=ordsavebt)
            b31.place(x=10,y=60)
            scr()
            def ordfindbt():
                lt=[]
                c3=Canvas(SC,height=1160,width=800,bg='lavender')
                c3.place(x=360,y=0)
                def filldata():
                    db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                    cur=db.cursor()
                    sql="select orderid from orders"
                    cur.execute(sql)
                    data=cur.fetchall()
                    for res in data:
                        lt.append(res[0])
                    db.close()   
                def finddata():
                    db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                    cur=db.cursor()
                    xa=d.get()
                    sql="select custid,catid,prodid,qty,date_of_order from orders where orderid='%s'"%(xa)
                    cur.execute(sql)
                    data=cur.fetchone()
                    f.delete(0,100)
                    h.delete(0,100)
                    k.delete(0,100)
                    u.delete(0,100)
                    r.delete(0,100)
                    f.insert(0,data[0])
                    h.insert(0,data[1])
                    k.insert(0,data[2])
                    r.insert(0,data[3])
                    u.insert(0,data[4])
                    db.close()
                def closebt():
                    c3.destroy()
                    scr()
                a=Label(c3,text='ORDER ID',font=('arial',15),bg='lavender')
                a.place(x=50,y=70)
                d=Entry(c3,width=40)
                d=ttk.Combobox(c3,width=40)
                filldata()
                d['values']=lt
                d.place(x=500,y=70)
                bt=Button(c3,text='FIND',command=finddata,bg='blue',font=('arial',15))
                bt.place(x=400,y=110)
                e=Label(c3,text='CUSTOMER ID',font=('arial',15),bg='lavender')
                e.place(x=50,y=150)
                f=Entry(c3,width=40)
                f.place(x=500,y=150)
                g=Label(c3,text='CATEGORY ID',font=('arial',15),bg='lavender')
                g.place(x=50,y=190)
                h=Entry(c3,width=40)
                h.place(x=500,y=190)
                j=Label(c3,text='PRODUCT ID',font=('arial',15),bg='lavender')
                j.place(x=50,y=230)
                k=Entry(c3,width=40)
                k.place(x=500,y=230)
                p=Label(c3,text='DATE OF ORDER',font=('arial',15),bg='lavender')
                p.place(x=50,y=270)
                u=Entry(c3,width=40)
                u.place(x=500,y=270)
                v=Label(c3,text='QUANTITY',font=('arial',15),bg='lavender')
                v.place(x=50,y=310)
                r=Entry(c3,width=40)
                r.place(x=500,y=310)
                bt=Button(c3,text='CLOSE',command=closebt,bg='red',font=('arial',15))
                bt.place(x=400,y=450)
                def orddata():
                    B1=[]
                    B2=[]
                    B3=[]
                    B4=[]
                    B5=[]
                    B6=[]
                    i=0
                    c3=Canvas(SC,height=1160,width=800,bg='lavender')
                    c3.place(x=360,y=0)
                    def filldata():
                        db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                        cur=db.cursor()
                        sql="select * from orders"
                        cur.execute(sql)
                        data=cur.fetchall()
                        for res in data:
                            B1.append(res[0])
                            B2.append(res[1])
                            B3.append(res[2])
                            B4.append(res[3])
                            B5.append(res[4])
                            B6.append(res[5])
                        db.close()
                    def firstdata():
                        global i
                        i=0
                        A1.config(text='')
                        A2.config(text='')
                        A3.config(text='')
                        A4.config(text='')
                        A5.config(text='')
                        A6.config(text='')
                
                        A1.config(text=B1[i])
                        A2.config(text=B2[i])
                        A3.config(text=B3[i])
                        A4.config(text=B4[i])
                        A5.config(text=B5[i])
                        A6.config(text=B6[i])
                        
                    def nextdata():
                        global i
                        if i<len(B1)-1:
                            i=i+1
                            A1.config(text='')
                            A2.config(text='')
                            A3.config(text='')
                            A4.config(text='')
                            A5.config(text='')
                            A6.config(text='')
                
                            A1.config(text=B1[i])
                            A2.config(text=B2[i])
                            A3.config(text=B3[i])
                            A4.config(text=B4[i])
                            A5.config(text=B5[i])
                            A6.config(text=B6[i])
                            
                
                        else:
                            messagebox.showinfo('Screen',"last record")
                    def lastdata():
                        global i
                        i=len(B1)-1
                        A1.config(text='')
                        A2.config(text='')
                        A3.config(text='')
                        A4.config(text='')
                        A5.config(text='')
                        A6.config(text='')
                
                        A1.config(text=B1[i])
                        A2.config(text=B2[i])
                        A3.config(text=B3[i])
                        A4.config(text=B4[i])
                        A5.config(text=B5[i])
                        A6.config(text=B6[i])
                        
                    def prevdata():
                        global i
                        if i>0:
                            i=i-1
                            A1.config(text='')
                            A2.config(text='')
                            A3.config(text='')
                            A4.config(text='')
                            A5.config(text='')
                            A6.config(text='')
                
                            A1.config(text=B1[i])
                            A2.config(text=B2[i])
                            A3.config(text=B3[i])
                            A4.config(text=B4[i])
                            A5.config(text=B5[i])
                            A6.config(text=B6[i])
                            
                        else:
                            messagebox.showinfo('Screen',"Already done")
                    def exitdata():
                        c3.destroy()
                        scr()
                    
                    A=Label(c3,text='ORDER ID',font=('arial',15),bg='lavender')
                    A.place(x=50,y=40)
                    A1=Label(c3,width=35)
                    A1.place(x=390,y=40)
                    B=Label(c3,text='CUSTOMER ID',font=('arial',15),bg='lavender')
                    B.place(x=50,y=110)
                    A2=Label(c3,width=35)
                    A2.place(x=390,y=110)
                    C=Label(c3,text='CATEGORY ID',font=('arial',15),bg='lavender')
                    C.place(x=50,y=170)
                    A3=Label(c3,width=35)
                    A3.place(x=390,y=170)
                    D=Label(c3,text='PRODUCT ID',font=('arial',15),bg='lavender')
                    D.place(x=50,y=230)
                    A4=Label(c3,width=35)
                    A4.place(x=390,y=230)
                    E=Label(c3,text='QUANTITY',font=('arial',15),bg='lavender')
                    E.place(x=50,y=290)
                    A5=Label(c3,width=35)
                    A5.place(x=390,y=290)
                    F=Label(c3,text='DATE OF ORDER',font=('arial',15),bg='lavender')
                    F.place(x=50,y=350)
                    A6=Label(c3,width=35)
                    A6.place(x=390,y=350)
                    BT1=Button(c3,text='FIRST',command=firstdata,bg='orange',font=('arial',15))
                    BT1.place(x=50,y=455)
                    BT2=Button(c3,text='NEXT',command=nextdata,bg='pink',font=('arial',15))
                    BT2.place(x=200,y=455)
                    BT3=Button(c3,text='LAST',command=lastdata,bg='green',font=('arial',15))
                    BT3.place(x=350,y=455)
                    BT4=Button(c3,text='PREVIOUS',command=prevdata,bg='blue',font=('arial',15))
                    BT4.place(x=500,y=455)
                    BT5=Button(c3,text='CLOSE',command=exitdata,bg='red',font=('arial',15))
                    BT5.place(x=650,y=455)
                    filldata()
                    
                b35=Button(c3,text='Records',bg='white',fg='purple',font=('arial',15),command=orddata)
                b35.place(x=600,y=450)
                scr()
            
            b32=Button(c2,text='Find',bg='white',fg='purple',font=('arial',14),command=ordfindbt)
            b32.place(x=10,y=110)
            scr()
            def orddeletebt():
                lt=[]
                c3=Canvas(SC,height=1160,width=800,bg='lavender')
                c3.place(x=360,y=0)
                def filldata():
                    db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                    cur=db.cursor()
                    sql="select orderid from orders"
                    cur.execute(sql)
                    data=cur.fetchall()
                    for res in data:
                        lt.append(res[0])
                    db.close()
                def deletedata():
                    db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                    cur=db.cursor()
                    xa=d.get()
                    sql="delete from orders where orderid='%s'"%(xa)
                    cur.execute(sql)
                    db.commit()
                    messagebox.showinfo('Screen','Deleted')
                    d.delete(0,100)
                    c3.destroy()
                    scr()
                def closebt():
                    c3.destroy()
                    scr()
                
                a=Label(c3,text=' ORDER ID',font=('arial',15),bg='lavender')
                a.place(x=200,y=70)
                d=Entry(c3,width=10)
                d=ttk.Combobox(c3,width=40)
                filldata()
                d['values']=lt
                d.place(x=500,y=70)
                bt=Button(c3,text='DELETE',command=deletedata,bg='blue',font=('arial',15))
                bt.place(x=400,y=110)
                bt=Button(c3,text='CLOSE',command=closebt,bg='red',font=('arial',15))
                bt.place(x=400,y=160)
                
            b34=Button(c2,text='Delete',bg='white',fg='purple',font=('arial',14),command=orddeletebt)
            b34.place(x=10,y=210)
            scr()
            

            def ordupdatebt():
                lt=[]
                c3=Canvas(SC,height=1160,width=800,bg='lavender')
                c3.place(x=360,y=0)
                def filldata():
                    db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                    cur=db.cursor()
                    sql="select orderid from orders"
                    cur.execute(sql)
                    data=cur.fetchall()
                    for res in data:
                        lt.append(res[0])
                    db.close()   
                def finddata():
                    db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                    cur=db.cursor()
                    xa=d.get()
                    sql="select custid,catid,prodid,qty,date_of_order from orders where orderid='%s'"%(xa)
                    cur.execute(sql)
                    data=cur.fetchone()
                    f.delete(0,100)
                    h.delete(0,100)
                    k.delete(0,100)
                    u.delete(0,100)
                    r.delete(0,100)
                    f.insert(0,data[0])
                    h.insert(0,data[1])
                    k.insert(0,data[2])
                    r.insert(0,data[3])
                    u.insert(0,data[4])
                    db.close()
                    
                def updatedata():
                    if len(d.get())==0 or len(f.get())==0 or len(h.get())==0 or len(k.get())==0 or len(u.get())==0 or len(r.get())==0 :
                        messagebox.showerror('ERROR','ENTER VAILD DATA')
                    db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                    cur=db.cursor()
                    xa=d.get()
                    xb=f.get()
                    xc=h.get()
                    xd=k.get()
                    xe=u.get()
                    xh=int(r.get())
                    sql="update orders set custid='%s',catid='%s',prodid='%s',qty=%d,date_of_order='%s' where orderid='%s'"%(xb,xc,xd,xh,xe,xa)
                    cur.execute(sql)
                    db.commit()
                    messagebox.showinfo('Screen','Updated')
                    db.close()
                    d.delete(0,100)
                    f.delete(0,100)
                    h.delete(0,100)
                    k.delete(0,100)
                    u.delete(0,100)
                    r.delete(0,100)
                    c3.destroy()
                    scr()
                def closebt():
                    c3.destroy()
                    scr()
                
                a=Label(c3,text='ORDER ID',font=('arial',15),bg='lavender')
                a.place(x=50,y=70)
                d=Entry(c3,width=40)
                d=ttk.Combobox(c3,width=40)
                filldata()
                d['values']=lt
                d.place(x=500,y=70)
                bt=Button(c3,text='FIND',command=finddata,bg='blue',font=('arial',15))
                bt.place(x=400,y=110)
                e=Label(c3,text='CUSTOMER ID',font=('arial',15),bg='lavender')
                e.place(x=50,y=150)
                f=Entry(c3,width=40)
                f.place(x=500,y=150)
                g=Label(c3,text='CATEGORY ID',font=('arial',15),bg='lavender')
                g.place(x=50,y=190)
                h=Entry(c3,width=40)
                h.place(x=500,y=190)
                j=Label(c3,text='PRODUCT ID',font=('arial',15),bg='lavender')
                j.place(x=50,y=230)
                k=Entry(c3,width=40)
                k.place(x=500,y=230)
                p=Label(c3,text='DATE OF ORDER',font=('arial',15),bg='lavender')
                p.place(x=50,y=270)
                u=Entry(c3,width=40)
                u.place(x=500,y=270)
                v=Label(c3,text='QUANTITY',font=('arial',15),bg='lavender')
                v.place(x=50,y=310)
                r=Entry(c3,width=40)
                r.place(x=500,y=310)
                btt=Button(c3,text='UPDATE',command=updatedata,bg='green',font=('arial',15))
                btt.place(x=300,y=450)
                bt=Button(c3,text='CLOSE',command=closebt,bg='red',font=('arial',15))
                bt.place(x=400,y=450)
                
            b33=Button(c2,text='Update',bg='white',fg='purple',font=('arial',14),command=ordupdatebt)
            b33.place(x=10,y=160)
            scr()
            
            
            def ordcographdatabt():
                
                def ordcharts():
                    deleteimg()
                    if int(q.get())==0:
                        
                        def ordlinegraphdata():
                            
                            deleteimg()
                            db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                            cur=db.cursor()
                            a=[]
                            b=[]
                            sql="select orderid, qty  from orders"
                            cur.execute(sql)
                            dt=cur.fetchall()
                            for i in dt:
                                a.append(i[0])
                                b.append(i[1])
                                
                            plt.plot(b,a)
                            plt.savefig('console_image.png')
                            plt.show()
                           
                            image = Image.open('console_image.png')
                            image.paste(image)
                            image.show()
                            scr()
                            
                        deleteimg()
                        ordlinegraphdata() 
                        
                        
                        
                    elif int(q.get())==1:
                                        
                        def ordbargraphdata():
                            
                            db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                            cur=db.cursor()
                            c=[]
                            d=[]
                            sql="select orderid, qty  from orders"
                            cur.execute(sql)
                            df=cur.fetchall()
                            for i in df:
                                c.append(i[0])
                                d.append(i[1])
                                
                            plt.bar(d,c)
                            plt.savefig('console_image1.png')
                            plt.show()
                            
                            image1 = Image.open('console_image1.png')
                            image1.paste(image1)
                            image1.show()
                            scr()
            
                        deleteimg()
                        ordbargraphdata()
                        
                    elif int(q.get())==2:
                                        
                        def orddbargraphdata():
                            
                            db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                            cur=db.cursor()
                            c=[]
                            d=[]
                            sql="select orderid, date_of_order from orders"
                            cur.execute(sql)
                            df=cur.fetchall()
                            for i in df:
                                c.append(i[0])
                                d.append(i[1])
                                
                            plt.bar(d,c)
                            plt.savefig('console_image1.png')
                            plt.show()
                            
                            image1 = Image.open('console_image1.png')
                            image1.paste(image1)
                            image1.show()
                            scr()
            
                        deleteimg()
                        orddbargraphdata()
                    
                    
                    elif int(q.get())==3:
                                        
                        def orrdbargraphdata():
                            
                            db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                            cur=db.cursor()
                            c=[]
                            d=[]
                            sql="select orderid, date_of_order  from orders"
                            cur.execute(sql)
                            df=cur.fetchall()
                            for i in df:
                                c.append(i[0])
                                d.append(i[1])
                                
                            plt.bar(d,c)
                            plt.savefig('console_image1.png')
                            plt.show()
                            
                            image1 = Image.open('console_image1.png')
                            image1.paste(image1)
                            image1.show()
                            scr()
            
                        deleteimg()
                        orrdbargraphdata()
                        
                    elif int(q.get())==4:
                                        
                        def oorrdbargraphdata():
                            
                            db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                            cur=db.cursor()
                            c=[]
                            d=[]
                            sql="select qty, date_of_order  from orders"
                            cur.execute(sql)
                            df=cur.fetchall()
                            for i in df:
                                c.append(i[0])
                                d.append(i[1])
                                
                            plt.bar(d,c)
                            plt.savefig('console_image1.png')
                            plt.show()
                            
                            image1 = Image.open('console_image1.png')
                            image1.paste(image1)
                            image1.show()
                            scr()
            
                        deleteimg()
                        oorrdbargraphdata()
                    
                    elif int(q.get())==3:
                                        
                        def orrdbbargraphdata():
                            
                            db=pymysql.connect(host='localhost',user='root',password='root',database='stockmgm')
                            cur=db.cursor()
                            c=[]
                            d=[]
                            sql="select qty, date_of_order  from orders"
                            cur.execute(sql)
                            df=cur.fetchall()
                            for i in df:
                                c.append(i[0])
                                d.append(i[1])
                                
                            plt.bar(d,c)
                            plt.savefig('console_image1.png')
                            plt.show()
                            
                            image1 = Image.open('console_image1.png')
                            image1.paste(image1)
                            image1.show()
                            scr()
            
                        deleteimg()
                        orrdbbargraphdata()
                        
                        
                
                c3=Canvas(SC,height=1160,width=800,bg='lavender')
                c3.place(x=360,y=0)
                q=IntVar()
                
                r5=Radiobutton(c3,text=' LINE CHART (date of order and qty)',variable=q,value=4,font=('arial',15),bg='lavender')
                r6=Radiobutton(c3,text='BAR CHART (date of order and qty)',variable=q,value=5,font=('arial',15),bg='lavender')
                
                r5.place(x=20,y=170)
                r6.place(x=400,y=170)
                
                r1=Radiobutton(c3,text=' LINE CHART (orderid and qty)',variable=q,value=0,font=('arial',15),bg='lavender')
                r2=Radiobutton(c3,text='BAR CHART (orderid and qty)',variable=q,value=1,font=('arial',15),bg='lavender')
                
                r1.place(x=20,y=270)
                r2.place(x=400,y=270)
                
                r3=Radiobutton(c3,text=' LINE CHART (orderid and date of order)',variable=q,value=2,font=('arial',15),bg='lavender')
                r4=Radiobutton(c3,text='BAR CHART (orderid and date of order)',variable=q,value=3,font=('arial',15),bg='lavender')
                
                r3.place(x=20,y=370)
                r4.place(x=400,y=370)
                
                deleteimg()
                bttt1=Button(c3,text='CREATE',command=ordcharts,font=('arial',15),bg='violet')
                bttt1.place(x=350,y=500)
                
            deleteimg()
            b101=Button(c2,text='Graph',bg='white',fg='purple',font=('arial',14),command=ordcographdatabt)
            b101.place(x=10,y=260)
            scr()

        c1=Canvas(SC,height=1160,width=180,bg='purple')
        c1.place(x=0,y=0)
        c2=Canvas(SC,height=1160,width=180,bg='violet')
        c2.place(x=180,y=0)
        c3=Canvas(SC,height=1160,width=800,bg='lavender')
        c3.place(x=360,y=0)

        scr()

        q=Label(c1,text='    PANEL    ',bg='pink',fg='purple',font=('arial',23))
        q.place(x=2,y=2)

        bt1=Button(c1,text='COMPANY ',bg='white',fg='purple',font=('arial',16),command=com)
        bt1.place(x=10,y=60)

        bt2=Button(c1,text='CATEGORY',bg='white',fg='purple',font=('arial',16),command=cat)
        bt2.place(x=10,y=110)

        bt3=Button(c1,text='PRODUCT ',bg='white',fg='purple',font=('arial',16),command=pro)
        bt3.place(x=10,y=160)

        bt4=Button(c1,text='SUPPLIERS',bg='white',fg='purple',font=('arial',16),command=sup)
        bt4.place(x=10,y=210)

        bt5=Button(c1,text=' STOCK  ',bg='white',fg='purple',font=('arial',16),command=stk)
        bt5.place(x=10,y=260)

        bt6=Button(c1,text='CUSTOMER',bg='white',fg='purple',font=('arial',16),command=cus)
        bt6.place(x=10,y=310)

        bt7=Button(c1,text='ORDERS ',bg='white',fg='purple',font=('arial',16),command=orde)
        bt7.place(x=10,y=360)

        SC.mainloop()
        
    else:
        messagebox.showerror('LOGIN','Enter vaild id and password')
        
SCM=tkinter.Tk()
SCM.geometry('1160x1160')
SCM.title('STOCK MAGANGEMENT')
SCM.maxsize(1160,1160)
SCM.configure(bg='purple')

global em1,em2

lm1=Label(SCM, text='LOGIN AUTHENTICATION', bg='white',fg='purple',font=('arial',23))
lm1.place(x=400,y=50)

lm2=Label(SCM, text='USERNAME', bg='purple',fg='white',font=('Areal', 20))
lm2.place(x=310,y=190)

lm3=Label(SCM, text='PASSWORD', bg='purple',fg='white',font=('Areal', 20))
lm3.place(x=310,y=340)

em1=Entry(SCM, font=('Areal', 14))
em1.place(x=600,y=200)

em2=Entry(SCM, font=('Areal', 14),show='*')
em2.place(x=600,y=350)

bum1=Button(SCM, text="LOGIN", bg='pink',font=('Areal', 14),bd=5 ,command=autherization)
bum1.place(x=500,y=500)


SCM.mainloop()
