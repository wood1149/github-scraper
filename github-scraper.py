# main module for github-scraper app
import sys
import requests

BASE_URL = 'https://api.github.com'

# this is not an exhaustive list of functions, will need to add to/refactor architecture of module depending on how we want to implement file access and reading

def get_user_repos(username):
    """Gets list of public repositories owned by a particular user
    
        [:param `username`] the String representation of the user's username
        
        [:rtype] `list` of dictionaries
        
        [:returns] a list of the public repositories owned by the user
    """
    
    url = f'{BASE_URL}/users/{username}/repos'

    try:
        response = requests.get(url)
        print(response.status_code)
        response.raise_for_status()
    except requests.HTTPError as e:
        sys.exit(e)

    return response.json()

def get_repo_files(username, repo):
    # TODO: implement
    return

def find_match(username, repo, file, pattern):
    # TODO: implement
    return

repos = get_user_repos('kklose23')

print(f'Num repos: {len(repos)}')

repos.sort(key=lambda x: x['stargazers_count'], reverse=True)

print('Top 5 most starred repos:')

for repo in repos[0:5]:
    count = repo['stargazers_count']
    name = repo['name']
    print(f'{count}: {name}')