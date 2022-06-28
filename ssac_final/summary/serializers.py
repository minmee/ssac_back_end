from users.models import User
from rest_framework import serializers
from summary.models import Summary


# User Serializer
class SummarySerializer(serializers.ModelSerializer) :
    """ For Serializing User """
    summary = serializers.CharField(max_length=1200)
    timestamp = serializers.DateTimeField()
    class Meta:
        model = Summary
        fields = [ 'summary', 'timestamp']
        
