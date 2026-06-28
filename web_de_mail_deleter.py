##web_de_mail_deleter welcher alle mails vor xx Tagen löscht
##imap muss aktiviert sein!
##import imaplib, email, datetime
##login festlegen

import imaplib, email, datetime

username_web = "email"
password_web = "Password"

##verbinden mit mail server
try:
    mail = imaplib.IMAP4_SSL("imap.web.de")
    mail.login(username_web, password_web)
    print("Login erfolgreich")

##posteingang wählen
    mail.select("INBOX")
    print("Posteingang geöffnet")
except Exception as e:
    print(f"Fehler: {e}")

#Number of days
number_of_days = input("E-Mails die älter als xx Tage sind sollen gelöscht werden:")

date = datetime.date.today() - datetime.timedelta(days=int(number_of_days))

date_str = date.strftime("%d-%b-%Y")
status, messages = mail.search(None, f'Before {date_str}')

##splitten
email_ids = messages[0].split()
print(f"{len(email_ids)} E-Mails gefunden")

##confirm
confirm = input(f"{len(email_ids)} E-Mails löschen? ja/nein: ")

##Delete
if confirm.lower() == "ja":
    for email_id in email_ids:
        mail.store(email_id, "+FLAGS", "\\Deleted")
    mail.expunge()
    print(f"{len(email_ids)} E-Mails gelöscht.")
else:
    print("Abgebrochen.")



















