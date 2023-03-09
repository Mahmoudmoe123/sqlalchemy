from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/result', methods=['GET'])
def result():
    number = request.args.get('number', None)
    result = ''
    if number:
        try:
            number = int(number)
            if number % 2 == 0:
                result = 'even'
            else:
                result = 'odd'
        except ValueError:
            result = 'not an integer'
    else:
        result = 'no query parameter included'
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run()
