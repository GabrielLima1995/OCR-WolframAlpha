import wolframalpha

def wolframAlpha(input):
    
    key = "93P3YQ-J9RYAGHPRK "
    client = wolframalpha.Client(key)
    request = client.query(input)
    output = next(request.results).text
    return output


