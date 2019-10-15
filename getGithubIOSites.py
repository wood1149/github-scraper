# alternate method for just scraping i/o sites
import requests
import glob
import time
import random
from random import shuffle


# this is not an exhaustive list of functions, will need to add to/refactor architecture of module depending on how we want to implement file access and reading


def readInUsernames():
    usernames = set()

    #walk through username directory
    for file in glob.glob("./usernames/*.txt"):
        print("reading " + str(file))
        with open(file,"r") as datafile:
            for user in datafile:
                usernames.add(user)

    print("found, " + str(len(usernames)) + " usernames")
    return usernames

def getAlreadyScrapedUsers():
    usernames = set()

    #walk through username directory
    for file in glob.glob("./githubIOSites/*.html"):
        #if("invalid" not in file.lower()):
        usernames.add(file.split("_")[0])
        #print("Foudn " + str(file.split("_")[0]))
    return usernames

def requestIOSite(username):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    url = 'https://'+username.strip()+'.github.io'
    print(username)
    print("\t" + url)
    response = requests.get(url,headers=headers)
    if(response.status_code == 200):
        #valid site
        print("\t(res): VALID")
        return response.content
        
    else:
        print("\t(res): " + str(response.status_code))
        return False

if __name__ == '__main__':
    userSet = readInUsernames()
    listOfUsernames = getAlreadyScrapedUsers()
    print("Scraped " + str(len(listOfUsernames))+ " previously")
    #gets users in a different order
    #random.shuffe(userSet)
    userSet = random.sample(userSet,len(userSet))

   
    #scrapes each user
    scrapecount = 0
    for user in userSet:

        if(user in listOfUsernames):
            continue

        scrapecount += 1

        #every 20, sleep 30 seconds
        if(scrapecount % 50 == 0):
            time.sleep(30)

        time.sleep(random.randint(5,8))
        res = requestIOSite(user)
        if(res!= False):
            #writes html to file
            with open("./githubIOSites/"+user+"_GithubSiteHTML.html","w+") as outfile:
                outfile.write(res)
        else:
            with open("./githubIOSites/"+user+"_INVALID.html","w+") as outfile:
                outfile.write("no data")


    print("done")

