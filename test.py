#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb
import praw

def keep_log(str):
        str = str.encode('utf-8')
        file = open("red_posts_log.txt","a")
        file.write(str)
        file.write("\n")
        file.close()

db =  MySQLdb.connect(
        host="localhost",
        user="root",
        passwd="Southampton11",
        db="Test")

cursor = db.cursor()

r = praw.Reddit(user_agent='getposts')
submission = r.get_subreddit('webdev').get_top_from_year(limit=1000)
for i in submission:
	query = """INSERT IGNORE INTO red_posts
		(post_id, title, body, author, up_vote, down_vote, score, permalink, url, creation_date, subreddit)
		VALUES ('%s', '%s', '%s', '%s', '%d', '%d', '%d', '%s', '%s', '%s', '%s')
		ON DUPLICATE KEY UPDATE up_vote = '%d', down_vote = '%d', score = '%d' ;
		""" % (i.id, i.title, i.selftext_html, i.author, i.ups, i.downs, i.score, i.permalink, i.url, i.created, i.subreddit, i.ups, i.downs, i.score)

	try:
		cursor.execute(query)
                db.commit()
		#print "Insert Successful"

	except:
		 pass
		 keep_log(i.title)   
#	print i.id
#	print i.title
#	print i.author
##	print i.url
#	print i.permalink
#	print i.ups
#	print i.downs
#	print i.created
#	print i.selftext_html
#	print i.score
