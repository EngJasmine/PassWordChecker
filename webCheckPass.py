from sys import stdout

from flask import Flask, request, render_template
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        password = request.form['password']
        # Call your password-checking script
        result = subprocess.run(['python', 'checkmypass.py', password], capture_output=True, text=True)

        output = result.stdout  # Capture the output of your script
        result = output.strip()  # Clean up the output

    return render_template('index.html', result=result)



if __name__ == '__main__':
    app.run(debug=True)

