__author__ = 'kyawthan'

from .models import Patient, Survey, SkipSurvey
from rest_framework import serializers


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('user_name',)


class SkipSurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = SkipSurvey
        fields = ('user_name',)


class SurveySerializer(serializers.ModelSerializer):

    class Meta:
        model = Survey
        fields = ('id', 'author', 'question1', 'question2', 'question3', 'question4', 'question5', 'question6',\
                  'question7', 'question8', 'question9', 'question10', 'question11', 'question12','delay_counter', 'created_at',)