import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def send_email_with_text(text, email_from, email_to):
    message = Mail(
        from_email=email_from,
        to_emails=email_to)
    message.template_id = os.environ.get('TEMPLATE_ID')
    message.dynamic_template_data = {
            "text": text,
        }
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API'))
        response = sg.send(message)
        return response
    except Exception as e:
        print(e.body)