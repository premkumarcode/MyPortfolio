from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__, template_folder='templates', static_folder='static')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_csv(data):
    with open('message_detail.csv', 'a') as db:
        email=data['email']
        subject = data['subject']
        message = data['message']
        csv_write = csv.writer(db, delimiter=',')

        csv_write.writerow([email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        requested_data = request.form.to_dict()
        write_to_csv(requested_data)
        return redirect('thankyou.html')
    else:
        return "Form not submitted.Need to implement the values"
