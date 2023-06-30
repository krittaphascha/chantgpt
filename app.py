from flask import Flask, render_template, request
from model import generate_response
import time
from openai.error import RateLimitError

app = Flask(__name__)

# Main function
# -------

@app.route('/', methods=['GET', 'POST'])

def index():
    output_dict = {0:'', 1:'', 2:''}
    if request.method == 'POST':
        if request.form.get('text'):
            word = request.form.get("text")
            for i in range(3):
                print("... Generating new chant ...")
                try:
                    chant = generate_response(word)
                    time.sleep(5)
                    output_dict[i] = chant
                except RateLimitError as e:
                    output_dict[i] = "error, try again."

    else:
        chant = ''
    return render_template('index.html', output_1=output_dict[0], output_2=output_dict[1], output_3=output_dict[2])
        

if __name__ == '__main__':
    app.run(debug=True)