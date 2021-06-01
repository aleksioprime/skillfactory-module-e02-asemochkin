from flask import Flask, render_template, request, jsonify
from service import add_email, get_tasks

app = Flask(__name__)

# главная страница, написание текста сообщения и указание количества секунд его отправки
@app.route("/", methods=['GET'])
def main():
    return render_template("send_email.html")

@app.route("/response", methods=['POST'])
def send_email():
    text = request.form.get('text')
    email = request.form.get('email')
    timer = int(request.form.get('timer'))
    add_email(text, timer, email)
    return jsonify({"text":text, "timer": timer, "email": email}), 201

@app.route("/tasks", methods=['GET'])
def last_tasks():
    emails = get_tasks()
    return render_template("list_emails.html", emails=emails)

# if __name__ == '__main__':
#     app.run(debug=True)