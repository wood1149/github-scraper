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
let usernameToScrape = "arunoda"
let numUsersToScrape = 1000

//Main Code
let bigSet2 = new Set();
let nxurl = usernameToScrape+"/followers";
let userCounter = 0;


//gets and writes data for a single page of followers
const getOnePage = url => {
    gs(url, (err, data) => {
        let pageUsernames = new Set();
        if (data) {
            console.log("data recieved");
            data.entries.forEach(userdata => {
                bigSet2.add(userdata.username);
                pageUsernames.add(userdata.username);
                userCounter += 1;

                fs.appendFile("./users_"+numUsersToScrape+"_"+usernameToScrape+"Followers.txt", userdata.username + "\n", err => {
                    // In case of a error throw err.
                    if (err) throw err;
                });
            });
            nxurl = data.next_page;
        }
    });
};

//makes a request every 10 seconds
const recGet = () => {
    let inter = setInterval(() => {
        getOnePage(nxurl);
        if (userCounter > numUsersToScrape) {
            console.log("cleared interval");
            clearInterval(inter);
        } else {
            console.log("running again " + userCounter);
        }
    }, 10000);
};

recGet();





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
