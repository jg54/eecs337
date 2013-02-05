import re
import json
import unicodedata
import AlchemyAPI

# Create an AlchemyAPI object.
alchemyObj = AlchemyAPI.AlchemyAPI()
# Load the API key from disk.
alchemyObj.loadAPIKey("api_key.txt")

d=['c']*301
chunk =""
name = "Ben Affleck"


with open('goldenglobes.json') as f:
    for i in range(300):
        d[i]= json.loads(f.readline())
        if re.findall(r''+name+' won Best ',d[i]["text"] ,re.M|re.I):
            try:
                chunk=chunk+unicodedata.normalize('NFKD',d[i]["text"]).encode('ascii','ignore')+" "
            except:
                chunk=chunk+d[i]["text"]+" "
             
print chunk
#print alchemyObj.TextGetRankedKeywords(chunk)







        
        
