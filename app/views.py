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
        all_patient = Patient.objects.all()

        return render(request, "home.html", locals())
    return render(request,  template_name='home.html')


def patient_detail(request, pk):
    try:
        patient = Patient.objects.get(pk=pk)
    except Patient.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    survey_from_this_patient = Survey.objects.filter(author=patient.user_name)

    return render(request, "detail.html", {})


@api_view(['GET', 'POST'])
def user_check(request, pk=None):
    try:
        user = Patient.objects.get(pk=pk)
    except Patient.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        user_serializer = PatientSerializer(user)
        return Response(user_serializer.data)

# @csrf_exempt
# def survey_detail(request):
#
#     if request.method == 'POST':
#         survey_serializer = SurveySerializer(data=request.data)
#         if survey_serializer.is_valid():
#             survey_serializer.save()
#             return Response(survey_serializer.data, status=status.HTTP_201_CREATED)
#         return Response(survey_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'GET':
#         all_surveys = Survey.objects.all()
#         serializer = SurveySerializer(all_surveys, many=True)
#         return Response(serializer.data)

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
        print(data)
        serializer = SurveySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)
