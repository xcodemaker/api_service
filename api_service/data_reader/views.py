from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json
import requests
from api_service.settings import BASE_DIR


IMPORT_URL = 'http://127.0.0.1:8000'

@api_view(["GET"])
def getState(request):
    try:
        code = request.GET['code']
        # f = open(BASE_DIR+'/json_reader/resources/states_hash.json')
        # json_string = f.read()
        # f.close()
        # data = json.loads(json_string)

        # result = 'No result'

        # for key, value in data.items():
        #     if(key == code):
        #         result = value
        headers = {'Content-Type': 'application/json'}
        response = requests.get(
            url=IMPORT_URL + '/codeToState/?code=' +code,
            headers=headers,
        )

        response.raise_for_status()
        data = response.json()

        return JsonResponse(data,safe=False)
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def getCode(request):
    try:
        state = request.GET['state']
        # f = open(BASE_DIR+'/json_reader/resources/states_titlecase.json')
        # json_string = f.read()
        # f.close()
        # data = json.loads(json_string)

        # result = 'No result'

        # for i in range(len(data)):
        #     if(data[i]['name'] == state):
        #         result = data[i]['abbreviation']
        headers = {'Content-Type': 'application/json'}
        response = requests.get(
            url=IMPORT_URL + '/stateToCode?state=' + state,
            headers=headers,
        )

        response.raise_for_status()
        data = response.json()

        return JsonResponse(data,safe=False)
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)