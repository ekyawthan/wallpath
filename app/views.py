from rest_framework.decorators import api_view
from .models import Patient, Survey
from rest_framework.response import Response
from rest_framework import status
from .serializers import PatientSerializer, SurveySerializer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.shortcuts import render
from .forms import PatientForm

from django.core.mail import get_connection, send_mail
from django.core.mail.message import EmailMessage
from django.core.files import File
from django.core.validators import validate_email
from datetime import timedelta
from django.utils import timezone

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


def home(request):
    if request.user.is_authenticated():
        form = PatientForm()
        all_patient = list(Patient.objects.all())
        return render(request, "home.html", {'patients': all_patient, 'form': form})
    return render(request,  template_name='home.html')


def patient_detail(request, pk):
    try:
        patient = Patient.objects.get(pk=pk)
    except Patient.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    survey_from_this_patient = list(Survey.objects.filter(author=patient.user_name))

    return render(request, "detail.html", {'surveys': survey_from_this_patient, 'username': patient.user_name})


def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            form = PatientForm()
            all_patient = list(Patient.objects.all())
            return render(request, "home.html", {'patients': all_patient, 'form': form})
        form = PatientForm()
        all_patient = list(Patient.objects.all())
        return render(request, "home.html", {'patients': all_patient, 'form': form})


@csrf_exempt
def user_check(request, pk):
    try:
        user = Patient.objects.get(pk=pk)
    except Patient.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        #serializer = PatientSerializer(user)
        return HttpResponse(status=200)





@csrf_exempt
def survey_detail(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Survey.objects.all()
        serializer = SurveySerializer(snippets, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SurveySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

#Email Stuff
def emailsetup(request):
    return render(request, "email.html", {'emails': getEmailsRawFromFile()})

def Email(request):
    #sendEmail()
    if request.method == 'POST':
        Email_Adresses = request.POST["Email_Adresses"]
        if saveEmails(Email_Adresses):
            print "Email Adresses Saved"
            return HttpResponse("<script type=\"text/javascript\"> alert(\"Email Adresses valid and Saved\");window.location = \"/emailsetup\";</script>")
        else:
            print "Email Adresses Not Saved"
            return HttpResponse("<script type=\"text/javascript\"> alert(\"Error: Email Adresses Not Valid\");window.location = \"/emailsetup\";</script>")

    

def getEmailInformation(csv):
    csv = csv.replace(" ", "")
    recipients = csv.split(",");
    return recipients

def getEmailsFromFile():
    return getEmailInformation(getEmailsRawFromFile())

def getEmailsRawFromFile():
    myfile = open("app/Email_Adresses.csv", 'r')
    return myfile.read()

def saveEmails(csv):
    #validate email adresses 
    recipients = getEmailInformation(csv)
    for i in recipients:
        try:
            validate_email(i)
        except Exception:
            return False
    myfile = open("app/Email_Adresses.csv", 'w')
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
    message = formatMessage()
    recipients = getEmailsFromFile()
    

    ##send email Need to add information about email you are sending it from here
    my_host = 'smtp.gmail.com'
    my_port = 587
    my_username = '@gmail.com'
    my_password = ''
    my_use_tls = True 
    print "Hello World"
    ##Creates connection to the mail server
    connection = get_connection(host=my_host, port=my_port, username=my_username, password=my_password, use_tls=my_use_tls) 

    ##Send the email to the array/list of Email recipients
    try:
        send_mail('Survey', message, my_username, recipients, connection = connection)
    except Exception:
        print "Message failed to send"

