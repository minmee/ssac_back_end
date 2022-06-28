import sys
sys.path.append('home/ubuntu/ssac_final/ssac_final/TTS/')
from users.models import User # Django Build in User Model
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from chats.models import Message # Our Message model
from chats.serializers import MessageSerializer # Our Serializer Classes
from TTS.bots.kobart_chatbot import kobart_chatbot
from TTS import main

# Users View
@csrf_exempt
def message_list(request, sender=None, receiver=None):
    """
    List all required messages, or create a new message.
    """
    if request.method == 'GET':
        messages = Message.objects.filter(sender_id=sender, receiver_id=receiver)
        serializer = MessageSerializer(messages, many=True, context={'request': request})
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MessageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            msg = main.stt_gen(data['message'])
            Message.objects.create(message=msg,sender_id=2, receiver_id=1)
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
