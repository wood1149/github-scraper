''' arg_parsing module. '''
import argparse

from sample_module import test, test2
from repo_processing import repo_processing as RepoProcessing

# Hardcoded strings, maybe replace with configuration file
desc = ''

def setup_argparse():
    parser = argparse.ArgumentParser(description='GitHub repository file vulnerability finder')

    # Add the CL args
    parser.add_argument('-u', '--username', required=True, help='GitHub username')
    parser.add_argument('-r', '--repo', help='Repository name')

    # Check for these vulnerabilities
    vuln_group = parser.add_argument_group('Vulnerability types')
    vuln_group.add_argument('-a', '--api', help='Look for API keys', action='store_true')
    vuln_group.add_argument('-p', '--password', help='Look for passwords', action='store_true')
    vuln_group.add_argument('-e', '--email', help='Look for email addresses', action='store_true')
    args = parser.parse_args()
    
    if args.repo:
        # Repo name provided
        repo_files = RepoProcessing.get_repo_files(args.username, args.repo)
    else:
        repo_names = RepoProcessing.get_user_repos(args.username)
    
