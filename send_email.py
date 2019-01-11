import flask
from flask_mail import Mail, Message

app = flask.Flask(__name__)
app.config.update(
    DEBUG=True,
    #EMAIL SETTINGS
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME = '',
    MAIL_PASSWORD = ''
    )

mail = Mail(app)

app.route('/send-mail/')
def send_mail(recipients, subject, mailbody):
    try:
        with app.app_context():
            msg = Message(subject,
                          sender=app.config.get('MAIL_USERNAME'),
                          recipients=recipients)
            msg.body = mailbody           
            mail.send(msg)
        return 'Mail sent!'
    except Exception as e:
        return(str(e))