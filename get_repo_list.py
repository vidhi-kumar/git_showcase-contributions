import os
import requests
import json
import sys

def get_repo_list(access_token: str) -> list:
    # Github API endpoint to fetch repositories belonging to user
    url = "https://api.github.com/user/repos"

    # headers for authentication
    headers = {
    'Authorization': f'token {access_token}',
    'Accept': 'application/vnd.github.v3+json'
    }

    # making API request
    response = requests.get(url, headers=headers)

    # Check if the request was successful and return them
    user_repositories = []
    if response.status_code == 200:
        repositories = response.json()
        for repo in repositories:
            user_repositories.append(repo['full_name'])

    return user_repositories

