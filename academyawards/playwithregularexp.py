import re

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""



entity = 'Hugh Jackman'

f = open('clearTweets.txt')
for tweet in f:
    # this is the best reg exp for getting the winners
    if re.findall( entity+'.(wins|won).best.(actor|actress).in.*for.*#' ,tweet , re.M|re.I):
        print(tweet)
        # Entity name
        print entity
        #Reward
        print "Rewards"
        print find_between(re.findall(r'[\W]in.*for',tweet , re.M|re.I)[0], "in" , "for")
        #Movie
        print "Movie"
        print find_between(re.findall(r'[\W]for.*#',tweet , re.M|re.I)[0], "for" , "#")
        


    
    #if re.findall( r'(wins|won).*Best' ,tweet , re.M|re.I):
    #if re.findall( r'Lena Dunham.(wins|won).*Best.*for.*#' ,tweet , re.M|re.I):
    #if re.findall( r'Lena Dunham.(wins|won).Best.*actor in.*.for.(\"|\').*(\"|\')' ,tweet , re.M|re.I):

    #for nominees
    #if re.findall( r'I HOPE.*WINS' ,tweet , re.M|re.I):
        

