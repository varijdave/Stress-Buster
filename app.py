from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Replace 'YOUR_API_KEY' with your actual OpenAI API key
openai.api_key = 'YOUR_API_KEY'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']
    response = get_stress_relief_response(user_input)
    return response

def get_stress_relief_response(input_text):
    prompt = "You are feeling stressed and need some relaxation. " + input_text
    response = openai.Completion.create(
        engine="text-davinci-002",  # You can also use "text-davinci-003" if it's available in the future
        prompt=prompt,
        max_tokens=150,
        temperature=0.7,
        stop=["You:"]
    )

    return response.choices[0].text.strip()

if __name__ == "__main__":
    app.run(debug=True, port = 300)

