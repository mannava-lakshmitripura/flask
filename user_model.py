import mysql.connector,json
from flask import make_response
class user_model():
    def __init__(self):
        try:
            con=mysql.connector.connect(host="localhost",user="root",password="mannava@4598",database="flask_tutorial")
            cur=con.cursor(dictionary=True)
            
            print("connection successful")
        except:
            print("some error")    
    
    def user_getall_model():
        con=mysql.connector.connect(host="localhost",user="root",password="mannava@4598",database="flask_tutorial")
        cur=con.cursor(dictionary=True)
        
        cur.execute("SELECT * FROM users")
        result=cur.fetchall()
        if len(result)>0:
            return make_response({"payload":result},200)
        else:
            return make_response({"message":"User not found"},204)
        
        
    def user_addone_model(data):
        con=mysql.connector.connect(host="localhost",user="root",password="mannava@4598",database="flask_tutorial")
        cur=con.cursor(dictionary=True)
        con.autocommit=True
        # print(data['email'])
        
        cur.execute(f"INSERT INTO users(name,email,phone,role,password) VALUES('{data['name']}','{data['email']}','{data['phone']}','{data['role']}','{data['password']}')")
        return make_response({"message":"Data Inserted Successfully"},201)
    
    def user_update_model(data):
        con=mysql.connector.connect(host="localhost",user="root",password="mannava@4598",database="flask_tutorial")
        cur=con.cursor(dictionary=True)
        con.autocommit=True
        
        cur.execute(f"UPDATE users SET name='{data['name']}',email='{data['email']}',phone='{data['phone']}',role='{data['role']}',password='{data['password']}' WHERE id={data['id']}")
        if cur.rowcount>0:
            return make_response({"message":"Updated successfully"},201)
        else:
            
            return make_response({"message":"no data found"},204)
        
    def user_delete_model(id):
        con=mysql.connector.connect(host="localhost",user="root",password="mannava@4598",database="flask_tutorial")
        cur=con.cursor(dictionary=True)
        con.autocommit=True
        
        cur.execute(f"DELETE FROM users WHERE id={id}")
        if cur.rowcount>0:
            return make_response({"message":"Deleted successfully"},201)
        else:
            
            return make_response({"message":"no data found"},204)   
        
    def user_patch_model(data,id):
        con=mysql.connector.connect(host="localhost",user="root",password="mannava@4598",database="flask_tutorial")
        cur=con.cursor(dictionary=True)
        con.autocommit=True
        qry="UPDATE users SET"
        for key in data:
            qry+=f"{key}='{data[key]}', "
        qry = qry[:-2] + f"  where id={id}"  
        # return qry
        cur.execute(qry)
        if cur.rowcount>0:
            return make_response({"message":"Updated successfully"},201)
        else:
            
            return make_response({"message":"no data found"},204)     
        
                                                                      