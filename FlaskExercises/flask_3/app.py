from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

ORGANIZATIONS = ['Charlotte Hack', 'Code 9', '49er Imporv', '49th Security Division', 'Archery']

registered_users = {}


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        
        name = request.form['name']
        organization = request.form['organization']

        if not name:
            return render_template('home.html', error='Please enter your name.')
        if not organization or organization not in ORGANIZATIONS:
            return render_template('home.html', error='Please select a valid organization.')

        registered_users[name] = organization

        return redirect(url_for('list_registered_users'))

    return render_template('home.html', organizations=ORGANIZATIONS)


@app.route('/list')
def list_registered_users():
    return render_template('list.html', users=registered_users)


if __name__ == '__main__':
    app.run(debug=True)
