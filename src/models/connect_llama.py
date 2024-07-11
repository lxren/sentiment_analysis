import requests


def llama_prompt(prompt):
  url = "https://api-llama.isaic.ai/api/generate"

  headers = {
    "Authorization": "AUTHKEY",
    "Content-Type": "application/json",
  }

  data = {"model": "llama2", "stream": False, "prompt": prompt}

  response = requests.post(url, headers=headers, json=data)
  #print(response)
  return response.json()['response']