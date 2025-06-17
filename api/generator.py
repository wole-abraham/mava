from ollama import chat, generate
import  json
def gen(topic):
    stream = generate(
    model='mistral',
    prompt=
                f"""
    You are a helpful assistant that creates multiple choice quiz questions.

    Generate 2 multiple choice questions based on this given text  {topic}. Return the result in this strict JSON format: Each choice must have on true and the rest false so we'd know the answer
    just repy with the json no extra information

    [
    {{
        "question": "Question text here",
        "choices": {{
        "the choice": false,
        "the choice": true,
        "the choice": false,
        "the choice": false
        }}
    }}
    ]
    """,
    )
    j = json.loads(stream['response'])
    return j
