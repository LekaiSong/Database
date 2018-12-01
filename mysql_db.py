#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import get_images as get_images
import convert_to_video as convert_to_video
import google_analysis as google_analysis

def query_user(mycursor):
    screen_name =input("Enter a username to query: ")
    mycursor.execute("SELECT * FROM mini3_db WHERE username='"+screen_name+"'")
    myresult = mycursor.fetchall()
    if (len(myresult)==0):
        print("There is NO such a username")
    else:
        for user in myresult:
            username=user[1]
            img_num=user[2]
            description=user[3]
            description_num=user[4]
            print("username=%s,image_num=%s,description=%s,description_num=%s") % \
            (username,img_num,description,description_num)

def print_db(mycursor):
    mycursor.execute(("SELECT * FROM mini3_db"))
    myresult = mycursor.fetchall()
    print("There are",len(myresult),"user(s) at database")
    print("The current database is ")
    avg_im=0
    descrip=[]
    for user in myresult:
        avg_im=avg_im+int(user[2])
        curr_des=user[3].split(',')
        for j in curr_des:
            descrip.append(j)
        print(user)
    if (len(myresult)>0):
        print("Some statistics:")
        print("The most popular description is",(max(set(descrip), key = descrip.count)))
        print("There is an average of",str(avg_im/len(myresult)),"images per feed")
    return

def delete_db(mycursor):
    mycursor.execute("truncate mini3_db;")
    return

def search_word(mycursor):
    word=input("Enter a word to search: ")
    mycursor.execute(("SELECT * FROM mini3_db"))
    myresult = mycursor.fetchall()
    print("The next user has the word",word,"in their description:")
    for user in myresult:
        descrip=user[3]
        descrip=descrip.split(',')
        if word in descrip:
            print(user[1])

def add_user(mycursor):
    screen_name =input("Enter a username: ")
    image_num =input("Enter the amount of images to be downloaded: ")
    mycursor.execute("SELECT * FROM mini3_db WHERE username='"+screen_name+"'")
    myresult = mycursor.fetchall()
    if (len(myresult)!=0):
        print("Username already existed")
        return
    print(screen_name)
    print("-------------------------------------")
    print("downloading images from twitter feed " + screen_name)
    print("-------------------------------------")
    get_images.get_all_tweets(screen_name,image_num)
    print("-------------------------------------")
    print("creating video from",int(image_num),"images")
    print("-------------------------------------")
    convert_to_video.convert_to_video(screen_name)
    print("-------------------------------------")
    print("analyzing video")
    print("-------------------------------------")
    google_analysis.google_analyze(screen_name,image_num)
    return
