import urllib, urllib2
import MySQLdb
import cgi

db =  MySQLdb.connect(
        host="localhost",
        user="root",
        passwd="Southampton11",
        db="Test")

cursor = db.cursor()

query = """SELECT body, comment_id FROM red_comments WHERE id > 392826;"""

cursor.execute(query)
numrows = int(cursor.rowcount)

rows = cursor.fetchall()
post = rows[0]

for i in range (numrows):

        commentid = rows[i][1]
        #print post
        #text = cgi.escape(rows[i][0], True)
        text2 = urllib.quote(rows[i][0])
#	print text2

        url = "http://spotlight.dbpedia.org/rest/annotate/"

        data = "disambiguator=Document&confidence=0.2&support=20&text=" + text2

        headers = { "Accept" : "application/rdf+xml", "content-Type" : "application/x-www-form-urlencoded"}
        try:

                req = urllib2.Request(url, data, headers)
                response = urllib2.urlopen(req)
                page = response.read()
                #print page
                #print "*******************************"
		
		query2 = """UPDATE red_comments SET 
                         body_annotation = '%s' WHERE comment_id = '%s'
                         """ % (page, commentid)
                try:

                        cursor.execute(query2)
                        db.commit()
                        #print "Update Successful"

                except:
                        pass
        except:
                pass
