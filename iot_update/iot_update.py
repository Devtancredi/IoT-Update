#Frank Tancredi 3/05/2019                   
                           
#IoT_Update is a program designed to be used in a terminal startup macro to alert the user when a new episode of the BBC4 podcast "Within Our Time" has been released                                                              

import bs4 as bs
import urllib
 
source = urllib.urlopen('https://www.bbc.co.uk/programmes/b006qykl/episodes/player').read() #Obtain HTML of BBC webpage
soup = bs.BeautifulSoup(source,'lxml')

episodeIterators = []  
episodeBlock = soup.find_all('span', {"class":"programme__title gamma"}) #Create a string block of the html within <span> tags
                                                                          #of type "programme__title gamma"
descriptionBlock = soup.find_all('p', {"class":"programme__synopsis text--subtle centi"}) #Create a string block of the html
                                                                          #within <span> of the type "programme...etc

oldEpisodeFile = open('EpisodeList.txt','r')
oldEpisodes = oldEpisodeFile.read().split("\n") #create a list of episodes already seen to compare against current webpage
 
for c in range(0,len(episodeBlock)): #For every episode on the webpage
    inList = False
    for d in range (0,len(oldEpisodes)): #For every episode listed in the text file
        if episodeBlock[c].span.text == oldEpisodes[d]:
            inList = True
    if inList == False: #If there exists an episode on the webpage that does not exist in the episode cache
        #episodes.append(episodeBlocks[c].span.text + "\n")
        EpisodeList = open("EpisodeList.txt", 'a')
        EpisodeList.write(episodeBlock[c].span.text + "\n") #Write this episode to the cache
        episodeIterators.append(c)
        #print("There's a new episode of Within Our Time out: " + episodeBlocks[c].span.text)

if len(episodeIterators) == 1:
    print "There is " + str(len(episodeIterators)) + " new episode of Within Our Time:\n\n" + episodeBlock[episodeIterators[0]].span.text + ": " + descriptionBlock[episodeIterators[0]].span.text +"\n"
elif len(episodeIterators) > 1:
    print "There are " + str(len(episodeIterators)) + " new episodes of Within Our Time:\n"
    for e in range (0,len(episodeIterators)):
        print episodeBlock[episodeIterators[e]].span.text + ": " + descriptionBlock[episodeIterators[e]].span.text +"\n"
