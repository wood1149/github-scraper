/*
Infosec Project
Teamname:TeamName

Github Scraper


This file will gather necessary usernames and repos
*/

//dependencies
const gs = require("github-scraper");
const fs = require("fs");

//EDIT THESE
//0, scrape from user
//1, scrape user followers
const operation = 0;
let usernameToScrape = "orta" //yegor256
const originalUser = usernameToScrape
let numUsersToScrape = 1000

//Main Code
let bigSet2 = new Set();
let nxurl = usernameToScrape+"/followers";
let userCounter = 0;
let unamesToScrape = [];
let seenUnamesThisRun = new Set()





//gets and writes data for a single page of followers
const getOnePage = url => {
    if(url == undefined){
        return;
    }
    gs(url, (err, data) => {
        let pageUsernames = new Set();
        if (data) {
            console.log("data recieved");
            data.entries.forEach(userdata => {
                bigSet2.add(userdata.username);
                pageUsernames.add(userdata.username);
                userCounter += 1;

                fs.appendFile("./usernames/users_"+numUsersToScrape+"_"+usernameToScrape+"Followers.txt", userdata.username + "\n", err => {
                    // In case of a error throw err.
                    if (err) throw err;
                });
            });
            nxurl = data.next_page;
        }

        if(err){
            nxurl = undefined
            console.log("ERROR!")
            console.log(err)
        }
        
    });
    
};


const hasUserBeenScraped = username =>{
    let res = false
    if(!seenUnamesThisRun.has(username))
    {
        fs.readdirSync("./usernames/").forEach(file => {
         if(file.includes(username)){
                console.log('Data for ' + username + " already exists")
                res = file;
            }
        });
    }
   
     
    return res;
}


const getFollowersOfFollowers = () =>{
    let user = hasUserBeenScraped(usernameToScrape)

    if(user === false){
        console.log("could not find user")
        throw "Error"
    }

    console.log("reading " + "./usernames/"+user)
    let lines = fs.readFileSync("./usernames/"+user, 'utf-8')
    .split('\n')
    .filter(Boolean);

    unamesToScrape = lines;
    intervalGet();
}
//makes a request every 10 seconds
const intervalGet = () => {
    let clInterval = false;
    let unameIndex = 0
    if(operation == 1){
        usernameToScrape = unamesToScrape[unameIndex]
        nxurl =  usernameToScrape+"/followers";
    }


    if(hasUserBeenScraped(usernameToScrape) !== false && (operation == 0 || operation === 1 && unamesToScrape.length <= unameIndex) ){
        throw "Data already exists"
    }else{
        seenUnamesThisRun.add(usernameToScrape)
        console.log("Starting to scrape " + usernameToScrape + " " + nxurl)
        let inter = setInterval(() => {

            if (hasUserBeenScraped(usernameToScrape) !== false || userCounter > numUsersToScrape  || nxurl === undefined ) {
                seenUnamesThisRun.add(usernameToScrape)

                console.log("cleared interval " + usernameToScrape);
                console.log(seenUnamesThisRun)
                clInterval= true;
                userCounter = 0;

                if( operation === 1 && unameIndex < unamesToScrape.length ){
                    unameIndex++;
                    usernameToScrape = unamesToScrape[unameIndex];
                    nxurl = usernameToScrape+"/followers"
                    console.log("Now scraping from " + usernameToScrape + " " + unameIndex + "/" + unamesToScrape.length)
                }else{
                    clearInterval(inter)
                }
            } else {
                console.log("Running again " + userCounter + " " + nxurl);
                getOnePage(nxurl);
            }

           

    }, 10000);
    }
   
   
};

if(operation === 0){
    intervalGet();
}else if(operation === 1){
    getFollowersOfFollowers();
}






//OLD CODE
const getNextPage = async url => {
    new Promise((resolve, reject) => {
        console.log("got url " + url);
        gs(url, (err, data) => {
            let pageUsernames = new Set();

            if (data) {
                data.entries.forEach(userdata => {
                    pageUsernames.add(userdata.username);
                });
                console.log(
                    "found " +
                        pageUsernames.size +
                        " on this page url:" +
                        data.next_page
                );
                //console.log(data)

                resolve({
                    nextPageUrl: data.next_page,
                    pageUsernames: pageUsernames
                });
            } else {
                reject();
            }
        });
    });
};

let bigSet = new Set();
const recursiveGet = async (url, numberLeft) => {
    if (numberLeft > 0) {
        getNextPage(url).then(data => {
            console.log("found usernames " + data);
            if (data) {
                console.log(data.pageUsernames);
                bigSet.add(data.pageUsernames);
                getNextPage(data.nextPageUrl, numberLeft - 51);
            }
        });
    }
};

//recursiveGet("fabpot/followers", 2);

const getFollowers = async (user, numberOfUsernames) => {
    //defines number of usernames per person to scrape
    let allUsernames = new Set();

    let nextPageUrl = user + "/followers";
    let usercount = 0;
    let pageCounter = 0;
    console.log("before while");
    while (nextPageUrl && usercount < numberOfUsernames) {
        console.log("in while");

        data2 = await getNextPage(nextPageUrl);
        console.log(data2);
        // pageData = await gs(nextPageUrl, async (err, data) => {
        //     data.entries.forEach(userdata => {
        //         allUsernames.add(userdata.username);
        //     });
        //     nextPageUrl = data.next_page;
        //     pageCounter += 1;
        //     console.log("finished page " + nextPageUrl);
        // });

        if (allUsernames.length > 2) {
            return allUsernames;
        }
        break;
    }
    console.log("after while");
};

//getFollowers("fabpot", 200);
