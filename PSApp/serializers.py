from rest_framework import serializers
from rest_framework import contests

class contestsSerializer(serializers.ModelSerializer):
    class Meta:
        model=contests
        #fields=()
        fields="__all__"

