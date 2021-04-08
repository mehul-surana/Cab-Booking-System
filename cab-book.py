
import sqlite3                                
conn=sqlite3.connect("cabooks.db")
c=conn.cursor();
# try:
#     conn.execute(''' CREATE TABLE admin
#         (admin_id INTEGER PRIMARY KEY,
#         admin_username varchar(20) NOT NULL,
#         admin_password varchar(20) NOT NULL)''')
#     conn.execute(''' CREATE TABLE cab_dealer
#         (cabdealer_id INTEGER primary key,
#         cabdealer_name varchar(20) NOT NULL,
#         cabdealer_password varchar(20) NOT NULL,
#         cabdealer_emailid varchar(20) NOT NULL,
#         cabdealer_phone INT(20) NOT NULL)''')
#     conn.execute(''' CREATE TABLE cabs
#         (cab_id INTEGER PRIMARY KEY,
#         cab_name varchar(20) NOT NULL,
#         cab_type varchar(20) NOT NULL,
#         cab_model varchar(20) NOT NULL,
#         cab_dealerid INT(20) NOT NULL,
#         cab_from varchar(20) NOT NULL,
#         cab_to varchar(20) NOT NULL)''')
#     conn.execute(''' CREATE TABLE user
#         (user_id INTEGER primary key,
#         user_name varchar(20) not null,
#         user_password varchar(20) not null,
#         user_emailid varchar(20) not null,
#         user_phone INT(20) not null)''')
#     print("table created")
# except:
#     print("some error")




def dealer_reg():
    cabdealer_name=input(" enter your name:")
    cabdealer_emailid=input(" enter your emailid: ")
    cabdealer_password=input(" enter your psswrd: ")
    cabdealer_phone=input(" enter your phone no.: ")
    ins="INSERT INTO cab_dealer(cabdealer_name,cabdealer_emailid,cabdealer_password,cabdealer_phone) VALUES ('"+cabdealer_name+"','"+cabdealer_emailid+"','"+cabdealer_password+"','"+cabdealer_phone+"')"
    
    c.execute(ins)
    conn.commit()
    print("     DEALER CREATED    ")
    main()
def dealer_log():
    global cabdealer_id
    cabdealer_name=input(" enter your name: ")
    cabdealer_password=input(" enter your psswrd: ")
    data=c.execute("SELECT * FROM cab_dealer WHERE cabdealer_name='"+cabdealer_name+"' and cabdealer_password='"+cabdealer_password+"'")
    d=data.fetchall()
    t=len(d)
    for a in d:
        cabdealer_id=a[0]


    if t==1:
        #print(cabdealer_id)
        print("   login successfully   ")
        dealer_main()
    else:
        print("invalid username and password")
        dealer_log()
    
          


            
                
            

    

def dealer_main():
    global cabdealer_id

    print(''' 
            1 add cabs
            2 view cabs
            3 delete cab
            4 update cab
            5 logout
            ''')
    dc=int(input(" enter your choice: "))
    if dc==1:
        add_cab()
    elif dc==2:
        view_cab()
    elif dc==3:
        delete_cab()
    elif dc==4:
        #view_cab()
        update_cab()
    elif dc==5:
        del cabdealer_id
        main()

def update_cab():
    global cabdealer_id

    cab_name=input(" enter  cab name: ")
    cab_type=input(" enter  cab type : ")
    cab_model=input(" enter  cab model : ")
    cabdealer_id= cabdealer_id # cabdealer_id => cab_dealer table
    cab_from=input(" enter cab FROM: ")
    cab_to=input(" enter  cab TO: ")
    cab_id=input(" enter the cab_id")
    upd="UPDATE cabs set cab_name='"+cab_name+"',cab_type='"+cab_type+"',cab_model='"+cab_model+"',cab_from='"+cab_from+"',cab_to='"+cab_to+"' where cab_id='"+str(cab_id)+"'"
    
    c.execute(upd)
    conn.commit()
    print(" cab created ")
    dealer_main()



def add_cab():
    global cabdealer_id
    cab_name=input(" enter  cab name: ")
    cab_type=input(" enter  cab type : ")
    cab_model=input(" enter  cab model : ")
    cab_dealerid= cabdealer_id # cabdealer_id => cab_dealer table
    cab_from=input(" enter cab FROM: ")
    cab_to=input(" enter  cab TO: ")
    ins=" INSERT into cabs (cab_name,cab_type,cab_model,cab_dealerid,cab_from,cab_to) VALUES ('"+cab_name+"','"+cab_type+"','"+cab_model+"','"+str(cab_dealerid)+"','"+cab_from+"','"+cab_to+"')"
    c.execute(ins)
    conn.commit()
    print(" cab created ")
    dealer_main()

def view_cab():
    global cabdealer_id
    data="SELECT c.cab_id,c.cab_name,c.cab_type,c.cab_model,d.cabdealer_name,c.cab_from,c.cab_to  FROM cabs  as c inner join cab_dealer as d  on c.cab_dealerid = d.cabdealer_id where c.cab_dealerid='"+str(cabdealer_id)+"'"
    cabdata=c.execute(data)
    d=cabdata.fetchall()
    print("{0:20}{1:20}{2:20}{3:20}{4:20}{5:20}{6:20}".format("CAB ID ","CAB NAME","CAB TYPE","CAB MODEL","CAB DEALER NAME","CAB FROM","CAB TO"))
    for a in d:
        print("{0:<20}{1:<20}{2:<20}{3:<20}{4:<20}{5:<20}{6:<20}".format(a[0],a[1],a[2],a[3],a[4],a[5],a[6]))
    dealer_main()   

def delete_cab():
    cabid=input(" enter the cab_id ")
    del1="DELETE FROM cabs where cab_id='"+cabid+"' and cab_dealerid='"+str(cabdealer_id)+"'"
    c.execute(del1)
    conn.commit()
    dealer_main()

  
    
    


def user_reg():
    user_name=input(" enter your name: ")
    user_emailid=input(" enter your emailid: ")
    user_password=input(" enter your psswrd: ")
    user_phone=input(" enter your phone no.: ")
    data=c.execute("SELECT * FROM user where user_emailid='"+user_emailid+"'")

    t=len(data.fetchall())
    if t==0:
        ins="INSERT INTO user(user_name,user_emailid,user_password,user_phone) VALUES('"+user_name+"','"+user_emailid+"','"+user_password+"','"+user_phone+"')"
        c.execute(ins)
        conn.commit()
        print("user created")
        main()
    else:
        print("user email id already exist")
        user_reg()

def user_log():
    global user_id
    user_name=input(" enter your user_name: ")
    user_password=input(" enter your psswrd: ")
    data=c.execute("SELECT * FROM user where user_name='"+user_name+"' and user_password='"+user_password+"'")
    d=data.fetchall()
    t=len(d)
    for a in d:
        user_id=a[0]
    if t==1:
        print(" login successfully....... ")
        user_main()
    else:
        print("invalid username and password")
        main()


def viewall_cabs():
    global user_id

    data="SELECT c.cab_id,c.cab_name,c.cab_type,c.cab_model,d.cabdealer_name,c.cab_from,c.cab_to  FROM cabs  as c inner join cab_dealer as d  on c.cab_dealerid = d.cabdealer_id "
    cabdata=c.execute(data)
    d=cabdata.fetchall()
    print("{0:20}{1:20}{2:20}{3:20}{4:20}{5:20}{6:20}".format("CAB ID ","CAB NAME","CAB TYPE","CAB MODEL","CAB DEALER NAME","CAB FROM","CAB TO"))
    for a in d:
        print("{0:<20}{1:<20}{2:<20}{3:<20}{4:<20}{5:<20}{6:<20}".format(a[0],a[1],a[2],a[3],a[4],a[5],a[6]))
    user_main() 

def search_cab(cab_from="",cab_to=""):

    #global user_id
    if (cab_from!="" and cab_to!=""):
        data="SELECT c.cab_id,c.cab_name,c.cab_type,c.cab_model,d.cabdealer_name,c.cab_from,c.cab_to  FROM cabs  as c inner join cab_dealer as d  on c.cab_dealerid = d.cabdealer_id where cab_from='"+(cab_from)+"' and cab_to='"+cab_to+"' "
    else:
        data="SELECT c.cab_id,c.cab_name,c.cab_type,c.cab_model,d.cabdealer_name,c.cab_from,c.cab_to  FROM cabs  as c inner join cab_dealer as d  on c.cab_dealerid = d.cabdealer_id "
    cabdata=c.execute(data)
    d=cabdata.fetchall()
    print("{0:20}{1:20}{2:20}{3:20}{4:20}{5:20}{6:20}".format("CAB ID ","CAB NAME","CAB TYPE","CAB MODEL","CAB DEALER NAME","CAB FROM","CAB TO"))
    for a in d:
        print("{0:<20}{1:<20}{2:<20}{3:<20}{4:<20}{5:<20}{6:<20}".format(a[0],a[1],a[2],a[3],a[4],a[5],a[6]))
    user_main() 

def updt_profile():
    global user_id
    user_emailid=input(" enter your emailid: ")
    user_phone=input(" enter your phone no : ")
    upd="UPDATE user set user_emailid='"+user_emailid+"',user_phone='"+user_phone+"' where user_id= '"+str(user_id)+"'"
    c.execute(upd)
    conn.commit()
    print(" PROFILE UPDATED ")
    user_main()
        
        
def change_password():
    global user_id
    old_password=input(" ENTER THE old_password ")
    #new_password=input(" ENTER THE new_password ")
    data=c.execute("SELECT * FROM user where user_password='"+old_password+"' and user_id='"+str(user_id)+"'")
    d=data.fetchall()
    t=len(d)
    if t==1:
        new_password=input(" ENTER THE new_password ")
        confirm_password=input(" ENTER THE confirm_password ")
        if new_password==confirm_password:
            upd="update user set user_password='"+new_password+"' where user_id= '"+str(user_id)+"' "
            c.execute(upd)
            conn.commit()
            print("password updated ......... ")
            user_main()
        else:   
            print(" new password and confirm password not matching ...... ")

    else:       
        print(" invalid old password ....")
        user_main()

        
    




def user_main():
    global user_id
    print(''' 
            1 view  all cabs
            2 search cabs
            3 update profile
            4 change password 
            5 logout
            ''')
    dc=int(input(" enter your choice: "))
    if dc==1:
        viewall_cabs()
        
    elif dc==2:
        cab_from=input(" enter cab from: ")
        cab_to=input(" enter cab to: ")

        search_cab(cab_from,cab_to)
    elif dc==3:
        updt_profile()

    elif dc==4:
        change_password()

        
    
    elif dc==5:
        #del user_id
        main()

# def admin_reg():
#     admin_username=input(" enter your name:")
#     admin_password=input(" enter your psswrd: ")
    
#     ins="INSERT INTO admin(admin_username,admin_password) VALUES ('"+admin_username+"','"+admin_password+"')"
    
#     c.execute(ins)
#     conn.commit()
#     print("     admin CREATED    ")
#     main()
        
def admin_log():
    global admin_id
    admin_username=input(" enter your username: ")
    admin_password=input(" enter your password: ")
    data=c.execute("SELECT * FROM admin WHERE admin_username='"+admin_username+"' and admin_password='"+admin_password+"'")

    d=data.fetchall()
    #print("hello")
    for a in d:
        admin_id=a[0]
    t=len(d)
    if (t==1):
        print(" login successfully ")
        admin_main()
    else:
        print(" invalid username and password ")
        admin_log()

        
    

def display_user():
    global user_id
    global admin_id
    print("{0:20}{1:20}{2:20}{3:20}".format("USER ID ","USER NAME","USER EMAIL","USER PHONE"))
    data="SELECT user_id,user_name,user_emailid,user_phone FROM user"
    userdata=c.execute(data)
    d=userdata.fetchall()
    for a in d:
        print("{0:<20}{1:<20}{2:<20}{3:<20}".format(a[0],a[1],a[2],a[3]))
    #user_main()
    
    dc=int(input(" enter 1: for delete  "))
    if dc==1:
        user_id=int(input(" enter user_id: "))
        deldata="DELETE  from user where user_id='"+str(user_id)+"' "
        c.execute(deldata)
        conn.commit()
        print(" user deleted ")
        admin_main()
    else:    
        admin_main()
def delete_cabadmin():
    print(''' 
            1:delete 
            2:admin menu
            ''')
    dc=int(input("enter your choice"))
    if dc==1:
        cabid=input(" enter the cab_id ")
        del1="DELETE FROM cabs where cab_id='"+cabid+"'"
        c.execute(del1)
        conn.commit()
        admin_main()
    else:    
        admin_main()
    


    

def display_dealers():
    global cabdealer_id
    global admin_id
    #global admin_id
    print("{0:20}{1:20}{2:20}{3:20}".format("CAB DEALER ID ","CAB DEALER NAME","CAB DEALER EMAIL","CAB DEALER PHONE"))
    data="SELECT cabdealer_id,cabdealer_name,cabdealer_emailid,cabdealer_phone FROM cab_dealer"
    userdata=c.execute(data)
    d=userdata.fetchall()
    for a in d:
        print("{0:<20}{1:<20}{2:<20}{3:<20}".format(a[0],a[1],a[2],a[3]))
    
    
    dc=int(input(" enter 1: for delete  "))
    if dc==1:
        cabdealer_id=int(input(" enter cabdealer_id: "))
        deldata="DELETE  from cab_dealer where cabdealer_id='"+str(cabdealer_id)+"' "
        c.execute(deldata)
        conn.commit()
        print(" cab dealer deleted ")
        admin_main()
    else:    
        admin_main()

def dispaly_cabs():
    data="SELECT c.cab_id,c.cab_name,c.cab_type,c.cab_model,d.cabdealer_name,c.cab_from,c.cab_to  FROM cabs  as c inner join cab_dealer as d  on c.cab_dealerid = d.cabdealer_id "
    

    
   
        
    cabdata=c.execute(data)
    d=cabdata.fetchall()
    print("{0:20}{1:20}{2:20}{3:20}{4:20}{5:20}{6:20}".format("CAB ID ","CAB NAME","CAB TYPE","CAB MODEL","CAB DEALER NAME","CAB FROM","CAB TO"))
    for a in d:
        print("{0:<20}{1:<20}{2:<20}{3:<20}{4:<20}{5:<20}{6:<20}".format(a[0],a[1],a[2],a[3],a[4],a[5],a[6]))
    delete_cabadmin()
   
def changepassword_admin():
    global admin_id
    old_password=input(" ENTER THE old_password ")
    #new_password=input(" ENTER THE new_password ")
    data=c.execute("SELECT * FROM admin where admin_password='"+old_password+"' and admin_id='"+str(admin_id)+"'")
    d=data.fetchall()
    t=len(d)
    if t==1:
        new_password=input(" ENTER THE new_password ")
        confirm_password=input(" ENTER THE confirm_password ")
        if new_password==confirm_password:
            upd="update admin set admin_password='"+new_password+"' where admin_id= '"+str(admin_id)+"' "
            c.execute(upd)
            conn.commit()
            print("password updated ......... ")
            admin_main()
        else:   
            print(" new password and confirm password not matching ...... ")

    else:       
        print(" invalid old password ....")
        admin_main()

def admin_main():
    global admin_id
    global user_id
    print(''' 
            1 view all users
            2 view all cabs
            3 view all dealers
            4 change password 
            5 logout
            ''')
    dc=int(input(" enter your choice: "))
    if dc==1:
        display_user()
        
    elif dc==2:
        dispaly_cabs()
        delete_cabadmin()
        

        
    elif dc==3:
        display_dealers()
        

    elif dc==4:
        changepassword_admin()

        
    
    elif dc==5:
        #del admin_id
        print(" logout successfully...")
        main()






def main():
    print(''' 
              1  Dealer registration
              2  dealer login
              3  user registration
              4  user login
              5  admin login
              6  exit''')

    userc=int(input(" enter your choice "))
    if userc==1:
        dealer_reg()
    elif userc==2:
        dealer_log()
    elif userc==3:
        user_reg()
    elif userc==4:
        user_log()

       
    elif userc==5:
        admin_log()
    else:
        exit()
        
main()      




        
        




    
