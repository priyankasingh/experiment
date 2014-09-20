import praw
import MySQLdb
from MySQLdb import cursors

db =  MySQLdb.connect(
        host="localhost",
        user="root",
        passwd="Southampton11",
        db="Test")

cursor = db.cursor()

query = """SELECT id, post_id FROM red_posts WHERE id>19370  ORDER BY id ASC LIMIT 7010;"""

cursor.execute(query)
numrows = int(cursor.rowcount)

rows = cursor.fetchall()

for j in range (numrows):
	#print "id =", rows[j][0]
	post =rows[j][1]

	r = praw.Reddit('Comment')

	submission = r.get_submission(submission_id=post)
	submission.replace_more_comments(limit=None, threshold=0)
	c = praw.helpers.flatten_tree(submission.comments)

	for i in c:

		query2 = """INSERT IGNORE INTO red_comments 
                         (red_posts_id, comment_id, body, author, up_vote, down_vote, parent_id, post_id, subreddit, creation_date) 
                         VALUES ('%d', '%s', '%s', '%s', '%d', '%d', '%s', '%s', '%s', '%s');
                         """ % (rows[j][0], i.id, i.body, i.author, i.ups, i.downs, i.parent_id, i.link_id, i.subreddit, i.created_utc)
		try:

                	cursor.execute(query2)
                        db.commit()
#                        print "Insert Successful"

                except:
                	pass

#		print i.author
#		print "---------"
		#print i.body_html
#	print i.id
#	print i.author
#	print i.parent_id
#	print i.ups
#	print i.downs
#	print i.link_id
#	print i.subreddit
#	print i.created_utc
#	print "---------"
#	print "*************************"
