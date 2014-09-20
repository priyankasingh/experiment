import praw

r = praw.Reddit(user_agent='getposts')
submissions = r.get_subreddit('programming').get_top_from_year(limit=3)

for i in submissions:
#	com = praw.helpers.flatten_tree(i.get_comments(limit=None))
	com = i.get_comments()
	print i.title
	print '---------'

	for j in com:
		print j.body
		print '-------------------'

