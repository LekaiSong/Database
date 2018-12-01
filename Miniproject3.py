#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Author - Lekai Song
import mysql_db as mysql_db
import mongo_db as mongo_db
import mysql.connector

def get_input_num():
    num=None
    while num is None:
        try:
            num = int(input("Enter a number: "))
        except ValueError:
            print("ERROR: Enter a NUMBER please! ")
    return num

MYSQL=1
def main():
#if __name__ == '__main__':
    while(1):
        mydb = mysql.connector.connect(host="localhost",user="root",passwd="")
        mycursor = mydb.cursor()
        mycursor.execute("CREATE DATABASE IF NOT EXISTS mini3")
        mycursor.execute("use mini3")
        mycursor.execute("CREATE TABLE IF NOT EXISTS mini3_db(id INT AUTO_INCREMENT PRIMARY KEY,username VARCHAR(255), img_num VARCHAR(255),description VARCHAR(255),description_num VARCHAR(255))")
        mycursor.execute("use mini3")
        print("------------------------------------------------")
        print("Menu:\n1.Query new username\n2.Query existed username\n3.See full database \n4.Delete database\n5.Search for a word\n6.Exit")
        data=get_input_num();
        
        if (data==1):
            #add to both db, after google_analysis
            mysql_db.add_user(mycursor)
            
        elif(data==2):
            print("Which database to query:\n1.MySQL\n2.MongoDB")
            db = get_input_num()
            if (db==MYSQL):
                mysql_db.query_user(mycursor)
            else:
                mongo_db.query_user()

        elif(data==3):
            print("Which database to query:\n1.MySQL\n2.MongoDB")
            db = get_input_num()
            if (db==MYSQL):
                mysql_db.print_db(mycursor)
            else:
                mongo_db.print_db()
                
        elif(data==4):
            #delete always both db
            mysql_db.delete_db(mycursor)
            mongo_db.delete_db()
            
        elif(data==5):
            print("Which database to query:\n1.MySQL\n2.MongoDB")
            db = get_input_num()
            if (db==MYSQL):
                mysql_db.search_word(mycursor)
            else:
                mongo_db.search_word()

        elif(data==6):
            return

main()
