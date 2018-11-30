#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pymongo

def query_user():
    screen_name =input("Enter a username to query: ")
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mini3"]
    mycol = mydb["users"]
    
    if (mycol.count()==0):
        print("There is NO such a username")
    else:
        for user in mycol.find():
            if (user.get('username')==screen_name):
                print(user)

def print_db():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mini3"]
    mycol = mydb["users"]
    print("There are",mycol.count(),"user(s) at database")
    print("The current data base is :")
    avg_im=0
    descrip=[]
    for user in mycol.find():
        print(user)
        avg_im=avg_im+int(user.get('img_num'))
        curr_des=user.get('description').split(',')
        for j in curr_des:
            descrip.append(j)
    if (mycol.count()>0):
        print("Some statistics:")
        print("The most popular description is",(max(set(descrip), key = descrip.count)))
        print("There is an average of",str(avg_im/mycol.count()),"images per feed")
    return

def delete_db():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mini3"]
    mycol = mydb["users"]
    mycol.delete_many({})
    return

def search_word():
    word=input("Enter a word to search: ")
    print("The next user has the word",word,"in their description:")
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mini3"]
    mycol = mydb["users"]
    for user in mycol.find():
        descrip=user.get('description')
        descrip=descrip.split(',')
        if word in descrip:
            print(user.get('username'))

