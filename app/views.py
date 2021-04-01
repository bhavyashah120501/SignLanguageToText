from django.shortcuts import render
import json
import base64
from rest_framework.decorators import permission_classes
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework import status
# Create your views here.

@api_view(['POST'])
def textToAsl(request):
    if request.method == 'POST':
        text = request.data['text']  #Extracting text
        print(text)
        arr = text.split()
        data = {}
        count = 0       #number of ele in dict
        for i in range(0,len(arr)):
            nesteddata = {}
            flag = 0                #flag to avoid empty nested dict
            for j in range(0,len(arr[i])):
                asci = ord(arr[i][j])
                if asci <=90 and asci >=65:           #converting to lower case
                    asci = asci + 32
                if  asci>= 97 and asci <=122: 
                    flag = 1
                    alphabet = chr(asci)       
                    with open('./split/'+alphabet+'.png', mode='rb') as file:
                        byte_img = file.read()

                    base64_bytes = base64.b64encode(byte_img)       #in byte base64 format
                    nesteddata[j] = base64_bytes.decode('utf-8')   #converting to string format
            if flag ==1:
                data[count] = nesteddata     #main dict
                count += 1
        print(json.dumps(data))          #conv to json
        return Response(json.dumps(data), status=200)


