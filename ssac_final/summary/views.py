import sys
sys.path.append('home/ubuntu/ssac_final/ssac_final/TTS/')
from users.models import User # Django Build in User Model
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from summary.models import Summary # Our Message model
from summary.serializers import SummarySerializer # Our Serializer Classes
from TTS import summary_model_infer
# Users View
@csrf_exempt
def summary_list(request, sender=None, receiver=None):
    """
    List all required messages, or create a new message.
    """
    if request.method == 'GET':
        # function ##
        msg = summary_model_infer.summary_result()
        print(msg)
        Summary.objects.create(summary=msg)
        summaries = Summary.objects.all()
        serializer = SummarySerializer(summaries,many =True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SummarySerializer(data=data)
        #msg = []
        if serializer.is_valid():
            serializer.save()
            #print(kobart_chatbot.chat(data['message']))
           
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
