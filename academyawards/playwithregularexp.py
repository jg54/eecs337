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

entity = 'Hugh Jackman'
tallies = {}
count = 0
tweets = []

f = open('clearTweets.txt')
for tweet in f:
   if re.findall( 'best' ,tweet , re.M|re.I):
       tweets.append(tweet)
entities = loadFile('first46600entities.txt')
def tryEntities(ents,f):
    found = {}
    count = 0
    of = len(ents)
    for e in ents:
        
        print e + " " + str(count) + " of " + str(of)
        count = count + 1
        try:
            found[e] = findEntities(e,f)
            if (found[e]!=None):
                print found[e]
        except:
            print "DIDNT WORK"
    return found
            
        
def findEntities(e,f):
    #f = open('clearTweets.txt')
    count = 0
    for tweet in f:
        # this is the best reg exp for getting the winners
        if re.findall( e+'.(wins|won).best.(supporting)*.(actor|actress).in.*for.*#' ,tweet , re.M|re.I):
            count = count + 1
            #print(tweet)
            # Entity name
            #print e
            #Reward
            #print "Rewards"
            reward = find_between(re.findall(r'[\W]in.*for',tweet , re.M|re.I)[0], "in" , "for")
            #Movie
            #print "Movie"
            movie = find_between(re.findall(r'[\W]for.*#',tweet , re.M|re.I)[0], "for" , "#")
    if count:
        print e
        return [count,reward,movie]
        


    
    #if re.findall( r'(wins|won).*Best' ,tweet , re.M|re.I):
    #if re.findall( r'Lena Dunham.(wins|won).*Best.*for.*#' ,tweet , re.M|re.I):
    #if re.findall( r'Lena Dunham.(wins|won).Best.*actor in.*.for.(\"|\').*(\"|\')' ,tweet , re.M|re.I):

    #for nominees
    #if re.findall( r'I HOPE.*WINS' ,tweet , re.M|re.I):
        

