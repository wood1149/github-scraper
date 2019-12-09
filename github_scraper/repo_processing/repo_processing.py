import sys
import requests

BASE_URL = 'https://api.github.com'

# Used so script ignores binary files
# We could do another way later if we don't want to list out all extensions we want
SCRAPABLE_EXTENSIONS = {'cpp', 'txt', 'py', 'config', 'c', 'js', 'html'}
DIRECTORIES_TO_AVOID = {'node_modules', 'env', 'github_site_data', 'username_data', 'js'}

def get_user_repos(username, headers={}):
    """Gets list of public repositories owned by a particular user
    
        [:param `username`] the String representation of the user's username
        
        [:rtype] `list` of dictionaries
        
        [:returns] a list of the public repositories owned by the user
    """
    
    url = f'{BASE_URL}/users/{username}/repos'

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.HTTPError as e:
        sys.exit(e)

    all_repo_names = []
    for repo in response.json():
        all_repo_names.append(repo['name'])
    return all_repo_names


def get_repo_files(username, repo_name, headers={}):
    """Gets list of all files for a specific user
    
        [:param `username`] the String representation of the user's username
        [:param `repo_name`] the String representation of the name of a repository
        [:param `path`] the String representation of the path of a directory within a repository. Used in recursive calls.
        
        [:rtype] `dictionary`
        
        [:returns] a dictionary of all the file paths and content from a given user's repository
    """

    # Get the entire tree to get file paths and in turn create the download urls
    url = f'{BASE_URL}/repos/{username}/{repo_name}/git/trees/master?recursive=1'

    try:
        response = requests.get(url, headers=headers)
        res = response.json()
    except requests.HTTPError as e:
        print(e)
        return {}

    repo_files = {}

    try:
        tree = res['tree']
    except KeyError as e:
        print('KeyError from Github Tree request')
        return {}

    for t in tree:
        if t['type'] == 'blob':
            file_path = t['path']
            file_ext = file_path.split(".")[-1]
            if file_ext in SCRAPABLE_EXTENSIONS and not any(dir in file_path for dir in DIRECTORIES_TO_AVOID):
                download_url = f'https://raw.githubusercontent.com/{username}/{repo_name}/master/{file_path}'
                try:
                    content = requests.get(download_url).text
                    file_key = repo_name + '/' + file_path
                    repo_files[file_key] = content
                except requests.HTTPError as e:
                    print(e)
                

    return repo_files

def get_all_files_for_user(username, headers={}):
    all_files = {}
    repo_names = get_user_repos(username, headers)
    for name in repo_names:
        repo_files = get_repo_files(username, name, headers)
        all_files.update(repo_files)
    return all_files

if __name__ == '__main__':
    # Testing purposes
    username = 'ss5nathan'

    files = get_all_files_for_user(username)
    print(files)


