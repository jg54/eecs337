import json
import unicodedata
import AlchemyAPI
import xmltodict
import pickle
from nltk import pos_tag, word_tokenize


# Create an AlchemyAPI object.
alchemyObj = AlchemyAPI.AlchemyAPI()
# Load the API key from disk.
alchemyObj.loadAPIKey("api_key.txt")


d=[]
alldata = []
Names={}
chunk=""
with open('goldenglobes.json') as f:
    for i in range(20000):
        d= json.loads(f.readline())
        try:
            chunk=chunk+unicodedata.normalize('NFKD',d["text"]).encode('ascii','ignore')+" "
        except:
            chunk=chunk+d["text"]+" "
        if (i % 50 ==0):
            data = {}
            data["text"] = chunk
            try:
                data["keywords"] = xmltodict.parse(alchemyObj.TextGetRankedKeywords(chunk))
                data["entities"] = xmltodict.parse(alchemyObj.TextGetRankedNamedEntities(chunk))
                alldata.append(data);
                #with open("Entities.txt", "w") as text_file:
                    #text_file.write(alchemyObj.TextGetRankedNamedEntities(chunk))
            except:
                continue
            chunk = ""
        #d[i]["text"]=unicodedata.normalize('NFKD', d[i]["text"]).encode('ascii','ignore')
'''       
with open('1000by50dump.txt','wb') as h:
	pickle.dump(alldata,h)
with open('1000by50dump.txt','rb') as h:
	k = pickle.loads(h.read())
k==alldata
'''
