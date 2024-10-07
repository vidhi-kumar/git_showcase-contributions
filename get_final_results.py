import json
import sys

def get_final_results(final_prompt, client, model):
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": final_prompt
            }
        ]
    )

    final_results = completion.choices[0].message.content.strip()
    cleaned_results = final_results.strip('```json').strip('```').strip()
    return cleaned_results