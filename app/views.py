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

    return render(request, "detail.html", {'surveys': survey_from_this_patient})


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
