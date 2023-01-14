

from rest_framework import serializers


from rest_framework import serializers

from.models import College



class CollegeSerilizer(serializers.ModelSerializer):

    class Meta:
        model=College
        fields='__all__'
