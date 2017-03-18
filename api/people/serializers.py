from rest_framework import serializers
from restapp.models import Person

class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = ('id', 'name', 'favorite_city')
