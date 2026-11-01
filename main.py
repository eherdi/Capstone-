from flask import *
from flask_mail import Mail, Message
import yagmail

app = Flask(__name__)
mail = Mail(app)
@app.route('/')
def home():
    return render_template('Index.html')
@app.route("/client_request")
def client_request():

    return render_template('clientrequest.html')


@app.route("/client_request/questionnaire",methods=["GET", "POST"])
def questionnaire():
    if request.method == "GET":
        return render_template('questionnaire.html')

    elif request.method == "POST":
        fullname = request.form.get("FullName")
        email = request.form.get("Email")
        phone = request.form.get("Phone")


        email_context={"fullname":fullname,"email":email,"phone":phone}

        yag = yagmail.SMTP("dummytestdev2@gmail.com","pretend there a password here")
        yag.send("dummytestdev2@gmail.com",'Hello!',email_context)



        return render_template('Message.html', email_context=email_context )



@app.route("/consultation")
def consultation():
    return render_template('consultation.html')

@app.route("/paint")
def paint():
    return render_template('paint.html')

@app.route("/Works")
def Works():
    return render_template('Works.html')



def main():
    app.run(debug=True)



main()

