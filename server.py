from flask import Flask, render_template, url_for, request, redirect
import csv

# Steps to run server local
# Activate venv - venv\Scripts\activate
# Initialize Flask - flask --app server.py run

app = Flask(__name__)
print(__name__)

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')

def write_to_csv_file(data):
    with open('database.csv', mode='a', newline='') as database_2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database_2,delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv_file(data)
            return redirect('/thank_you.html')
        except:
            return 'Did not save to database'
    else:
        return 'Oops! I am new, I am unsure of what happened'