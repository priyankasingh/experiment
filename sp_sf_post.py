import urllib, urllib2
import MySQLdb
#import cgi

db =  MySQLdb.connect(
        host="localhost",
        user="root",
        passwd="Southampton11",
        db="Test")

cursor = db.cursor()
#cursor2 = db.cursor()

query = """SELECT body, id FROM sof_posts where id >1058604 LIMIT 5000;"""

cursor.execute(query)
numrows = int(cursor.rowcount)

rows = cursor.fetchall()
#post = rows[0]

for i in range (numrows):

        pid = rows[i][1]
        print pid
        #text = cgi.escape(rows[i][0], True)
        text2 = urllib.quote(rows[i][0])
        #print text2

        url = "http://spotlight.dbpedia.org/rest/annotate/"

        data = "disambiguator=Document&confidence=0&support=0&text=" + text2

        headers = { "Accept" : "application/rdf+xml", "content-Type" : "application/x-www-form-urlencoded"}
        try:

                req = urllib2.Request(url, data, headers)
                response = urllib2.urlopen(req)
                page = response.read()
                #print page
                #print "*******************************"

                query2 = """UPDATE sof_posts SET 
                         body_annotation = '%s' WHERE id = '%s'
                         """ %  (page, pid)
                try:
			cursor.execute(query2)
			#print "a"
                	db.commit()
                	print "Update Successful"

		except:
			pass

        except:
                pass
