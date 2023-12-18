from tkinter import *

def clear_all():
    pawanbuy_field.delete(0,END)
    price_field1.delete(0,END)
    gram_field1.delete(0,END)

    pawan_field1.delete(0,END)
    price_field2.delete(0,END) 
    gram_field2.delete(0,END) 
    pawan_field2.delete(0,END
                        )
    price_field3.delete(0,END)
    gram_field3.delete(0,END)
    pawan_field3.delete(0,END)

    pawanbuy_field.focus_set()

def calculate():
    pawan_buy=int(pawanbuy_field.get())

    pawan1=46280
    price1=int(pawan_buy*pawan1)
    one_gram1=int(pawan1/8)
    gram_field1.insert(10,one_gram1)
    price_field1.insert(10,price1)
    pawan_field1.insert(10,pawan1)
    
    pawan2=50488
    price2=int(pawan_buy*pawan2)
    one_gram2=int(pawan2/8)
    gram_field2.insert(10,one_gram2)
    price_field2.insert(10,price2)
    pawan_field2.insert(10,pawan2)

    pawan3=37912
    price3=int(pawan_buy*pawan3)
    one_gram3=int(pawan3/8)
    gram_field3.insert(10,one_gram3)
    price_field3.insert(10,price3)
    pawan_field3.insert(10,pawan3)

if __name__=="__main__":
    window=Tk()
    window.configure(background='light blue')
    window.geometry("380x500")
    window.title("Gold Rate Calculator")
    
    lbl1=Label(window,text='How Much Gold You Buy (Pawan):',fg='black',bg='violet')
    
    lbl2=Label(window,text='22K Gold Price (Rs):',fg='black',bg='orange')
    lbl3=Label(window,text='22K 1Gram Gold Price (Rs):',fg='black',bg='orange')
    lbl4=Label(window,text='22K Pawan Gold Price (Rs):',fg='black',bg='orange')
    
    lbl5=Label(window,text='24K Gold Price (Rs):',fg='black',bg='grey')
    lbl6=Label(window,text='24K 1Gram Gold Price (Rs):',fg='black',bg='grey')
    lbl7=Label(window,text='24K Pawan Gold Price (Rs):',fg='black',bg='grey')

    lbl8=Label(window,text='18K Gold Price (Rs):',fg='black',bg='light green')
    lbl9=Label(window,text='18K 1Gram Gold Price (Rs):',fg='black',bg='light green')
    lbl10=Label(window,text='18K Pawan Gold Price (Rs):',fg='black',bg='light green')
    
    lbl1.grid(row=1,column=0,padx=10,pady=10)
    
    lbl2.grid(row=3,column=0,padx=10,pady=10)
    lbl3.grid(row=4,column=0,padx=10,pady=10)
    lbl4.grid(row=5,column=0,padx=10,pady=10)
    
    lbl5.grid(row=6,column=0,padx=10,pady=10)
    lbl6.grid(row=7,column=0,padx=10,pady=10)
    lbl7.grid(row=8,column=0,padx=10,pady=10)
    
    lbl8.grid(row=9,column=0,padx=10,pady=10)
    lbl9.grid(row=10,column=0,padx=10,pady=10)
    lbl10.grid(row=11,column=0,padx=10,pady=10)
    
    pawanbuy_field=Entry(window)
    
    price_field1=Entry(window)
    gram_field1=Entry(window)
    pawan_field1=Entry(window)
    
    price_field2=Entry(window)
    gram_field2=Entry(window)
    pawan_field2=Entry(window)
    
    price_field3=Entry(window)
    gram_field3=Entry(window)
    pawan_field3=Entry(window)
    
    pawanbuy_field.grid(row=1,column=1,padx=10,pady=10)
    
    price_field1.grid(row=3,column=1,padx=10,pady=10)
    gram_field1.grid(row=4,column=1,padx=10,pady=10)
    pawan_field1.grid(row=5,column=1,padx=10,pady=10)
    
    price_field2.grid(row=6,column=1,padx=10,pady=10)
    gram_field2.grid(row=7,column=1,padx=10,pady=10)
    pawan_field2.grid(row=8,column=1,padx=10,pady=10)
    
    price_field3.grid(row=9,column=1,padx=10,pady=10)
    gram_field3.grid(row=10,column=1,padx=10,pady=10)
    pawan_field3.grid(row=11,column=1,padx=10,pady=10)
    
    btn1=Button(window,text='Calculate',fg='black',bg='gold',command=calculate)
    btn2=Button(window,text='Clear All',fg='black',bg='gold',command=clear_all)
    
    btn1.grid(row=2,column=1,pady=10)
    btn2.grid(row=12,column=1,pady=10)
    
    window.mainloop()