import re
import smtplib
from email.mime.text import MIMEText

from dundie.settings import SMTP_HOST, SMTP_PORT, SMTP_TIMEOUT
from dundie.utils.log import get_logger

log = get_logger()


def is_email(email):
    """Return True if the email is valid"""
    return (
        re.match(r"\b[A-Za-z0-9._+-]+@[A-za-z0-9.-]+\.[A-z|a-z]{2,}\b", email)
        is not None
    )


def send_email(from_, to: list, subject, text):
    try:
        with smtplib.SMTP(
            host=SMTP_HOST, port=SMTP_PORT, timeout=SMTP_TIMEOUT
        ) as server:
            message = MIMEText(text)
            message["Subject"] = subject
            message["From"] = from_
            message["To"] = ",".join(to)
            server.sendmail(from_, to, message.as_string())
    except:
        log.error("Cannot send email to %s", to)
