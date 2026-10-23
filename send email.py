import smtplib
from email.message import EmailMessage
import getpass

EMAIL = input("Your Microsoft 365 email: ").strip()
PASSWORD = getpass.getpass("Your password: ")

# IMPORTANT: change this
TO_EMAIL = "syahidhalid@exim.com.my"

msg = EmailMessage()
msg["From"] = EMAIL
msg["To"] = TO_EMAIL
msg["Subject"] = "Python Email Test"

msg.set_content("""
Hi,

This is a test email from Python.

Regards,
Syahid
""")

try:
    print("1. Connecting to Microsoft 365...")

    server = smtplib.SMTP(
        "smtp.office365.com",
        587,
        timeout=30
    )

    server.set_debuglevel(1)

    print("2. Starting TLS...")
    server.ehlo()
    server.starttls()
    server.ehlo()

    print("3. Logging in...")
    server.login(EMAIL, PASSWORD)

    print("4. Sending email...")
    server.send_message(msg)

    server.quit()

    print("Email sent successfully!")

except smtplib.SMTPAuthenticationError as e:
    print("\nAUTHENTICATION ERROR")
    print("SMTP code:", e.smtp_code)
    print("SMTP message:", e.smtp_error)

except smtplib.SMTPConnectError as e:
    print("\nCONNECTION ERROR")
    print(e)

except TimeoutError:
    print("\nCONNECTION TIMEOUT")

except Exception as e:
    print("\nOTHER ERROR")
    print(type(e).__name__)
    print(e)