#!/usr/bin/python
# -*- coding: utf-8 -*-

import praw
import MySQLdb
from MySQLdb import cursors

def keep_log(str):
        str = str.encode('utf-8')
        file = open("red_comments_log.txt","a")
        file.write(str)
        file.write("\n")
        file.close()

db =  MySQLdb.connect(
        host="localhost",
        user="root",
        passwd="Southampton11",
        db="Test")

cursor = db.cursor()

query = """SELECT id, post_id FROM red_posts LIMIT 10;"""

try:
        cursor.execute(query)
        numrows = int(cursor.rowcount)

        rows = cursor.fetchall()

        for j in range (numrows):
#        row = cursor.fetchone()
        	print row[0],row[1]
		pid = row[j]
		print pid		
		r = praw.Reddit('Comment')

                submission = r.get_submission(submission_id=pid)
                submission.replace_more_comments(limit=None, threshold=0)
                c = praw.helpers.flatten_tree(submission.comments)

                for i in c:

                        print i.body_html
                        print i.id
                        print i.author
                        print i.parent_id
                        print i.ups
                        print i.downs
                        print i.link_id
                        print i.subreddit
                        print i.created_utc
                        print "---------"
        
except:
	pass

def get_comments(url):
        print url
        try:
		r = praw.Reddit('Comment')

		submission = r.get_submission(submission_id=url)
		submission.replace_more_comments(limit=None, threshold=0)
		c = praw.helpers.flatten_tree(submission.comments)

		for i in c:

        		print i.body_html
        		print i.id
        		print i.author
        		print i.parent_id
        		print i.ups
        		print i.downs
        		print i.link_id
        		print i.subreddit
        		print i.created_utc
        		print "---------"
	except:
                pass

        return
