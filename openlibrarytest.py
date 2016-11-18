from urllib2 import urlopen
from json import load

apiurl = "http://openlibrary.org/api/get?key=/b/OL1001932M"

response = urlopen(apiurl)

json_obj = load(response)

dict_brkdwn = json_obj["result"]["subject_place"]

print json_obj
print dict_brkdwn


#http://openlibrary.org/search.json?subject=france
#http://openlibrary.org/search.json?q=france

# curl -G --data-urlencode 'query={"type":"\/type\/edition", "isbn_10":"0789312239"}' \
# http://openlibrary.org/api/things

# curl -G --data-urlencode 'query={/subjects/love.json?details=true}' \
# http://openlibrary.org/api/things

#curl http://openlibrary.org/api/get?key=/b/OL1001932M&prettyprint;=true