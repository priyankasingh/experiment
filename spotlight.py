import urllib, urllib2
import MySQLdb

db =  MySQLdb.connect(
        host="localhost",
        user="root",
        passwd="Southampton11",
        db="Test")

cursor = db.cursor()

query = """SELECT body, post_id FROM red_posts WHERE id > 7746;"""

cursor.execute(query)
numrows = int(cursor.rowcount)

rows = cursor.fetchall()
post = rows[0]

for i in range (numrows):
	
	postid = rows[i][1]
	#print post
	#text = rows[i][0]
	text2 = urllib.quote(rows[i][0])

	url = "http://spotlight.dbpedia.org/rest/annotate/"
	#data = rows[i][0]
	
	data = "disambiguator=Document&confidence=0.2&support=20&text=" + text2

	#A Dictionary of Algorithms and Data Structures"
	headers = { "Accept" : "application/rdf+xml", "content-Type" : "application/x-www-form-urlencoded"}
        try:
 
		req = urllib2.Request(url, data, headers)
		response = urllib2.urlopen(req)
		page = response.read()
		#print page
		#print "*******************************"

		query2 = """UPDATE red_posts SET 
                	 body_annotation = '%s' WHERE post_id = '%s'
                 	 """ % (page, postid)
        	try:

                	cursor.execute(query2)
                	db.commit()
                	#print "Update Successful"

        	except:
                	pass
	except:
		pass
