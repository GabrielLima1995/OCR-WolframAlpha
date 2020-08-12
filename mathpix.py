import sys
import base64
import requests
import wolframalpha
import json
import ast

def math_ocr(file_path):
    
    image_uri = "data:image/jpg;base64," + base64.b64encode(open(file_path, "rb").read()).decode()
    r = requests.post("https://api.mathpix.com/v3/text",
    data=json.dumps({'src': image_uri}),
    headers={"app_id": "API Project", "app_key": "API KEY",
    "Content-type": "application/json"})
    #string = json.dumps(json.loads(r.text), indent=4, sort_keys=True)
    string = r.text
    text = ast.literal_eval(string)["text"]

    return text.strip('\(').strip('\)')


def wolframAlpha(input):
    
    key = "<Your wolframAlpha's Key"
    client = wolframalpha.Client(key)
    request = client.query(input)
    output = next(request.results).text
    return output


text = math_ocr("images/0216.jpg")
print(wolframAlpha(text))