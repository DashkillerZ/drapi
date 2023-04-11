import openai
openai.api_key = "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"

def generate_response(request):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=request,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )
    text = response['choices'][0]['text']
    return text
print(generate_response(request))