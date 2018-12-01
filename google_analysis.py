#!/usr/bin/env python
import os
import io
from google.cloud import videointelligence
import mysql.connector
import pymongo

#must pip install google-cloud-videointelligence
def google_analyze(screen_name,image_num):
    #ap = argparse.ArgumentParser()
    #ap.add_argument("-u", "--user", required=True, help="user you're interested in")
    #ap.add_argument("-i", "--images", required=True, help="amount of images you want to download")
    #args = vars(ap.parse_args())

    #https://cloud.google.com/video-intelligence/docs/analyze-labels#video_analyze_labels-python
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=os.getcwd()+'/google.json'
    video_client = videointelligence.VideoIntelligenceServiceClient()
    features = [videointelligence.enums.Feature.LABEL_DETECTION]

    with io.open(os.path.join(os.getcwd(),""+screen_name+".mp4"),'rb')as movie:
        input_content = movie.read()

    operation = video_client.annotate_video(features=features, input_content=input_content)
    print('\nProcessing video for label annotations:')

    result = operation.result(timeout=90)
    print('\nFinished processing.')

    # Process video/segment level label annotations
    descrip=""
    count=0
    segment_labels = result.annotation_results[0].segment_label_annotations
    for i, segment_label in enumerate(segment_labels):
        print('Video label description: {}'.format(segment_label.entity.description))
        descrip=descrip+ segment_label.entity.description+","
        count+=1
        for category_entity in segment_label.category_entities:
            print('\tLabel category description: {}'.format(category_entity.description))

        #show the matching degree
        for i, segment in enumerate(segment_label.segments):
            confidence = segment.confidence
            print('\tConfidence: {}'.format(confidence))
            print('\n')


    #insert to database table
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="")
    mycursor = mydb.cursor()
    mycursor.execute("use mini3")
    sql = "INSERT INTO mini3_db(username,img_num,description,description_num) VALUES (%s,%s,%s,%s)"
    values = (screen_name,image_num,descrip,count)
    descrip = descrip[:-1]
    mycursor.execute(sql,values)
    mydb.commit()
    #try:
    #   mycursor.execute(sql,val)
    #   mydb.commit()
    #except:
    #   # Rollback in case there is any error
    #   mydb.rollback()

    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mini3"]
    mycol = mydb["users"]
    mydict = { "username": screen_name, "img_num": image_num,"description":descrip,"description_num":count }
    mycol.insert_one(mydict)
