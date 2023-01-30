

from rest_framework import serializers


from rest_framework import serializers

from.models import College

from django.contrib.auth.models import User
 
 
class userSerializers(serializers.ModelSerializer):
 
    class Meta:
        model = User
        fields =  '__all__'



class CollegeSerilizer(serializers.ModelSerializer):

    class Meta:
        model=College
        fields='__all__'
