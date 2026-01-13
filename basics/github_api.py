import requests
import plotly.express as px

# Make an API call and check the response.

url = 'https://api.github.com/search/repositories'
url += '?q=language:python+sort:stars:>10000'

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Convert the response object to a dictionary.
response_dict = r.json()

# Process results.
print(response_dict.keys())

print(f"Total repo: {response_dict['total_count']}")
print(f"Complete results: {response_dict['incomplete_results']}")

repo_dicts = response_dict['items']
print(f"Repo returned: {len(repo_dicts)}")

# Examine the first repo.
repo_dict = repo_dicts[0]
print(f"\nKeys: {len(repo_dict)}")
for key in sorted(repo_dict.keys()):
    print(key)

for repo in repo_dicts:
    print(f"\nSelected info about repo: {repo['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")

repo_names, stars = [], []
for repo in repo_dicts:
    repo_names.append(repo['name'])
    stars.append(repo['stargazers_count'])

# Visualize repo vs star count graph

fig = px.bar(x=repo_names, y=stars)
fig.show()
