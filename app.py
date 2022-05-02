from flask import jsonify, Flask
import smtplib
import os

app = Flask(__name__)


@app.route('/')
def home():
    return 'It works!'

@app.route('/contact/<name>/<email>/<subject>/<message>', methods=['GET', 'POST'])
def contact(name, email, subject, message):
    MY_EMAIL = os.environ.get('MY_EMAIL')
    TO_SEND_TO = os.environ.get('TO_SEND_TO')
    MY_PASSWORD = os.environ.get('MY_PASSWORD')

    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=TO_SEND_TO,
            msg=f"Subject: Message from your portfolio website\n\nName of sender: {name}.\nEmail of sender: {email}."
                f"\nSubject from sender: {subject} \n\nMessage: {message}"
        )

    response = jsonify({'Success': 'Email Sent! Expect a feedback from me very soon!'})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/circle/<radius>', methods=['GET', 'POST'])
def get_diameter(radius):
    diameter = float(radius) * 2
    response = jsonify({"diameter": diameter})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/triangle/<height>/<base>', methods=['GET', 'POST'])
def get_area(height, base):
    area = (float(base) * float(height)) / 2
    response = jsonify({"area": area})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response



if __name__ == '__main__':
    app.run(debug=False)
