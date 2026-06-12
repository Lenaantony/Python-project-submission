import requests
import json

username="Lenaantony"
url=f"https://api.github.com/users/{username}/repos"
response=requests.get(url)
repos=response.json()
projects=[]
for repo in repos:
    projects.append({
        "name":repo["name"],
        "description":repo["description"],
        "url":repo["html_url"]
    })
with open("projects.json","w")as file:
    json.dump(projects,file,indent=4)
print("projects.json generated")