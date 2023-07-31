from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)

@app.route("/")
def myHome():
    return render_template('index.html')

@app.route("/<string:page_name>")
def myWorks(page_name):
    return render_template(page_name)

def writeToTxtFile(data):
    with open('database.txt', 'a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'{email}, {subject}, {message}\n')


def writeToCsvFile(data):
    try:
        with open('database.csv', 'a') as database2:
            email = data['email']
            subject = data['subject']
            message = data['message']
            csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow([email, subject, message])
    except Exception as e:
        print("Error", e)


@app.route("/submit_form", methods = {"POST", "GET"})
def submitForm():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            writeToCsvFile(data)
            return redirect('/thankyou.html')
        except: 
            print("Error")
    else: 
        return '<h1>Form ran into an error</h1>'

