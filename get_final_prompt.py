import json


def get_final_prompt(user_contributions: list, summary_size: str, expertise: str) -> list:

    # sample response for adding in prompt
    sample_json_response = f"""
    [
        {{
            'repository_name': '....',
            'contribution_summary': [
                "line 1",
                "line 2",
                "line 3",
                .,
                .,
                "line {summary_size}"
            ]
        }},
        {{
            'repository_name': '....',
            'contribution_summary': [
                "line 1",
                "line 2",
                "line 3"
                "line 3",
                .,
                .,
                "line {summary_size}"
            ]
        }},
    ]
    """

    introduction_to_prompt = f"The JSON objects provided below detail a user's GitHub contributions, including repository names, contributions made, and repository descriptions. The user is a software developer with expertise in {expertise}. Please generate a JSON output that includes the repository name and a summary of contributions in three concise, technically sound, and relevant lines. These summaries will be used to create a GitHub report showcasing the user's contributions..\n\n"
    closure_to_prompt = f"\n\nFrom the above context, provide a JSON response with the repository name and a summarized contribution in {summary_size} technically sound, and relevant lines for each repository with respect to the expertise as well. Format of json response: {sample_json_response}. Only provide json output and nothing else."
    prompt = introduction_to_prompt + "\n\n------\n\n".join(json.dumps(repo, indent=4) for repo in user_contributions) + closure_to_prompt

    return prompt


