import wolframalpha

def wolframAlpha(input):
    
    key = "<YOUR API KEY >"
    client = wolframalpha.Client(key)
    request = client.query(input)
    output = next(request.results).text
    return output


