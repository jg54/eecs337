import re
import pickle

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

def loadFile(name):
    with open(name,'rb') as h:
        into = pickle.loads(h.read())
        return into

def trimData(f, twlist, entities): #trims up the data 
    copye = []
    for tweet in f:
       if re.findall( 'best' ,tweet , re.M|re.I):
           twlist.append(tweet)

    for i in entities:
        copye.append(i)
	
    for i in copye:
        if "(" in i or ")" in i or len(i)< 4 or re.match('^[a-z ]+$', i) is None:
            del entities[i] 

            
        
def findWinningActors(e,f):
    #f = open('clearTweets.txt')
    count = 0
    sample = {}
    movieType = ""
    mediaType = ""
    for tweet in f:
        # this is the best reg exp for getting the winners
        if re.findall( e+'.(wins|won).best.(supporting)* *(actor|actress).in.*for.*#' ,tweet , re.M|re.I):
            count = count + 1
            #print(tweet)
            # Entity name
            #print e
            #Reward
            #print "Rewards"
            reward = find_between(re.findall(r'[\W]in.*for',tweet , re.M|re.I)[0], "in" , "for")
            if re.findall(r'drama',tweet):
                movieType = "drama"
            elif re.findall(r'musical',tweet):
                movieType = "musical or comedy"
            if re.findall(r'series',tweet) and  not(re.findall(r'film',tweet)):
                mediaType = "TV series"
            elif re.findall(r'film',tweet):
                mediaType = "Film"
                
            #Movie
            #print "Movie"
            #movie = find_between(re.findall(r'[\W]for.*#',tweet , re.M|re.I)[0], "for" , "#")
            movie = re.findall(r'best.*for.*[A-Z][a-z]*',tweet , re.M|re.I)
            movie = re.findall(r'[A-Z][a-z]+',movie[0] , re.M)
            sample = tweet
    if count:
        moviestr = ""
        for i in movie:
            moviestr = moviestr + i + " "
        obj= {'count':count,'title':moviestr,'sample':sample,'genre':movieType,'media':mediaType}
        return obj
        


    
    #if re.findall( r'(wins|won).*Best' ,tweet , re.M|re.I):
    #if re.findall( r'Lena Dunham.(wins|won).*Best.*for.*#' ,tweet , re.M|re.I):
    #if re.findall( r'Lena Dunham.(wins|won).Best.*actor in.*.for.(\"|\').*(\"|\')' ,tweet , re.M|re.I):

    #for nominees
    #if re.findall( r'I HOPE.*WINS' ,tweet , re.M|re.I):
        

def findWinningMovies(e,f):
    #f = open('clearTweets.txt')
    count = 0
    sample = {}
    for tweet in f:
        # this is the best reg exp for getting the winners
        if re.findall( e+'.(wins|won).best.picture.*' ,tweet , re.M|re.I):
            count = count + 1
            sample = tweet
            #print(tweet)
            # Entity name
            #print e
    if count>50:
        #print(e)
        return [count,sample]
    
def findWinningSeries(e,f):
    #f = open('clearTweets.txt')
    count = 0
    sample = {}
    for tweet in f:
        # this is the best reg exp for getting the winners
        if re.findall( e+'.*(wins|won)*.best.*series.*' ,tweet , re.M|re.I):
            count = count + 1
            sample = tweet
            #print(tweet)
            # Entity name
            #print e
    if count:
        #print e
        return [count,sample]
        

def getNominees(e,f):
     #f = open('clearTweets.txt')
    count = 0
    sample = {}
    for tweet in f:
        # this is the best reg exp for getting nominees
        if re.findall( r'HOPE.'+e+'.WINS' ,tweet , re.M|re.I) or re.findall( e+'.*HOPE .* wins' ,tweet , re.M|re.I):
            count = count + 1
            sample = tweet
            #print(tweet)
            # Entity name
            #print e
    if count:
        #print e
        return [count,sample]

def getPresenters(e,f):
     #f = open('clearTweets.txt')
    count = 0
    sample = {}
    for tweet in f:
        # this is the best reg exp for getting nominees
        if re.findall( e+'.*(intro|ointroduced|introduces|introduce|inroducing|presenting|speach).*' ,tweet , re.M|re.I):
            count = count + 1
            sample = tweet
            #print(tweet)
            # Entity name
            #print e
    if count:
        #print e
        return [count,sample]
    
    
def runSearch():
    entity = 'Hugh Jackman'
    tallies = {}
    count = 0
    tweets = []
    entities = loadFile('allentities.txt')
    f = open('clearTweets.txt')

    trimData(f, tweets, entities)

    bestActors = []
    best 

    for i in entities:
        if ("Movie" == entities[i]["type"]) or ("Person" == entities[i]["type"]):
            temp = None
            
            count = count + 1
            try:
                temp = findWinningActors(i,tweets)
            except:
                continue
            if temp:
                if " " in i:
                print temp
                foundstuff.append(temp)
        else:
            try:
                temp = findWinningMovies(i,tweets)
            except:
                continue
            if temp:
                print temp
                foundstuff.append(temp)
    print ("Best Actors and Actresses: \n")
    print (findWinningActors(entity, tweets))
    print ("\n Best Movies: \n")
    print (findWinningMovies(entity, tweets))
    print ("\n Best Series: \n")
    print (findWinningSeries(entity, tweets))

    print ("\n Nominees: \n")
    print (getNominees(entity, tweets))

    print ("\n Presenters: \n")
    print (getPresenters(entity, tweets))
    return
    
    
# runSearch()
    
    

'''        
def tcwrapper(f,a,b):
    return f(a,b)
foundstuff = []
k = 0
print len(entities)
for i in entities:
    k= k + 1
    if ("Movie" == entities[i]["type"]) or ("Person" == entities[i]["type"]):
        temp = None
        try:
            temp = findWinningActors(i,tweets)
        except:
            continue
        if temp:
            if " " in i:
                print temp
                foundstuff.append(temp)
        else:
            try:
                temp = findWinningMovies(i,tweets)
            except:
                continue
            if temp:
                print temp
                foundstuff.append(temp)
    if (k%100==0):
        break
'''
