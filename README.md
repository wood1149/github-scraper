# github-scraper
Searches predefined list of GitHub Users' repositories and GitHub.io pages for sensitive or personal information.

## Resources

Here is some documentation for tools/APIs that we will most likely be using:

### [GitHub API](https://developer.github.com/v3/)

Specifically, the [contents](https://developer.github.com/v3/repos/contents/#get-contents) API. This will let us retrieve information about a specific file, given the username, repo, and filename associated with it. I imagine we will use the `download_url` to get the files in raw format in the browser for easy file scraping.

### nelsonic's [github-scraper](https://github.com/nelsonic/github-scraper)

The extent to which we will be able to use this tool is TBD, but at the very least we can use it to gather a list of popular GitHub users and their repositories.

## First Steps

Before the first check in with our professor, it would be good to have a script that can gather a solid list of users, and scan through their files for some specific keywords. This can be very basic regex (find all occurances of the string `"my name is dave"` or maybe something a little more common) simply to prove the funcionality of the tool.

Assuming we want ot use nelsonic's github-scraper, we will be writing in JavaScript. However, if we find the tool's funcionality to be fairly basic, we could perhaps move to Python.