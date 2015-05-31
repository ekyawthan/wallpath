__author__ = 'kyawthan'

from .models import Patient, Survey
from rest_framework import serializers


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('user_name',)


class SurveySerializer(serializers.ModelSerializer):

    class Meta:
        model = Survey
        fields = ('id', 'author', 'answers', 'choices', 'delay_counter', 'created_at',)