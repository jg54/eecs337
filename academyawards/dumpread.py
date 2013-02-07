import pickle
def loadFile(name):
    with open(name,'rb') as h:
        into = pickle.loads(h.read())
        return into
def saveFile(name,data):
    with open(name,'wb') as h:
	pickle.dump(data,h)
def sumEntities(data):
    entities={}
    for i in range(len(data)):
        x = data[i]["entities"]["results"]["entities"]
        if(type(x)==unicode):
            continue
        x = data[i]["entities"]["results"]["entities"]["entity"]
        if(isinstance(x,list)):
            for i in range(len(x)):
                tag = x[i]["text"].lower()
                if tag in entities.keys():
                    num = entities[tag]["count"]
                    entities[tag]["count"] = num + 1
                else:
                    entities[tag] = {}
                    entities[tag]["count"]=1
                    entities[tag]["type"]= x[i]["type"]
                    if "disambiguated" in x[i].keys():
                        entities[tag]["disambiguated"]= x[i]["disambiguated"]

    return entities

def combineEntityDicts(x,y):
    
