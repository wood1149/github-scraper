# github-scraper
Searches predefined list of GitHub Users' repositories and GitHub.io pages for sensitive or personal information.

## Scrape Usernames:
    1)npm install
    2)node scrapeUsers.js

    Edit the scrapeUsers file to pick what user will be scraped for their usernames.

    This tool will allow the user to scrape many ussernames from github. Please input a user with many followers, and the tool will output their followers, up to a maximum.

    Features in scrapeUsers.js:
        Edit "usernameToScrape" to set user
        Edit "numUsersToScrape" to set limits
        Edit "operation" to 0 to scrape a users followers
        Edit "operation" to 1 to scrape followers of a user (the user must have been scraped by operation 0 first)



## Coder Resources

Here is some documentation for tools/APIs that we will most likely be using:

### GitHub's [API](https://developer.github.com/v3/)

Specifically, the [contents](https://developer.github.com/v3/repos/contents/#get-contents) API. This will let us retrieve information about a specific file, given the username, repo, and filename associated with it. I imagine we will use the `download_url` to get the files in raw format in the browser for easy file scraping.

### nelsonic's [github-scraper](https://github.com/nelsonic/github-scraper)

The extent to which we will be able to use this tool is TBD, but at the very least we can use it to gather a list of popular GitHub users and their repositories.
