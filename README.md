# github-scraper
Searches predefined list of GitHub Users' repositories and GitHub.io pages for sensitive or personal information.


## Overview
This python package primarily deals with finding sensitive data on public github repositories. This senstive info includes password, API keys, crypto (AES, RSA) keys, and cryptocurrency keys.

**Single User**

This tool was made to scrape a single user's repository for accidental secrets exposed. This can be run via commandline or script (see the demo script in the top level directory or see the **Main Functionality** section below for commandline usage)

**Group Data Collection**

This tool also functions as a way to anlyaze a list of usernames for secrets in github files

The first step of identifying secrets is to gather a list of usernames. This functionality detailed in the **Scrape Usernames** section below. This is the only section using Javascript, due to a dependency. The rest of the python library will reference this username list created in ./usernames

**Main Functionality:**

Commandline usage

```python
    python3 github_scraper -h
```

**Demo:**

There is a demo repository that was setup to include the different types of vulnerabilities.  This demo repository can be scraped by running the command below.

```python
    python3 github_scraper -u daphneehuang -r cse4471-demo
```

The vulnerabilities discovered can be checked in the public repository at https://github.com/daphneehuang/cse4471-demo

Also, see the demo file (get-user-data.py) in the root directory to see a basic program that will loop through the entire directory of scraped usernames. This github_scraper module will run the main functionality of finding vulnerable files. The output will be the accumulated data by the scraper on the number of vulnerabilities found, unlike the commandline which will give specific files and line numbers of the vulnerabilities.  A Github API OAuth Token would be needed for running this script on more than a few of the users.

## Scrape Usernames:
```
    npm install
    node scrapeUsers.js
```

Run the scrapeUsers.js file to pick what user will be scraped for their usernames.

This tool will allow the user to scrape many usernames from github. Please input a user with many followers, and the tool will output their followers, up to a maximum.

Features in scrapeUsers.js:
    "usernameToScrape" set user
    "numUsersToScrape" set limits
    "operation" 0 to scrape a users followers
    "operation" 1 to scrape followers of a user (the user must have been scraped by operation 0 first)

> Use the CLI prompts of scrapeUsers.js for the easiest use

## Extra Features:

Also included in the "github_site_tools" module there is the ability to scrape github sites found in "github_site_data." Keep in mind, usernames must have been previously scraped by the scrapeUsers.js file into the ./usernames directory for these additional features to work.

```python
    from github_scraper.github_site_tools import scrape_githubIO_sites as SGIO
    #This will save site data to the top level directory
    SGIO.main() 
```

Then
```python
    from github_scraper.github_site_tools import get_user_emails as GE
    #This will save site data to the top level directory (./emails.json)
    GE.main() 
```

This will extact emails from these github sites. Currently only emails are supported for github sites

## External Resources

Here is some documentation for tools/APIs that are used:

### GitHub's [API](https://developer.github.com/v3/)

Specifically, the [contents](https://developer.github.com/v3/repos/contents/#get-contents) API. This lets us retrieve information about a specific file, given the username, repo, and filename associated with it.

### nelsonic's [github-scraper](https://github.com/nelsonic/github-scraper)

Used to gather a list of popular GitHub users and their repositories.
