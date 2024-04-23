'''Requires mysql.connector
change passwd from 'abhishek' to the password set on the device on which it will be used.
tables and database will be created automatically as i have provided the commands in the code
'''



import mysql.connector as ms
conobj=ms.connect(host='localhost',user='root',passwd='abhishek')
q='create database if not exists Palweb'
curobj=conobj.cursor()
curobj.execute(q)
ub='use Palweb'
curobj.execute(ub)
quet="create table if not exists queries(query varchar(100),Reply varchar(100))"
curobj.execute(quet)
d="create database if not exists links"
curobj.execute(d)
dlink="create table if not exists links(links varchar(100))"
curobj.execute(dlink)
conobj.commit()
conobj.close()

def writequery():
    #import mysql.connector as ms
    conobj=ms.connect(host='localhost',user='root',passwd='abhishek',database='Palweb')
    curobj=conobj.cursor()
    query=input("Enter your query")
    q="insert into queries(query) values('{}')".format(query)
    curobj.execute(q)
    print("Query submitted successfully")
    conobj.commit()
    conobj.close()


def readqueries():
    conobj=ms.connect(host='localhost',user='root',passwd='abhishek',database='Palweb')
    curobj=conobj.cursor()
    q='select * from queries'
    curobj.execute(q)
    data=curobj.fetchall()
    for i in data:
        print('Query:',i[0],'Reply:',i[1])
    conobj.commit()
    conobj.close()


def replyqueries():
    conobj=ms.connect(host='localhost',user='root',passwd='abhishek',database='Palweb')
    curobj=conobj.cursor()
    q='select * from queries'
    curobj.execute(q)
    data=curobj.fetchall()
    for i in data:
        if i[0]!=None and i[1] is None:
            print(i[0])
            rpl=input("Enter your reply")
            updatereply="update queries set reply='{}' where query='{}'".format(rpl,i[0])
            curobj.execute(updatereply)
    conobj.commit()
    conobj.close()

def writelinks():
    #import mysql.connector as ms
    conobj=ms.connect(host='localhost',user='root',passwd='abhishek',database='Palweb')
    curobj=conobj.cursor()
    link=input("add a link")
    q="insert into links(links) values('{}')".format(link)
    curobj.execute(q)
    print("link added  successfully")
    conobj.commit()
    conobj.close()
    
def readlinks():
    conobj=ms.connect(host='localhost',user='root',passwd='abhishek',database='Palweb')
    curobj=conobj.cursor()
    q='select * from links'
    curobj.execute(q)
    data=curobj.fetchall()
    for i in data:
        print('Links:',i[0])
    conobj.commit()
    conobj.close()


while True:
    print("Menu\n1.Write a query\n2.Read a query\n3.Reply a query\n4.Add a link\n5.View existing links\n6.Exit")
    ch=int(input("Enter choice"))
    if ch==1:
        writequery()
    elif ch==2:
        readqueries()
    elif ch==3:
        replyqueries()
    elif ch==4:
        writelinks()
    elif ch==5:
        readlinks()
    elif ch==6:
        break
print("Exited from menu")
      
    
    
    
