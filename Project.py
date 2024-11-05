from tkinter import *
from tkinter import messagebox
class demo:
    
    def  my_database(self):
        import sqlite3
        con=sqlite3.Connection("MyDB")
        cur=con.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS route(route_id INT PRIMARY KEY,station_name VARCHAR(30),station_id INT)')
        cur.execute('CREATE TABLE IF NOT EXISTS operator(operator_id INT PRIMARY KEY,Name VARCHAR(30),Address VARCHAR(50),Phone CHAR(10),Email VARCHAR(30))')
        cur.execute('CREATE TABLE IF NOT EXISTS bus_run(bus_id INT PRIMARY KEY,running_date DATE,seats_available INT)')
        cur.execute('CREATE TABLE IF NOT EXISTS passenger(Name VARCHAR(30),gender VARCHAR(15),no_of_seats INT,mobile_number CHAR(10) PRIMARY KEY,age INT,sno INT,Bus_id INT REFERENCES bus_run(bus_id) ON DELETE CASCADE )')
        cur.execute('CREATE TABLE IF NOT EXISTS bus(bus_id INT REFERENCES bus_run(bus_id) ON DELETE CASCADE,bus_type VARCHAR(15),capacity INT,fare INT,operator_id INT REFERENCES operator(operator_id) ON DELETE CASCADE,route_id INT REFERENCES route(route_id) ON DELETE CASCADE,PRIMARY KEY(bus_id,operator_id,route_id))')
        cur.execute('CREATE TABLE IF NOT EXISTS store_value(value INT)')
        con.commit()


        #cur.execute('DELETE FROM passenger')
        cur.execute('SELECT * FROM passenger')
        con.commit()
        a=cur.fetchall()
        print("passenger",a)
        
        print()
               
        #cur.execute('DELETE FROM bus') 
        cur.execute('SELECT * FROM bus')
        con.commit()
        a=cur.fetchall()
        print("bus",a)
        
        print()
        #cur.execute('DELETE FROM operator')
        cur.execute('select * FROM operator')
        con.commit()
        a=cur.fetchall()
        print("operator",a)
        
        print()
        #cur.execute('DELETE FROM route')
        cur.execute('SELECT * FROM route')
        con.commit()
        a=cur.fetchall()
        print("route",a)
        print()
        
        #cur.execute('DELETE FROM bus_run')
        cur.execute('SELECT * FROM bus_run')
        con.commit()
        a=cur.fetchall()
        print("bus_run",a)
        print() 

        #cur.execute('DELETE FROM store_value')
        cur.execute('SELECT * FROM store_value')
        a=cur.fetchall()
        print("store value",a)

        print()




        
    def front_page(self):
        root=Tk()
        root.geometry('1600x1000')
        root.title('Book Your Ticket')
        img=PhotoImage(file='starbus.png')
        Label(root,text="\n").pack()
        Label(root,image=img).pack()

        Label(root,text="Online Bus Booking System", font="Impact 35 bold").pack()
        Label(root,text="\n").pack()

        Label(root,text="Name : Manoj Kumar Lodha", font="Arial 15 bold",fg="blue").pack()
        Label(root,text="\n").pack()

        Label(root,text="Er. : 221B231", font="Arial 15 bold",fg="blue").pack()
        Label(root,text="\n").pack()

        Label(root,text="Mobile : 6268893387", font="Arial 15 bold",fg="blue").pack()
        Label(root,text="\n").pack()

        Label(root,text="Submitted to : Dr. Mahesh Kumar", font="Arial 22 bold",fg="red").pack()
        Label(root,text="Project Based Learning", font="Arial 18 bold",fg="red").pack()
        Label(root,text="\n").pack()

        def second(event):
            root.destroy()
            self.Menu()

        root.bind("<KeyPress>", second)

        root.mainloop()

        

    def Menu(self):
        root=Tk()
        root.geometry('1600x1000')
        root.title('Book Your Ticket')
        img=PhotoImage(file='starbus.png')
                                               
        Label(root,image=img).grid(row=0,column=0 ,pady=30)
        Label(root,text="Online Bus Booking System", font="Impact 35 bold").grid(row=1,column=0)
        Label(root,text="\n").grid(row=0,column=0)

        fr=Frame(root)
        fr.grid(row=2,column=0,padx=300,pady=60)

        def call1():
            root.destroy()
            self.choose_and_book()

        def call2():
            root.destroy()
            self.check_your_booking()
        
        def call3():
            root.destroy()
            self.add_details()


            
        Button(fr,text="Seat Booking",command=call1,font="Arial 15 bold",bg="purple",fg="white").grid(row=2,column=1,padx=50)
        Button(fr,text="Check Booked Seat",command=call2,font="Arial 15 bold",bg="purple",fg="white").grid(row=2,column=2,padx=50)
        Button(fr,text="Add Bus Details",command=call3,font="Arial 15 bold",bg="purple",fg="white").grid(row=2,column=3,padx=50)
        Label(fr,text="For Admin Only",font="Arial 13 bold",fg="red").grid(row=3,column=3,pady=20)

        root.mainloop()

    def add_details(self):
        import sqlite3
        con=sqlite3.Connection("MyDB")
        cur=con.cursor()

        root=Tk()
        root.geometry('1600x1000')
        root.title('Book Your Ticket')
        img=PhotoImage(file='starbus.png')


        Label(root,image=img).grid(row=0,column=0,padx=300,pady=20)
        Label(root,text="Online Bus Booking System", font="Impact 29 bold").grid(row=1,column=0)
        fr1=Frame(root)

        fr1.grid(row=2,column=0,padx=300,pady=20)
        Label(fr1,text="Add New Details to Database",font="Arial 22 bold",fg="green2",relief="groove",bd=5).grid(row=2,column=0,columnspan=4,padx=50,pady=20)

        def call1():
            root.destroy()
            self.add_operator()

        def call2():
            root.destroy()
            self.add_bus()

        def call3():
            root.destroy()
            self.add_bus_route_details()

        def call4():
            root.destroy()
            self.add_bus_running()

        def callhome():
            root.destroy()
            self.Menu()

        Button(fr1,text="New Operator",command=call1,bg="springgreen",font="monospace 18 bold").grid(row=3,column=0,pady=20,padx=20)
        Button(fr1,text="New Bus",command=call2,bg="sienna1",font="monospace 18 bold").grid(row=3,column=1,pady=20,padx=20)

        Button(fr1,text="New Route",command=call3,bg="dodger blue",font="monospace 18 bold").grid(row=3,column=2,pady=20,padx=20)

        Button(fr1,text="New Run",command=call4,bg="khaki",font="monospace 18 bold").grid(row=3,column=3,pady=20,padx=20)

        icon=PhotoImage(file="icon.png")
        Button(fr1,image=icon,command=callhome,font="monospace 11 bold").grid(row=4,column=4,padx=10,pady=100)


        
        root.mainloop()

    def add_operator(self):
        import sqlite3
        con=sqlite3.Connection("MyDB")
        cur=con.cursor()

        root=Tk()
        root.geometry('1600x1000')
        root.title('Book Your Ticket')
        img=PhotoImage(file='starbus.png')

        Label(root,image=img).grid(row=0,column=0,padx=300,pady=20)
        Label(root,text="Online Bus Booking System", font="Impact 29 bold").grid(row=1,column=0)
        fr1=Frame(root)

        fr1.grid(row=2,column=0,padx=300,pady=20)
        Label(fr1,text=" Add Bus Operator Details ",font="Arial 20 bold",fg="green2",relief="groove",bd=5).grid(row=2,column=0,columnspan=4,padx=50,pady=20)

        fr2=Frame(root)
        fr2.grid(row=3,column=0,padx=300,pady=20)
        Label(fr2,text="Operator id ",font="monospace 11 bold").grid(row=3,column=0)
        operator_id=Entry(fr2)
        operator_id.grid(row=3,column=1)

        Label(fr2,text="Name ",font="monospace 11 bold").grid(row=3,column=2)
        name=Entry(fr2)
        name.grid(row=3,column=3)

        Label(fr2,text="Address ",font="monospace 11 bold").grid(row=3,column=4)
        address=Entry(fr2)
        address.grid(row=3,column=5)



        Label(fr2,text="Phone ",font="monospace 11 bold").grid(row=3,column=6)


        def validate_mobile_number(new_value):
            return new_value.isdigit() and len(new_value)<=10
            

        phone=Entry(fr2,validate="key",validatecommand=(fr2.register(validate_mobile_number),"%P"))
        phone.grid(row=3,column=7)

        Label(fr2,text="Email ",font="monospace 11 bold").grid(row=3,column=8)
        email=Entry(fr2)
        email.grid(row=3,column=9)

        def check_null_entries(a,b,c,d,e):
            if a=="" or b=="" or c=="" or d=="" or e=="":
                return True
            else:
                return False

        def add_operator(a,b,c,d,e):
            if check_null_entries(a,b,c,d,e):
                Label(fr2,text="Enter all fields !",font="monospace 10 bold",fg="red").grid(row=4,column=4,columnspan=2)

            else:     
                try:
                    c=c.casefold()
                    cur.execute('INSERT INTO operator VALUES(?,?,?,?,?)',(a,b,c,d,e))
                    con.commit()
                    messagebox.showinfo('Operator details','Operator added successfully !')
                    print("updated")
                except sqlite3.IntegrityError:
                    messagebox.showinfo("Redefine","Operator already exists !",icon="warning")


            
        def edit_operator(a,b,c,d,e):
            if check_null_entries(a,b,c,d,e):
                messagebox.showinfo('entry','Enter all fields !',icon="error")
                
                Label(fr2,text="",font="monospace 10 bold",fg="red").grid(row=4,column=4,columnspan=2)

            else:
                try:
                    c=c.casefold()
                    cur.execute('INSERT INTO operator VALUES(?,?,?,?,?)',(a,b,c,d,e))
                except sqlite3.IntegrityError:
                    c=c.casefold()
                    cur.execute('DELETE FROM operator WHERE operator_id=(?)',(a,))
                    cur.execute('INSERT INTO operator VALUES(?,?,?,?,?)',(a,b,c,d,e))
                    con.commit()
                    messagebox.showinfo('Operator update','Operator updated successfully')
                    Label(fr2,text="Entries ",font="monospace 10 bold",fg="green2").grid(row=4,column=4,columnspan=2)
                    print("updated")

        def opcall1():
            add_operator(operator_id.get(),name.get(),address.get(),phone.get(),email.get())
            


        def opcall2():
            edit_operator(operator_id.get(),name.get(),address.get(),phone.get(),email.get())
            

        Button(fr2,text="Add",command=opcall1,font="monospace 11 bold",bg="green2").grid(row=3,column=10,padx=5)

        Button(fr2,text="Edit",command=opcall2,font="monospace 11 bold",bg="green2").grid(row=3,column=11,padx=5)

        def callhome():
            root.destroy()
            self.add_details()

        icon=PhotoImage(file="icon.png")
        Button(fr2,image=icon,command=callhome,font="monospace 11 bold").grid(row=5,column=6,padx=5,pady=30)
        root.mainloop()


    def add_bus(self):
        import sqlite3
        con=sqlite3.Connection("MyDB")
        cur=con.cursor()

        root=Tk()
        root.geometry('1600x1000')
        root.title('Book Your Ticket')
        img=PhotoImage(file='starbus.png')

        Label(root,image=img).grid(row=0,column=0,padx=100,pady=30)

        Label(root,text="Online Bus Booking System", font="Impact 29 bold").grid(row=1,column=0)
        fr1=Frame(root)

        fr1.grid(row=2,column=0,padx=100,pady=30)
        Label(fr1,text=" Add Bus Details ",font="Arial 20 bold",fg="green2",relief="groove",bd=5).grid(row=2,column=0,columnspan=4,padx=50,pady=20)

        fr2=Frame(root)
        fr2.grid(row=3,column=0,padx=100,pady=30)
        Label(fr2,text="Bus ID ",font="monospace 11 bold").grid(row=3,column=0)
        bus_id=Entry(fr2)
        bus_id.grid(row=3,column=1)

        Label(fr2,text="Bus Type ",font="monospace 11 bold").grid(row=3,column=2)
        v1=StringVar()
        v1.set("AC 2X2")
        option=["AC 2X2","AC 3X2","Non AC 2X2","Non AC 3X2","AC Sleeper 2X1","Non-AC Sleeper 2X1"]
        OptionMenu(fr2,v1,*option).grid(row=3,column=3,padx=5)


        

        Label(fr2,text="Capacity ",font="monospace 11 bold").grid(row=3,column=4)
        capacity=Entry(fr2)
        capacity.grid(row=3,column=5)

        Label(fr2,text="Fare Rs. ",font="monospace 11 bold").grid(row=3,column=6)
        fare_rupees=Entry(fr2)
        fare_rupees.grid(row=3,column=7)

        Label(fr2,text="Operator ID ",font="monospace 11 bold").grid(row=3,column=8)
        operator_id=Entry(fr2)
        operator_id.grid(row=3,column=9)

        Label(fr2,text="Route id ",font="monospace 11 bold").grid(row=3,column=10)
        route_id=Entry(fr2)
        route_id.grid(row=3,column=11)
        

        def check_null_entries(a,b,c,d,e,f):
            if a=="" or b=="" or c=="" or d=="" or e==""or f=="":
                return True
            else:
                return False

        def _add_bus(a,b,c,d,e,f):
            if check_null_entries(a,b,c,d,e,f) :
                messagebox.showinfo('Entry details','Enter all fields !',icon='error')

            

            else:     
                try:
                    cur.execute('INSERT INTO bus VALUES(?,?,?,?,?,?)',(a,b,c,d,e,f))
                    con.commit()
                    messagebox.showinfo('Entry details','Bus added successfully !')
                    print("updated")
                except sqlite3.IntegrityError:
                    messagebox.showinfo('Entry details','bus already exists !',icon='warning')
        
            
        def edit_bus(a,b,c,d,e,f):
            if check_null_entries(a,b,c,d,e,f) :
                messagebox.showinfo('Entry details','Enter all fields !',icon='error')

            else:
                try:
                    cur.execute('INSERT INTO bus VALUES(?,?,?,?,?,?)',(a,b,c,d,e,f))
                except sqlite3.IntegrityError:
                    cur.execute('DELETE FROM bus WHERE bus_id=(?)',(a,))
                    cur.execute('INSERT INTO bus VALUES(?,?,?,?,?,?)',(a,b,c,d,e,f))
                    con.commit()
                    
                    messagebox.showinfo('Bus update','Bus updated successfully ! !')


        def bcall1():
            _add_bus(bus_id.get(),v1.get(),capacity.get(),fare_rupees.get(),operator_id.get(),route_id.get())

        def bpcall2():
            edit_bus(bus_id.get(),v1.get(),capacity.get(),fare_rupees.get(),operator_id.get(),route_id.get())
    
            
        Button(fr2,text="Add Bus",command=bcall1,font="monospace 11 bold",bg="green2").grid(row=4,column=6,padx=5,pady=40)
        Button(fr2,text="Edit Bus",command=bpcall2,font="monospace 11 bold",bg="green2").grid(row=4,column=7,padx=5,pady=40)

        def callhome():
            root.destroy()
            self.add_details()

        icon=PhotoImage(file="icon.png")
        Button(fr2,image=icon,command=callhome,font="monospace 11 bold").grid(row=4,column=8,padx=5,pady=40)
        root.mainloop()


    def add_bus_route_details(self):
        import sqlite3
        con=sqlite3.Connection("MyDB")
        cur=con.cursor()

        root=Tk()
        #root.attributes('-fullscreen',True)
        root.geometry('1600x1000')
        root.title('Book Your Ticket')
        img=PhotoImage(file='starbus.png')

        Label(root,image=img).grid(row=0,column=0,padx=300,pady=50)

        Label(root,text="Online Bus Booking System", font="Impact 29 bold").grid(row=1,column=0)
        fr1=Frame(root)

        fr1.grid(row=2,column=0,padx=300,pady=50)
        Label(fr1,text=" Add Bus Route Details ",font="Arial 20 bold",fg="green2",relief="groove",bd=5).grid(row=2,column=0,columnspan=4,padx=50,pady=20)


        fr2=Frame(root)
        fr2.grid(row=3,column=0,padx=300)
        Label(fr2,text="Route Id ",font="monospace 11 bold").grid(row=3,column=0,padx=5)
        route_id=Entry(fr2)
        route_id.grid(row=3,column=1)

        Label(fr2,text="Station Name ",font="monospace 11 bold").grid(row=3,column=2,padx=5)
        station_name=Entry(fr2)
        station_name.grid(row=3,column=3)

        Label(fr2,text="Station Id ",font="monospace 11 bold").grid(row=3,column=4,padx=5)
        station_id=Entry(fr2)
        station_id.grid(row=3,column=5)


        def check_null_entries(a,b,c):
            if a=="" or b=="" or c=="":
                return True
            else:
                return False
                

        def add_route(a,b,c):
            if check_null_entries(a,b,c):
                messagebox.showinfo('Entry details','Enter all fields !',icon='error')
            else:     
                try:
                    b=b.casefold()
                    cur.execute('INSERT INTO route VALUES(?,?,?)',(a,b,c))
                    con.commit()
                    messagebox.showinfo('Entry details','route added successfully !')
                    print("updated")
                except sqlite3.IntegrityError:
                    messagebox.showinfo("Check","route already exists !",icon="warning")
       

            
        def delete_route(a,b,c):
            if check_null_entries(a,b,c):
                messagebox.showinfo('Entry details','Enter all fields !',icon='error')
                
            else:
                cur.execute('DELETE FROM route WHERE route_id=(?)',(a,))
                con.commit()
                messagebox.showinfo('Entry details','route deleted successfully !')
                print("updated")

        def rcall1():
            add_route(route_id.get(),station_name.get(),station_id.get())
            


        def rcall2():
            delete_route(route_id.get(),station_name.get(),station_id.get())


        Button(fr2,text="Add Route",command=rcall1,font="monospace 11 bold",bg="green2").grid(row=3,column=6,padx=80)

        Button(fr2,text="Delete Route",command=rcall2,font="monospace 11 bold",bg="green2",fg="red").grid(row=3,column=7,padx=5)

        def callhome():
            root.destroy()
            self.add_details()

        icon=PhotoImage(file="icon.png")
        Button(fr2,image=icon,command=callhome,font="monospace 11 bold").grid(row=4,column=6,padx=5,pady=50)
        root.mainloop()


    def add_bus_running(self):
        import sqlite3
        con=sqlite3.Connection("MyDB")
        cur=con.cursor()

        root=Tk()
        root.geometry('1600x1000')
        root.title('Book Your Ticket')
        img=PhotoImage(file='starbus.png')

        Label(root,image=img).grid(row=0,column=0,padx=300,pady=30)
        Label(root,text="Online Bus Booking System", font="Impact 29 bold").grid(row=1,column=0)
        fr1=Frame(root)

        fr1.grid(row=2,column=0,padx=300,pady=30)
        Label(fr1,text=" Add Bus Running Details ",font="Arial 20 bold",fg="green2",relief="groove",bd=5).grid(row=2,column=0,columnspan=4,padx=50,pady=20)

        fr2=Frame(root)
        fr2.grid(row=3,column=0,padx=300)
        Label(fr2,text="Bus ID ",font="monospace 11 bold").grid(row=3,column=0,padx=5)
        bus_id=Entry(fr2)
        bus_id.grid(row=3,column=1)

        Label(fr2,text="Running Date ",font="monospace 11 bold").grid(row=3,column=2,padx=5)
        running_date=Entry(fr2)
        running_date.grid(row=3,column=3)

        Label(fr2,text="Seat Available ",font="monospace 11 bold").grid(row=3,column=4,padx=5)
        seat_available=Entry(fr2)
        seat_available.grid(row=3,column=5)

        def check_null_entries(a,b,c):
            if a=="" or b=="" or c=="":
                return True
            else:
                return False
                

        def add_bus_run(a,b,c):
            if check_null_entries(a,b,c):
                messagebox.showinfo('Entry','Enter all fields !',icon='error')
            else:     
                try:
                    cur.execute('INSERT INTO bus_run VALUES(?,?,?)',(a,b,c))
                    con.commit()
                    messagebox.showinfo('Entry details','bus run added successfully !')

                    print("updated")
                except (sqlite3.IntegrityError,sqlite3.OperationalError):
                    messagebox.showinfo("Check","bus run already exists !",icon="warning")

            
        def delete_bus_run(a,b,c):
            if check_null_entries(a,b,c):
                 messagebox.showinfo('Entry','Enter all fields !',icon='error')
                
            else:
                cur.execute('DELETE FROM bus_run WHERE bus_id =? AND running_date=? AND seats_available=?',(a,b,c))
                con.commit()
                messagebox.showinfo('Entry details','bus run deleted successfully !')
                print("updated")

        def brcall1():
            add_bus_run(bus_id.get(),running_date.get(),seat_available.get())
            


        def brcall2():
            delete_bus_run(bus_id.get(),running_date.get(),seat_available.get())


        Button(fr2,text="Add Run",command=brcall1,font="monospace 11 bold",bg="green2").grid(row=3,column=6,padx=5)

        Button(fr2,text="Delete Run",command=brcall2,font="monospace 11 bold",bg="green2").grid(row=3,column=7,padx=7)

        def callhome():
            root.destroy()
            self.add_details()

        icon=PhotoImage(file="icon.png")
        Button(fr2,image=icon,command=callhome,font="monospace 11 bold").grid(row=4,column=6,padx=5,pady=50)
        root.mainloop()


    def check_your_booking(self):
        import sqlite3
        con=sqlite3.Connection("MyDB")
        cur=con.cursor()

        root=Tk()
        root.geometry('1600x1000')
        root.title('Book Your Ticket')
        img=PhotoImage(file='starbus.png')

        Label(root,image=img).grid(row=0,column=0,padx=500,pady=10)
        Label(root,text="Online Bus Booking System", font="Impact 29 bold").grid(row=1,column=0)

        fr1=Frame(root)
        #fr1=Frame(root,relief="raised",bd=5)
        fr1.grid(row=2,column=0,padx=300)
        Label(fr1,text="Check Your Booking",font="Arial 15 bold",fg="green4",bg="palegreen").grid(row=2,column=1,columnspan=8,padx=8,pady=8)
        Label(fr1,text="Enter Mobile No.:",font="monospace 10 bold").grid(row=3,column=1,padx=5)


        def validate_mobile_number(new_value):
            return len(new_value)<=10



        
        Mobile_number=Entry(fr1,validate="key",validatecommand=(fr1.register(validate_mobile_number),"%P"))
        Mobile_number.grid(row=3,column=2,padx=5)
                    
        fr=Frame(root)
        fr=Frame(root,relief="raised",bd=5)
        fr.grid(row=3,column=0,padx=0,pady=0)

        def check_null(a):
            return True if a=="" else False

        def complete_data(data):
            for i in data:
                if i==None:
                    return False
            return True
                
            

        def check_booking(n):
            cur.execute('SELECT Name,no_of_seats,age,sno,gender,Bus_id,sno FROM passenger WHERE mobile_number=(?)',(n,))
            data=cur.fetchall()
            print(data)


            if len(data)>=1:
                
                data=data[0]

                if complete_data(data):
                    cur.execute('SELECT fare,operator_id,route_id FROM bus WHERE bus_id=(?)',(data[-2],))
                    data1=cur.fetchall()
                    print(data1)
                    data1=data1[0]
                    

                    cur.execute('SELECT Address FROM operator WHERE operator_id=(?)',(data1[1],))
                    input_data4=cur.fetchall()
                    print(input_data4)
                    input_data4=input_data4[0]
                    

                    cur.execute('SELECT station_name FROM route WHERE route_id=(?)',(data1[2],))
                    input_data5=cur.fetchall()
                    print(input_data5)
                    input_data5=input_data5[0]
                    
                    cur.execute('SELECT running_date FROM bus_run WHERE bus_id=(?)',(data[-2],))
                    input_data6=cur.fetchall()
                    print(input_data6)
                    input_data6=input_data6[0]


                    Label(fr,text=f"Passengers : {data[0]}",font="monospace 15 bold").grid(row=1,column=0)
                    Label(fr,text=f"No of seats : {data[1]}",font="monospace 15 bold").grid(row=2,column=0)
                    Label(fr,text=f"Age : {data[2]}",font="monospace 15 bold").grid(row=3,column=0)
                    Label(fr,text=f"Booking refs: {data[3]}",font="monospace 15 bold").grid(row=4,column=0)
                    Label(fr,text=f"Travel On : {input_data6[0]}",font="monospace 15 bold").grid(row=5,column=0)
                    Label(fr,text=f"Destination Point: {input_data5[0]}",font="monospace 15 bold").grid(row=6,column=0,pady=20)
                    # right
                    Label(fr,text=f"Gender : {data[4]}",font="monospace 15 bold").grid(row=1,column=1)
                    Label(fr,text=f"Phone : {n}",font="monospace 15 bold").grid(row=2,column=1)
                    Label(fr,text=f"Fare Rs. : {data1[0]}",font="monospace 15 bold").grid(row=3,column=1)
                    Label(fr,text=f"Boarding Point: {input_data4[0]}",font="monospace 15 bold").grid(row=6,column=1,pady=20)

                    Label(fr,text=f"* Total amount Rs. {data[1]*data1[0]} /- To be paid at the Time of Boarding the bus",font="Arial 14 italic").grid(row=7,column=0,columnspan=2)

                else:
                    messagebox.showinfo('Info','Incomplete data fetched!',icon='error')
                    
                    
                    
            else:
                messagebox.showinfo('Records not found!','Cannot fetch details,Enter valid mobile number')
                

        def mcheckbook():
            if check_null(Mobile_number.get()):
                messagebox.showinfo('Entry details','Entry cannot be empty !',icon='error')
            
            else:
                check_booking(Mobile_number.get())
                
        Button(fr1,text="Check Booking",font="monospace 10 bold",command=mcheckbook,fg="white",bg="purple").grid(row=3,column=3,padx=5)

        def callhome():
            root.destroy()
            self.Menu()

        icon=PhotoImage(file="icon1.png")
        Button(fr1,image=icon,command=callhome,font="monospace 11 bold",bg="white").grid(row=3,column=4,padx=20,pady=30)

        root.mainloop()
        
    def bus_ticket(self):
        import sqlite3
        con=sqlite3.Connection("MyDB")
        cur=con.cursor()
        root=Tk()
        root.geometry('1600x1000')
        root.title('Book Your Ticket')

        cur.execute('SELECT no_of_seats,Bus_id FROM passenger order by sno desc limit 1')
        input_data=cur.fetchall()
        #print(input_data)

        
        cur.execute('SELECT fare FROM bus WHERE bus_id=(?)',(input_data[0][1],))
        input_data3=cur.fetchall()
        #print(input_data3)
        input_data3=input_data3[0][0]

        if messagebox.askyesno("fare confirm",f"The total amount to be paid is {input_data[0][0]*input_data3} Rs.")==True:
            print("true")
        else:
            cur.execute('SELECT mobile_number FROM passenger order by sno desc limit 1')
            dq=cur.fetchall()
            cur.execute('DELETE FROM passenger WHERE mobile_number=(?)',(dq[0][0],))
            con.commit()
            root.destroy()
            self.Menu()        


        image_obj=PhotoImage(file='starbus.png')
        Label(root,image=image_obj).grid(row=0,column=0,padx=400,pady=20)

        Label(root,text="Online Bus Booking System", font="Impact 29 bold").grid(row=1,column=0)

        Label(root,text="Bus Ticket",font="Arial 20 bold").grid(row=2,column=0,columnspan=2,pady=20)
        fr=Frame(root)
        fr=Frame(root,relief="raised",bd=5)
        fr.grid(row=3,column=0,padx=400,pady=10)
        cur.execute('SELECT Name,no_of_seats,age,sno,gender,mobile_number,Bus_id FROM passenger order by sno desc limit 1')
        input_data=cur.fetchall()
        
        busids=input_data[0][-1]
        
        cur.execute('SELECT running_date FROM bus_run WHERE bus_id=(?)',(busids,))
        input_data2=cur.fetchall()
        input_data2=input_data2[0][0]

        cur.execute('SELECT fare,bus_type,operator_id FROM bus WHERE bus_id=(?)',(busids,))
        input_data3=cur.fetchall()
        #print(input_data3[0])

        oprid=input_data3[0][-1]
        cur.execute('SELECT Address FROM operator WHERE operator_id=(?)',(oprid,))
        input_data4=cur.fetchall()
        

        # left 
        Label(fr,text=f"Passengers : {input_data[0][0]}",font="monospace 15 bold").grid(row=1,column=0,padx=50)
        Label(fr,text=f"No of seats : {input_data[0][1]}",font="monospace 15 bold").grid(row=2,column=0)
        Label(fr,text=f"Age : {input_data[0][2]} yrs.",font="monospace 15 bold").grid(row=3,column=0)
        Label(fr,text=f"Booking refs: {input_data[0][3]}",font="monospace 15 bold").grid(row=4,column=0)
        Label(fr,text=f"Travel On : {input_data2}",font="monospace 15 bold").grid(row=5,column=0)
        #Label(fr,text="No of seats: ",font="monospace 15 bold").grid(row=6,column=0)

        # right
        Label(fr,text=f"Gender : {input_data[0][4]}",font="monospace 15 bold").grid(row=1,column=1,padx=10)
        Label(fr,text=f"Phone : {input_data[0][5]}",font="monospace 15 bold").grid(row=2,column=1,padx=10)
        Label(fr,text=f"Fare Rs. : {input_data3[0][0]}",font="monospace 15 bold").grid(row=3,column=1)
        Label(fr,text=f"Bus Detail : {input_data3[0][1]}",font="monospace 15 bold").grid(row=4,column=1)
        #Label(fr,text="Booked On : ",font="monospace 15 bold").grid(row=5,column=1)
        Label(fr,text=f"Boarding Point: {input_data4[0][0]}",font="monospace 15 bold").grid(row=5,column=1,pady=10)
        Label(fr,text=f"* Total amount Rs. {(input_data[0][1])*(input_data3[0][0])} /- To be paid at the Time of Boarding the bus",font="Arial 14 italic").grid(row=8,column=0,columnspan=2)

        def callhome():
            root.destroy()
            self.Menu()

        icon=PhotoImage(file="icon1.png")
        Button(root,image=icon,command=callhome,font="monospace 11 bold").grid(row=4,column=1,padx=20,pady=10)

        
        root.mainloop()


    def choose_and_book(self):
        import sqlite3
        con=sqlite3.Connection("MyDB")
        cur=con.cursor()
        root=Tk()
        root.geometry('1600x1000')
        root.title('Book Your Ticket')
              
        img=PhotoImage(file='starbus.png')

        
        cur.execute('DELETE FROM store_value')
        con.commit()
        

        Label(root,image=img).grid(row=0,column=0,padx=500,pady=10) 
        Label(root,text="Online Bus Booking System", font="Impact 29 bold").grid(row=1,column=0)

        fr1=Frame(root)

        fr1.grid(row=2,column=0,padx=150,pady=20)
        Label(fr1,text="Enter journey Details",font="Arial 15 bold",fg="green4",bg="palegreen").grid(row=2,column=1,columnspan=8,padx=8,pady=8)
        Label(fr1,text="To",font="sans-serif 10 bold").grid(row=3,column=1,padx=3)


        def check_null(a,b,c):
            if a=="" or b=="" or c=="":
                return True
            else:
                return False
            
        start=Entry(fr1)
        start.grid(row=3,column=2,padx=3)


        Label(fr1,text="From",font="sans-serif 10 bold").grid(row=3,column=3,padx=3)
        station=Entry(fr1)
        station.grid(row=3,column=4,padx=3)

        Label(fr1,text="Journey Date",font="sans-serif 10 bold").grid(row=3,column=5,padx=3)
        journey_date=Entry(fr1)
        journey_date.grid(row=3,column=6,padx=3)

        
        Label(fr1,text="DD-MM-YYYY",font="sans-serif 10 bold",fg="red").grid(row=4,column=6,padx=3,pady=5)


        def Proceed():
            cur.execute('SELECT* FROM store_value')
            f1=cur.fetchall()
            try: 
                print(f1[0][0])
            except IndexError:
                messagebox.showinfo("Check","Perheps, you fogot to select the bus !",icon="error")
                
            
            #print(f1)
            
            
            fr3=Frame(root)
            fr3.grid(row=5,column=0,pady=20)
            Label(fr3,text="Fill Passenger Details to book the ticket",font="Arial 15 bold",fg="red").grid(row=1,column=0,columnspan=12,pady=10)

            Label(fr3,text="Name").grid(row=2,column=0,padx=5)
            Name=Entry(fr3)
            Name.grid(row=2,column=1,padx=5)

            
            v1=StringVar()
            v1.set("Male")
            option=["Male","Female","Third Gender"]
            Label(fr3,text="Gender : ").grid(row=2,column=2,padx=5)
            OptionMenu(fr3,v1,*option).grid(row=2,column=3,padx=5)
            

            Label(fr3,text="No of Seats").grid(row=2,column=4,padx=5)
            No_of_Seats=Entry(fr3)
            No_of_Seats.grid(row=2,column=5,padx=5)

            Label(fr3,text="Mobile No").grid(row=2,column=6,padx=5)
#=============================================================================
            def validate_mobile_number(new_value):
                return new_value.isdigit() and len(new_value)<=10
            
            Mobile_No=Entry(fr3,validate="key",validatecommand=(fr3.register(validate_mobile_number),"%P"))
            Mobile_No.grid(row=2,column=7)

            def validate_age(new_value1):
                return new_value1.isdigit() and int(new_value1)<=120

                
            Label(fr3,text="Age").grid(row=2,column=8,padx=5)
            Age=Entry(fr3,validate="key",validatecommand=(fr3.register(validate_age),"%P"))
            Age.grid(row=2,column=11,padx=5)

#===============================================================         

            def check_null(a,b,c,d,e):
                if a=="" or b=="" or c=="" or d=="" or e=="":
                    return True
                else:
                    return False     

            def book_seat():
                def check_duplicate():     
                    cur.execute('SELECT * from passenger WHERE mobile_number=(?)',(Mobile_No.get(),))
                    as_=cur.fetchall()

                    try:
                        as_=as_[0]
                    except IndexError:
                        return False
                    return True

                cur.execute('SELECT * from store_value')
                f=cur.fetchall()
                f=f[-1][0]

                cur.execute('SELECT seats_available from bus_run where bus_id=(?)',(f,))
                a=cur.fetchall()
                

                
                if check_null(Name.get(),v1.get(),No_of_Seats.get(),Mobile_No.get(),Age.get()):
                    messagebox.showinfo("Check","Empty entries are not allowed !",icon="error")

                elif check_duplicate():
                    messagebox.showinfo("Check","Duplicate mobile number !",icon="warning")

                elif int(a[-1][0])<=0:
                   messagebox.showinfo("Check","Seats cannot be booked!",icon="warning")
                   
#===========================================================================================
                elif validate_age (Age.get()) and int(Age.get())<6:
                    messagebox.showinfo("Age bound","Age must be greater than 6 Yrs. !",icon="warning")

                elif len(Mobile_No.get())<10:
                    messagebox.showinfo("Mobile Number ","Enter 10- digit Mobile number !",icon="warning")

                elif int(No_of_Seats.get())>int(a[-1][0]) or int(No_of_Seats.get())==0:
                    messagebox.showinfo("Unavailable seats ","Enter seats is more or less than the available seats!",icon="warning")
                    
#=====================================================================================                    
                else:  
                    no_of_entries_in_passenger=0
                    cur.execute('SELECT COUNT(*) FROM passenger')
                    no_of_entries_in_passenger=cur.fetchall()
                    no_of_entries_in_passenger=no_of_entries_in_passenger[0][0]
                    sno=no_of_entries_in_passenger+1
                    
                    cur.execute('SELECT * FROM store_value')
                    vap=cur.fetchall()                 

                    vap=vap[0]                
                    
                    try:
                        cur.execute('INSERT INTO passenger(Name,gender,no_of_seats,mobile_number,age,sno,Bus_id)VALUES(?,?,?,?,?,?,?)',(Name.get(),v1.get(),No_of_Seats.get(),Mobile_No.get(),Age.get(),sno,vap[0]))
                            
                    except sqlite3.IntegrityError:
                        Label(fr3,text="Enter valid entries !",font="Arial 16 italic bold",fg="red").grid(row=3,column=0,padx=5,columnspan=11,pady=50)
                    con.commit()
                    vap=vap[0]
                        
                    cur.execute('SELECT * FROM store_value')
#=====================================================                        
                    ids=cur.fetchall()
                    cur.execute('SELECT seats_available from bus_run WHERE bus_id=(?)',(ids[0][0],))
                    n=cur.fetchall()
                        


                    seats=n[0][0]
                    seats=seats-int(No_of_Seats.get())
#=============================================================                        
                    cur.execute('UPDATE bus_run SET seats_available=(?) WHERE bus_id=(?)',(seats,ids[0][0]))
                    con.commit()
                        
                    root.destroy()
                    self.bus_ticket()

            Button(fr3,text="Book Seat",command=book_seat,bg="Springgreen").grid(row=2,column=12,padx=5)


        def generate_data():
            destination=start.get()    
            start_place=station.get()           
            date=journey_date.get()
            
            cur.execute('SELECT operator.Name, operator.Address,bus.bus_id,bus.bus_type,bus.capacity,bus.fare,bus.route_id FROM operator INNER JOIN bus ON operator.operator_id=bus.operator_id')
            data1=cur.fetchall()
                            
            cur.execute('CREATE TABLE IF NOT EXISTS bco(name VARCHAR(15),address VARCHAR(30),bus_id INT,bus_type VARCHAR(10),capacity INT,fare INT,route_id INT)')
            for record_data1 in data1:
                cur.execute('INSERT INTO bco VALUES(?,?,?,?,?,?,?)',(record_data1[0],record_data1[1],record_data1[2],record_data1[3],record_data1[4],record_data1[5],record_data1[6]))

            con.commit()
            cur.execute('select * from bco')
            data2=cur.fetchall()

            cur.execute('SELECT bco.address,route.station_name,bco.bus_id,bco.name,bco.bus_type,bco.capacity,bco.fare FROM bco INNER JOIN route ON bco.route_id=route.route_id')
            data3=cur.fetchall()

            cur.execute('CREATE TABLE IF NOT EXISTS bco_c_r(address VARCHAR(30),station_name VARCHAR(30),bus_id INT,name VARCHAR(15),bus_type VARCHAR(10),capacity INT,fare INT)')
            for record_data3 in data3:
                cur.execute('INSERT INTO bco_c_r VALUES(?,?,?,?,?,?,?)',(record_data3[0],record_data3[1],record_data3[2],record_data3[3],record_data3[4],record_data3[5],record_data3[6]))
                            
            con.commit()
            cur.execute('select * from bco_c_r')
            data4=cur.fetchall()

            cur.execute('SELECT bco_c_r.address,bco_c_r.station_name,bco_c_r.bus_id,bco_c_r.name,bco_c_r.bus_type,bco_c_r.capacity,bco_c_r.fare,bus_run.running_date,bus_run.seats_available FROM bco_c_r INNER JOIN bus_run ON bco_c_r.bus_id=bus_run.bus_id')
            data5=cur.fetchall()

            cur.execute('CREATE TABLE IF NOT EXISTS bco_c_r_c_br(address VARCHAR(30),station_name VARCHAR(30),bus_id INT,name VARCHAR(15),bus_type VARCHAR(10),capacity INT,fare INT,running_date DATE,seats_available INT)')

            for record_data5 in data5:
                cur.execute('INSERT INTO bco_c_r_c_br VALUES(?,?,?,?,?,?,?,?,?)',(record_data5[0],record_data5[1],record_data5[2],record_data5[3],record_data5[4],record_data5[5],record_data5[6],record_data5[7],record_data5[8]))
            con.commit()
            destination=destination.casefold()
            start_place=start_place.casefold()

            cur.execute('select name,bus_type,seats_available,capacity,fare,bus_id from bco_c_r_c_br WHERE station_name=? AND address=? AND running_date=?',(destination,start_place,date))
            data6=cur.fetchall()
                
            cur.execute('DROP TABLE bco ')
            cur.execute('DROP TABLE bco_c_r')
            cur.execute('DROP TABLE bco_c_r_c_br')
            con.commit()
            return data6


        fr2=Frame(root)
        #fr2=Frame(root,relief="raised",bd=5)
        fr2.grid(row=4,column=0)

        def get_val(a,row_):
            cur.execute('DELETE FROM store_value')
            con.commit()
            cur.execute('INSERT INTO store_value VALUES(?)',(a,))
            con.commit()
            Button(fr2,text="   Bus  ",font="Arial 12 bold",bg="blue",fg="white").grid(row=row_,column=0,pady=10)
            

        def print_header():
            Label(fr2,text="Select Bus",font="Arial 12 bold",fg="green").grid(row=1,column=0,padx=10)
            Label(fr2,text="Operator",font="Arial 12 bold",fg="green").grid(row=1,column=1,padx=30)
            Label(fr2,text="Bus Type",font="Arial 12 bold",fg="green").grid(row=1,column=2,padx=30)
            Label(fr2,text="Available/Capacity",font="Arial 12 bold",fg="green").grid(row=1,column=3,padx=30)
            Label(fr2,text="Fare",font="Arial 12 bold",fg="green").grid(row=1,column=4,padx=30)

        def partial_print(data,row_,i):
            Button(fr2,text=f"Bus {i}",command=lambda:get_val(data[5],row_),font="Arial 12 bold",bg="Springgreen",fg="white",activebackground="blue").grid(row=row_,column=0,pady=10)
            Label(fr2,text=data[0],font="Arial 12 bold",fg="blue").grid(row=row_,column=1,pady=10)
            Label(fr2,text=data[1],font="Arial 12 bold",fg="blue").grid(row=row_,column=2,pady=10)
            Label(fr2,text=f"{(data[2])}/{(data[3])}",font="Arial 12 bold",fg="blue").grid(row=row_,column=3,pady=10)
            Label(fr2,text=data[4],font="Arial 12 bold",fg="blue").grid(row=row_,column=4,pady=10)
            Button(fr2,text="Proceed to Book",command=Proceed,bg="Springgreen").grid(row=row_,column=5,pady=10)
                 
    
        def show_Bus():
            data=generate_data()
            #print(data)
            x=0
            try:
                x=len(data)
            except TypeError:
                x=0
            if not x:    
                if x==0 and check_null(start.get(),station.get(),journey_date.get()):
                    messagebox.showinfo("Check","Entries can't be empty! ",icon="error")

                else:
                    if x==0: 
                        messagebox.showinfo("Information","No Buses available for this route ")
            else:
                print_header()
                i=1
                _row_partial=2
                for records in data:
                    partial_print(records,_row_partial,i)
                    _row_partial+=1
                    i=i+1
                
        
        Button(fr1,text="Show Bus",command=show_Bus,bg="purple",fg="white").grid(row=3,column=7,padx=10)
        home=PhotoImage(file="icon1.png")

        def callhome():
            root.destroy()
            self.Menu()
        
        Button(fr1,image=home,command=callhome).grid(row=3,column=8,padx=7)
        root.mainloop() 

d1=demo()
d1.my_database()
d1.front_page()

