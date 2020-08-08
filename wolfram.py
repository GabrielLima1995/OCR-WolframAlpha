import wolframalpha

input = input("Digite an operation: ")

key = "Your WolframAlpha's Key "
client = wolframalpha.Client(key)
request = client.query(input)
output = next(request.results).text
print(output)
