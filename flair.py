import praw
import MySQLdb
from MySQLdb import cursors

db =  MySQLdb.connect(
        host="localhost",
        user="root",
        passwd="Southampton11",
        db="Test")

cursor = db.cursor()

query = """SELECT post_id FROM red_posts  ORDER BY id ASC;"""

cursor.execute(query)
numrows = int(cursor.rowcount)

rows = cursor.fetchall()

for j in range (numrows):
        #print "id =", rows[j][0]
        post = rows[j][0] 
	r = praw.Reddit('Flair')

        s = r.get_submission(submission_id=post)
#	print s.link_flair_text 
        
	query2 = """UPDATE red_posts SET 
		 flair = '%s', up_vote = '%d', down_vote = '%d', score = '%d'
                 WHERE post_id = '%s'
		 """ % (s.link_flair_text, s.ups, s.downs, s.score, s.id)
	try:

		cursor.execute(query2)
		db.commit()
                #print "Update Successful"
	
	except:
		pass
