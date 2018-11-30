# Database
### EC601-Miniproject3

### 1. Goal
### Based on Miniproject 1, do two database implementations with MySQL and MongoDB.
The main requirements:<br>
>1.1 Detail information of every transaction the user may run using your system.<br>
>1.2 Store all relevant information for everytime a user uses your application.<br>
>1.3 Add API and develop test program to <br>
>>1.3.1 Search for certain words and retrieve which user/session that has this work in it.  <br> 
>>>For example, search for ‘basketball”, and get results of which user had Basketball in their sessions. <br>

>>1.3.2 Collective statistics about overall usage of the system.  <br> 
>>>For example, Number of images per feed & Most popular descriptors

### 2.Preparation
Install both mysql and mongo database.
https://www.mysql.com/downloads/
https://www.mongodb.com
![mysql](https://github.com/LekaiSong/Database/blob/master/result/mysql.png)
![mongo](https://github.com/LekaiSong/Database/blob/master/result/mongo.png)

### 3. Run
#### 'python Miniproject3.py' and then follow the instructions.

### 4. Result
#### When running the project, the database is empty. <br> Add a new username named 'maroon5' for example. <br> Then tweets(images) are being downloaded. ![tweets](https://github.com/LekaiSong/Database/blob/master/result/3.png)
#### Then convert these images into a video. ![video](https://github.com/LekaiSong/Database/blob/master/result/4.png)
#### Analyze the video and give it labels. ![labels](https://github.com/LekaiSong/Database/blob/master/result/5.png)
#### Also add 'nba' and 'boston' as well.
#### Now see the full database. ![full](https://github.com/LekaiSong/Database/blob/master/result/9.png)
#### And we can query a existed username and see details about it. If searching a keyword, username that contains it will be displayed. ![keyword_stage](https://github.com/LekaiSong/Database/blob/master/result/10.png) ![keyword_basketball](https://github.com/LekaiSong/Database/blob/master/result/11.png)
