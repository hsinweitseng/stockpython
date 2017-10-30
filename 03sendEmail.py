# Example for sending an email with an attached image using smtplib
#
# IMPORTANT: You need to enter your email login in the main() function.
#            The example is prepared for GMail, but other providers
#            should be possible by changing the mail server.

import time
import smtplib
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders
import Image
from io import BytesIO
currentTime=0

def get_attachment(img):
        bytes = BytesIO()
        img.save(bytes, format='JPEG')
        msg = MIMEBase('image', 'jpeg')
        msg.set_payload(bytes.getvalue())
        encoders.encode_base64(msg)
        msg.add_header('Content-Disposition', 'attachment',
                       filename='~\Desktop\stockpython\status.txt')
        return msg

def main():
        ### CHANGE THESE VALUES:
        to = 'hsinwei.tseng@gmail.com'
        subject = 'Image from Pythonista'
        gmail_user = 'hsinwei.tseng@gmail.com'
        gmail_pwd = '9954beST!'

        #Load a sample image, modify as needed:
        image = Image.open('NUGT.png')

        print 'Connecting...'
        smtpserver = smtplib.SMTP("smtp.gmail.com", 587)

        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.ehlo
        smtpserver.login(gmail_user, gmail_pwd)

        print 'Preparing message...'
        outer = MIMEMultipart()
        outer['Subject'] = subject
        outer['To'] = to
        outer['From'] = gmail_user
        outer.preamble = 'You will not see this in a MIME-aware email reader.\n'
        attachment = get_attachment(image)
        outer.attach(attachment)
        composed = outer.as_string()

        print 'Sending...'
        smtpserver.sendmail(gmail_user, to, composed)
        smtpserver.close()
        print 'Done.'


if __name__ == '__main__':
        main()
        print 'current time=',currentTime


#while True:
#    main()
#    currentTime=currentTime+300
#    print 'current time=',currentTime
#    time.sleep(300)
#    print 'done with sending'
