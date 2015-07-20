# app/cron.py

import kronos
import random
import os.path
from app import views

from django.core.mail import get_connection, send_mail
from django.core.mail.message import EmailMessage
from django.core.files import File
from django.core.validators import validate_email
from datetime import timedelta
from django.utils import timezone
from .models import Patient, Survey

SITE_ROOT = os.path.dirname(os.path.realpath(__file__))

@kronos.register('0 10 * * 1')
def complain():
    sendEmail()

def getEmailInformation(csv):
	csv = csv.replace(" ", "")
	recipients = csv.split(",")
	return recipients

def getEmailsFromFile():
    return getEmailInformation(getEmailsRawFromFile())

def getEmailsRawFromFile():
    myfile = open(SITE_ROOT + "/Email_Adresses.csv", 'r')
    print(SITE_ROOT + "Email_Adresses.csv")
    return myfile.read()

def saveEmails(csv):
    #validate email adresses 
    recipients = getEmailInformation(csv)
    for i in recipients:
        try:
            validate_email(i)
        except Exception:
            return False
    myfile = open(SITE_ROOT + "/Email_Adresses.csv", 'w')
    myfile.write(csv)
    return True
 
def formatMessage():
    lastWeek = timezone.now().date() - timedelta(days=7)#get last week Date to get one week of Information for the email

    surveys = list(Survey.objects.filter(created_at__gte=lastWeek))
    message  = ""
    message += "ID"
    message += "\t" +"Q1"
    message += "\t" + "Q2"
    message += "\t" + "Q3"
    message += "\t" + "Q4"
    message += "\t" + "Q5"
    message += "\t" + "Q6"
    message += "\t" + "Q7"
    message += "\t" + "Q8"
    message += "\t" + "Q9"
    message += "\t" + "Q10"
    message += "\t" + "Q11"
    message += "\t" + "Q12"
    message += "\t\t" + "delay_counter"
    message += "\t\t" + "created_at"
    message += "\n"

    for i in surveys:
        message += str(i.author)
        message += "\t" +str(i.question1)
        message += "\t" + str(i.question2)
        message += "\t" + str(i.question3)
        message += "\t" + str(i.question4)
        message += "\t" + str(i.question5)
        message += "\t" + str(i.question6)
        message += "\t" + str(i.question7)
        message += "\t" + str(i.question8)
        message += "\t" + str(i.question9)
        message += "\t" + str(i.question10)
        message += "\t" + str(i.question11)
        message += "\t" + str(i.question12)
        message += "\t\t" + str(i.delay_counter)
        message += "\t\t\t\t" + str(i.created_at)
        message += "\n"
    return message

def sendEmail():
    #gets all other information
    #saveEmails("jackiscool20@gmail.com")
    message = formatMessage()
    recipients = getEmailsFromFile()
    
    
    ##send email Need to add information about email you are sending it from here
    my_host = 'smtp.gmail.com'
    my_port = 587
    my_username = '@gmail.com'
    my_password = ''
    my_use_tls = True 
    ##Creates connection to the mail server
    connection = get_connection(host=my_host, port=my_port, username=my_username, password=my_password, use_tls=my_use_tls) 

    ##Send the email to the array/list of Email recipients
    try:
        send_mail('Survey', message, my_username, recipients, connection = connection)
    except Exception:
        print "Message failed to send"