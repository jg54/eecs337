import pickle
with open('20000by50dump.txt','rb') as h:
	alldata = pickle.loads(h.read())
def sumEntities(data):
    entities={}
    for i in range(len(data)):
        x = data[i]["entities"]["results"]["entities"]
        if(type(x)==unicode):
            continue
        x = data[i]["entities"]["results"]["entities"]["entity"]
        if(isinstance(x,list)):
            for i in range(len(x)):
                if x[i]["text"] in entities.keys():
                    num = entities[x[i]["text"]]["count"]
                    entities[x[i]["text"]]["count"] = num + 1
                else:
                    entities[x[i]["text"]] = {}
                    entities[x[i]["text"]]["count"]=1
                    entities[x[i]["text"]]["type"]= x[i]["type"]

    return entities
