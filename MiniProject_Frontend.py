#Frontend

from tkinter import *
import tkinter.messagebox
import MiniProject_Backend

class Movie:
	def __init__(self, root):
		self.root=root
		self.root.title("Online Stocks Details System")
		self.root.geometry("1350x750+0+0")
		self.root.config(bg="black")

		stock_Name=StringVar()
		stock_ID=StringVar()
		stock_Date=StringVar()
		seller=StringVar()
		buyer=StringVar()
		price=StringVar()
		quantity=StringVar()
		perstockprice=StringVar()

		#Fuctions
		def iExit():
			iExit=tkinter.messagebox.askyesno("Online Stocks Details System", "Are you sure???")
			if iExit>0:
				root.destroy()
			return

		def clcdata():
			self.txtstock_ID.delete(0,END)
			self.txtstock_Name.delete(0,END)
			self.txtstock_Date.delete(0,END)
			self.txtseller.delete(0,END)
			self.txtbuyer.delete(0,END)
			self.txtprice.delete(0,END)
			self.txtquantity.delete(0,END)
			self.txtperstockprice.delete(0,END)

		def adddata():
			if(len(stock_ID.get())!=0):
				MiniProject_Backend.AddMovieRec(stock_ID.get(),stock_Name.get(),stock_Date.get(),seller.get(),buyer.get(),price.get(),quantity.get(),perstockprice.get())
				MovieList.delete(0,END)
				MovieList.insert(END,(stock_ID.get(),stock_Name.get(),stock_Date.get(),seller.get(),buyer.get(),price.get(),quantity.get(),perstockprice.get()))

		def disdata():
			MovieList.delete(0,END)
			for row in MiniProject_Backend.ViewMovieData():
				MovieList.insert(END, row, str(""))

		def movierec(event):
			global sd
			searchmovie=MovieList.curselection()[0]
			sd=MovieList.get(searchmovie)

			self.txtstock_ID.delete(0,END)
			self.txtstock_ID.insert(END,sd[1])
			self.txtstock_Name.delete(0,END)
			self.txtstock_Name.insert(END,sd[2])
			self.txtstock_Date.delete(0,END)
			self.txtstock_Date.insert(END,sd[3])
			self.txtseller.delete(0,END)
			self.txtseller.insert(END,sd[4])
			self.txtbuyer.delete(0,END)
			self.txtbuyer.insert(END,sd[5])
			self.txtprice.delete(0,END)
			self.txtprice.insert(END,sd[6])
			self.txtquantity.delete(0,END)
			self.txtquantity.insert(END,sd[7])
			self.txtperstockprice.delete(0,END)
			self.txtperstockprice.insert(END,sd[8])

		def deldata():
			if(len(stock_ID.get())!=0):
				MiniProject_Backend.DeleteMovieRec(sd[1])
				clcdata()
				disdata()

		def searchdb():
			MovieList.delete(0,END)
			for row in MiniProject_Backend.SearchMovieData(stock_ID.get(),stock_Name.get(),stock_Date.get(),seller.get(),buyer.get(),price.get(),quantity.get(),perstockprice.get()):
				MovieList.insert(END, row, str(""))

		def updata():
			if(len(stock_ID.get())!=0):
				MiniProject_Backend.DeleteMovieRec(sd[1])
			if(len(stock_ID.get())!=0):
				MiniProject_Backend.AddMovieRec(stock_ID.get(),stock_Name.get(),stock_Date.get(),seller.get(),buyer.get(),price.get(),quantity.get(),perstockprice.get())
				MovieList.delete(0,END)
				MovieList.insert(END,(stock_ID.get(),stock_Name.get(),stock_Date.get(),seller.get(),buyer.get(),price.get(),quantity.get(),perstockprice.get()))

		#Frames
		MainFrame=Frame(self.root, bg="black")
		MainFrame.grid()

		TFrame=Frame(MainFrame, bd=5, padx=54, pady=8, bg="black", relief=RIDGE)
		TFrame.pack(side=TOP)

		self.TFrame=Label(TFrame, font=('Arial', 45, 'bold'), text="ONLINE STOCK DETAILS SYSTEM", bg="black", fg="orange")
		self.TFrame.grid() 

		BFrame=Frame(MainFrame, bd=2, width=1350, height=70, padx=18, pady=10, bg="black", relief=RIDGE)
		BFrame.pack(side=BOTTOM)

		DFrame=Frame(MainFrame, bd=2, width=1300, height=400, padx=20, pady=20, bg="black", relief=RIDGE)
		DFrame.pack(side=BOTTOM)

		DFrameL=LabelFrame(DFrame, bd=2, width=1000, height=600, padx=20, bg="black", relief=RIDGE, font=('Arial', 20, 'bold'), text="Stock Info_\n", fg="white")
		DFrameL.pack(side=LEFT)

		DFrameR=LabelFrame(DFrame, bd=2, width=450, height=300, padx=31, pady=3, bg="black", relief=RIDGE, font=('Arial', 20, 'bold'), text="Stocks List_\n", fg="white")
		DFrameR.pack(side=RIGHT)

		#Labels & Entry Box

		self.lblstock_ID=Label(DFrameL, font=('Arial', 18, 'bold'), text="Stock ID:", padx=2, pady=2, bg="black", fg="orange")
		self.lblstock_ID.grid(row=0, column=0, sticky=W)
		self.txtstock_ID=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=stock_ID, width=39, bg="black", fg="white")
		self.txtstock_ID.grid(row=0, column=1) 

		self.lblstock_Name=Label(DFrameL, font=('Arial', 18, 'bold'), text="Stock Name:", padx=2, pady=2, bg="black", fg="orange")
		self.lblstock_Name.grid(row=1, column=0, sticky=W) 
		self.txtstock_Name=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=stock_Name, width=39, bg="black", fg="white")
		self.txtstock_Name.grid(row=1, column=1)

		self.lblstock_Date=Label(DFrameL, font=('Arial', 18, 'bold'), text="Transaction Date:", padx=2, pady=2, bg="black", fg="orange")
		self.lblstock_Date.grid(row=2, column=0, sticky=W) 
		self.txtstock_Date=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=stock_Date, width=39, bg="black", fg="white")
		self.txtstock_Date.grid(row=2, column=1)

		self.lblseller=Label(DFrameL, font=('Arial', 18, 'bold'), text="Seller:", padx=2, pady=2, bg="black", fg="orange")
		self.lblseller.grid(row=3, column=0, sticky=W) 
		self.txtseller=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=seller, width=39, bg="black", fg="white")
		self.txtseller.grid(row=3, column=1)

		self.lblbuyer=Label(DFrameL, font=('Arial', 18, 'bold'), text="Buyer:", padx=2, pady=2, bg="black", fg="orange")
		self.lblbuyer.grid(row=4, column=0, sticky=W) 
		self.txtbuyer=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=buyer, width=39, bg="black", fg="white")
		self.txtbuyer.grid(row=4, column=1)

		self.lblprice=Label(DFrameL, font=('Arial', 18, 'bold'), text="Amount:", padx=2, pady=2, bg="black", fg="orange")
		self.lblprice.grid(row=5, column=0, sticky=W) 
		self.txtprice=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=price, width=39, bg="black", fg="white")
		self.txtprice.grid(row=5, column=1)

		self.lblquantity=Label(DFrameL, font=('Arial', 18, 'bold'), text="Quantity:", padx=2, pady=2, bg="black", fg="orange")
		self.lblquantity.grid(row=6, column=0, sticky=W) 
		self.txtquantity=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=quantity, width=39, bg="black", fg="white")
		self.txtquantity.grid(row=6, column=1)

		self.lblperstockprice=Label(DFrameL, font=('Arial', 18, 'bold'), text="Per Stock Price:", padx=2, pady=2, bg="black", fg="orange")
		self.lblperstockprice.grid(row=7, column=0, sticky=W) 
		self.txtperstockprice=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=perstockprice, width=39, bg="black", fg="white")
		self.txtperstockprice.grid(row=7, column=1)

		#ListBox & ScrollBar
		sb=Scrollbar(DFrameR)
		sb.grid(row=0, column=1, sticky='ns')

		MovieList=Listbox(DFrameR, width=41, height=16, font=('Arial', 12, 'bold'), bg="black", fg="white", yscrollcommand=sb.set)
		MovieList.bind('<<ListboxSelect>>', movierec)
		MovieList.grid(row=0, column=0, padx=8)
		sb.config(command=MovieList.yview)

		#Buttons
		self.btnadd=Button(BFrame, text="Add New", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="orange", command=adddata)
		self.btnadd.grid(row=0, column=0)

		self.btndis=Button(BFrame, text="Display", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="orange", command=disdata)
		self.btndis.grid(row=0, column=1)

		self.btnclc=Button(BFrame, text="Clear", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="orange", command=clcdata)
		self.btnclc.grid(row=0, column=2)

		self.btnse=Button(BFrame, text="Search", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="orange", command=searchdb)
		self.btnse.grid(row=0, column=3)

		self.btndel=Button(BFrame, text="Delete", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="orange", command=deldata)
		self.btndel.grid(row=0, column=4)

		self.btnup=Button(BFrame, text="Update", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="orange", command=updata)
		self.btnup.grid(row=0, column=5)

		self.btnx=Button(BFrame, text="Exit", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="orange", command=iExit)
		self.btnx.grid(row=0, column=6)


if __name__=='__main__':
	root=Tk()
	datbase=Movie(root)
	root.mainloop()
