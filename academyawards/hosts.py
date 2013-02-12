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

entities = loadFile('first46600entities.txt')    
tweets = []
count = 0

f = open('clearTweets.txt')
'''
for tweet in f:
   if re.findall( 'actress' ,tweet , re.M|re.I):
       if re.findall( 'have won' ,tweet , re.M|re.I):
           tweets.append(tweet)
'''

'''
for tweet in tweets:
    for ent in entities:
        try:
            if re.findall( ent ,tweet , re.M|re.I):
                print ent
        except:
            count = count
'''

hosts = {}
vote = 0
firsthost = ''
secondhost = ''
tweet1 = ''
tweet2 = ''

for tweet in f:
    if re.findall( 'hosts.*and.*#' ,tweet , re.M|re.I):
        try:
            host1 = find_between(re.findall(r'[\W]hosts.*and',tweet , re.M|re.I)[0], "hosts" , "and")
            host2 = find_between(re.findall(r'[\W]and.*#',tweet , re.M|re.I)[0], "and" , "#")
            
            host1 = host1.replace('#', '')
            host1 = host1.replace('?', '')
            host1 = host1.replace('!', '')
            host1 = host1.replace('.', '')
            host2 = host2.replace('#', '')
            host2 = host2.replace('?', '')
            host2 = host2.replace('!', '')
            host2 = host2.replace('.', '')
            
            if host1 in hosts:
                hosts[host1] = hosts[host1] + 1
                if hosts[host1] > 6:
                    tweet1 = tweet                 
            else:
                hosts[host1] = 1
            if host2 in hosts:
                hosts[host2] = hosts[host2] + 1
            else:
                hosts[host2] = 1
        except:
            continue
    if re.findall( '(watch|watching).*and.*host' ,tweet , re.M|re.I):
        try:
            host1 = find_between(re.findall(r'[\W]watch.*and',tweet , re.M|re.I)[0], "watch" , "and")
            host2 = find_between(re.findall(r'[\W]and.*host',tweet , re.M|re.I)[0], "and" , "host")

            host1 = host1.replace('#', '')
            host1 = host1.replace('?', '')
            host1 = host1.replace('!', '')
            host1 = host1.replace('.', '')
            host2 = host2.replace('#', '')
            host2 = host2.replace('?', '')
            host2 = host2.replace('!', '')
            host2 = host2.replace('.', '')

            if host1 in hosts:
                hosts[host1] = hosts[host1] + 1
                if hosts[host2] > 6:
                    tweet2 = tweet
            else:
                hosts[host1] = 1
            if host2 in hosts:
                hosts[host2] = hosts[host2] + 1
            else:
                hosts[host2] = 1
        except:
            continue

for host in hosts:
    if hosts[host] > vote and host != '':
        secondhost = firsthost
        firsthost = host
        vote = hosts[host]


print firsthost
print secondhost
print tweet1
print tweet2


