import re

entity = 'Damien Lewis'

f = open('clearTweets.txt')
for tweet in f:
    # this is the best reg exp for getting the winners
    if re.findall( entity+'.(wins|won).best.(actor|actress).in.*for.*#' ,tweet , re.M|re.I):
        print(tweet)


    
    #if re.findall( r'(wins|won).*Best' ,tweet , re.M|re.I):
    #if re.findall( r'Lena Dunham.(wins|won).*Best.*for.*#' ,tweet , re.M|re.I):
    #if re.findall( r'Lena Dunham.(wins|won).Best.*actor in.*.for.(\"|\').*(\"|\')' ,tweet , re.M|re.I):

    #for nominees
    #if re.findall( r'I HOPE.*WINS' ,tweet , re.M|re.I):
        
