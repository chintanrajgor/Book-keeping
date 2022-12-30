#backend
import mysql.connector as sql
def MovieData():
    con=sql.connect(host='127.0.0.1', user='root', password='', database='stocks')
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, stock_ID text,stock_Name text,stock_Date text,seller text,buyer text,price text,quantity text,perstockprice text)")
    con.commit()
    con.close()
    
def AddMovieRec(stock_ID,stock_Name,stock_Date,seller,buyer,price,quantity,perstockprice):
    con=sql.connect(host='127.0.0.1', user='root', password='', database='stocks')
    cur=con.cursor()
    adduser="""INSERT INTO `book` (`id`, `stock_ID`, `stock_Name`, `stock_Date`, `seller`, `buyer`, `price`, `quantity`, `perstockprice`) VALUES (NULL,%s,%s,%s,%s,%s,%s,%s,%s)"""
    datauser=(stock_ID,stock_Name,stock_Date,seller,buyer,price,quantity,perstockprice)
    cur.execute(adduser,datauser)
    con.commit()
    con.close()

def ViewMovieData():
    con=sql.connect(host='127.0.0.1', user='root', password='', database='stocks')
    cur=con.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    con.close()    
    return rows

def DeleteMovieRec(stock_ID):    
    con=sql.connect(host='127.0.0.1', user='root', password='', database='stocks')
    cur=con.cursor()
    deluser="""DELETE FROM book WHERE stock_ID=%s"""
    dataduser=(stock_ID,)
    cur.execute(deluser,dataduser)
    con.commit()
    con.close()  

def SearchMovieData(stock_ID="",stock_Name="",stock_Date="",seller="",buyer="",price="",quantity="",perstockprice=""):  
    con=sql.connect(host='127.0.0.1', user='root', password='', database='stocks')
    cur=con.cursor()
    searchuser="""SELECT * FROM book WHERE stock_ID=%s OR stock_Name=%s OR stock_Date=%s OR seller=%s OR buyer=%s OR price=%s OR quantity=%s OR perstockprice=%s"""
    datasuser=(stock_ID,stock_Name,stock_Date,seller,buyer,price,quantity,perstockprice)
    cur.execute(searchuser,datasuser)
    rows=cur.fetchall()
    con.close()    
    return rows

def UpdateMovieData(id,stock_ID="",stock_Name="",stock_Date="",seller="",buyer="",price="",quantity="",perstockprice=""):
    con=sql.connect(host='127.0.0.1', user='root', password='', database='stocks')
    cur=con.cursor()
    adduser="""UPDATE book SET stock_Name=%s,stock_Date=%s,seller=%s,buyer=%s,price=%s,quantity=%s,perstockprice=%s, WHERE stock_ID=%s"""
    datauser=(stock_ID,stock_Name,stock_Date,seller,buyer,price,quantity,perstockprice)
    cur.execute(adduser,datauser)
    con.commit()
    con.close()

