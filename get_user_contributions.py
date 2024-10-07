from langchain_community.document_loaders import GitHubIssuesLoader
from langchain_community.document_loaders import GithubFileLoader

def get_user_contributions(repository_list: list, username: str, access_token: str) -> list:
    user_contributions = []
    for repo in repository_list:
        # loading issues and pr repo wise
        repo_name = repo.split("/")[1]
        loader = GitHubIssuesLoader(
            repo=repo,
            access_token=access_token,  
            creator=username,
            include_prs=True,
            state='all'
        )

        docs = loader.load() 
        
        # gathering contribution in the repo
        contributions = []  # Initialize contributions list outside the document loop

        for doc in docs:
            contribution_description = doc.metadata['title'] + " " + doc.page_content
            contributions.append(contribution_description)

        if contributions:
            # Create the filtered_data after contributions are gathered
            filtered_data = {}
            filtered_data['repository_name'] = repo_name
            filtered_data['contributions'] = contributions

            # Loading the repository README file
            loader = GithubFileLoader(
                repo=username + "/" + repo_name,
                access_token=access_token,
                github_api_url="https://api.github.com",
                file_filter=lambda file_path: file_path == "README.md",  
            )
            main_readme_data = loader.load()

            if main_readme_data:
                filtered_data['repository_description'] = main_readme_data[0].page_content
            else:
                filtered_data['repository_description'] = "No README available."

            # Append the filtered_data to user_contributions
            user_contributions.append(filtered_data)
    
    return user_contributions
