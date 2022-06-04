from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, HttpResponse
from .models import Member
from .serializer import MemberSerializer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    if request.method == 'GET':
        members = Member.objects.all()
        serializer = MemberSerializer(members, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        body = request.body
        file = request.FILES['image']
        print("-------")
        # print(file)
        # print(name)

        mokhlesurr031@gmail.com
