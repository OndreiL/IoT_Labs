import imaplib
import email
#import RPi.GPIO as GPIO
import time
from email.header import decode_header

mail_pass = "hvsvscxibcwaxrxy"
username = "frogerr2001@yandex.ru"
imap_server = "imap.yandex.ru"
#imap = imaplib.IMAP4_SSL(imap_server)
#imap.login(username, mail_pass)
#status, messages = imap.select("INBOX")
#GPIO.setmode(GPIO.BOARD) #"включение" GPIO
#GPIO.setup(7, GPIO.OUT)  #объявление 7-го пина как выход



mail = imaplib.IMAP4_SSL('imap.yandex.ru')
(retcode, capabilities) = mail.login('frogerr2001@yandex.ru','hvsvscxibcwaxrxy')
mail.list()
mail.select('inbox')

(retcode, messages) = mail.search(None, '(UNSEEN)')
if retcode == 'OK':

   for num in messages[0].split() :
      print ('Processing ')
      typ, data = mail.fetch(num,'(RFC822)')
      for response_part in data:
         if isinstance(response_part, tuple):
             original = email.message_from_bytes(response_part[1])
             subject, encoding = decode_header(original["Subject"])[0]
             if isinstance(subject, bytes):
                 # if it's a bytes, decode to str
                 subject = subject.decode(encoding)
             # decode email sender
             From, encoding = decode_header(original.get("From"))[0]
             if isinstance(From, bytes):
                 From = From.decode(encoding)
             if subject == 'ALARM':
                #GPIO.output(7, 1)
                print ("ПИЗДЕЦ")
                time.sleep(5)
                #GPIO.output(7, 0)
             typ, data = mail.store(num,'+FLAGS','\\Seen')
