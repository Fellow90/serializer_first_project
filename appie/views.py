#function based api view , it doesnot need third party app
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views import View
from rest_framework import status
from django.http import HttpResponse

from appie.models import Student
from appie.serializers import StudentSerializer
@api_view(['GET','POST','PUT','PATCH','DELETE'])
def student_api(request,pk=None):
    if request.method == 'GET':
        #for browsable api
        id = pk        
        # id = request.data.get('id')
        # id = request.query_params.get('id')

        if id is not None:
            stu = Student.objects.get(id= id)

            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu,many = True)       
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created Successfully.'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PUT':
        id = pk
        # id = request.data.get('id')

        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu,data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data updated'},status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

    if request.method == 'PATCH':
        id = pk
        # id = request.data.get('id')
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu,data=request.data,partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data updated'},status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        id = pk
        # id = request.data.get('id')
        stu = Student.objects.get(id = id)
        stu.delete()
        return Response("Data deleted",status=status.HTTP_200_OK)
            


 





















#FUNCTION AND CLASS BASED VIEW --- needs third party app which is in project directory--myapp.py
'''from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View

from appie.models import Student
from appie.serializers import StudentSerializer

# Create your views here.
## for class based view
@method_decorator(csrf_exempt,name = 'dispatch')
class StudentAPI(View):
    def get(self,request,*args,**kwargs):
        json_data  = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id',None)

        if id is not None:
            stu = Student.objects.get(id= id)
            serializer = StudentSerializer(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type = 'application/json')
            # response = {
            #     'msg':'data accessed of individual',
            # }
            # return JsonResponse(response)

        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many = True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')
        # response = {
        #         'msg':'data accessed of all',
        # }
        # return JsonResponse()
    
    def post(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data = pythondata)
        if serializer.is_valid():
            serializer.save()

            response = {'msg':'Data Created'}
            json_data = JSONRenderer().render(response)
            return HttpResponse(json_data,content_type = 'application/json')
        else:
            print(serializer.errors)
            # return JsonResponse(response)
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type = 'application/json')
        # return JsonResponse(serializer.errors)





    def put(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id = id)
        serializer = StudentSerializer(stu,data = pythondata, partial = True)
        #if complete update, all data should be passed, and for partial update,    partial = True should be passed 
        if serializer.is_valid():
            serializer.save()
            res = {
                'msg':'Data updated',
            }
            # json_data = JSONRenderer().render(res)
            # return HttpResponse(json_data,content_type = 'application/json')
            return JsonResponse(res)
        
        # json_data = JSONRenderer().render(serializer.errors)
        # return HttpResponse(json_data,content_type = 'application/json')
        return JsonResponse(serializer.errors)
    

    def delete(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id = id)
        stu.delete()
        res = {
            'msg':'Data deleted',
        }
        # json_data = JSONRenderer().render(res)
        # return HttpResponse(json_data,content_type = 'application/json')

        return JsonResponse(res,safe=False)



### class based view ends here , all other process are same
'''
'''
#for function based view
# get single student data, approach to serialization
def student_detail(request,pk):
    stu= Student.objects.get(id=pk)
    serializer= StudentSerializer(stu)
    print(serializer)
    data = serializer.data
    # json_data = JSONRenderer().render(data)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(data)

# get all student data
def student_list(request):
    stu= Student.objects.all()
    serializer= StudentSerializer(stu , many = True)
    data = serializer.data
    # json_data = JSONRenderer().render(data)
    # return HttpResponse(json_data,content_type='application/json')
    return JsonResponse(data, safe=False)


#for creating student or posting from the client , an approach to deserialization
@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data  = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Created'}
            # json_data = JSONRenderer().render(res)
            # return HttpResponse(json_data , content_type = 'application/json')
            return JsonResponse(serializer.data )
        

        # json_data = JSONRenderer().render(serializer._errors)
        # return HttpResponse(json_data , content_type = 'application/json')
        return JsonResponse(serializer.errors)

## getting data from client and posting it to database
@csrf_exempt
def student_api(request):
    if request.method == 'GET':
        json_data  = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id',None)

        if id is not None:
            stu = Student.objects.get(id= id)
            serializer = StudentSerializer(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type = 'application/json')
            # response = {
            #     'msg':'data accessed of individual',
            # }
            # return JsonResponse(response)

        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many = True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')
        # response = {
        #         'msg':'data accessed of all',
        # }
        # return JsonResponse()

    if request.method =='POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data = pythondata)
        if serializer.is_valid():
            serializer.save()
            response = {'msg':'Data Created'}
            # json_data = JSONRenderer().render(response)
            # return HttpResponse(json_data,content_type = 'application/json')
            return JsonResponse(response)
        # json_data = JSONRenderer().render(serializer.errors)
        # return HttpResponse(json_data,content_type = 'application/json')
        return JsonResponse(serializer.errors)

    if request.method == "PUT":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id = id)
        serializer = StudentSerializer(stu,data = pythondata, partial = True)
        #if complete update, all data should be passed, and for partial update,    partial = True should be passed 
        if serializer.is_valid():
            serializer.save()
            res = {
                'msg':'Data updated',
            }
            # json_data = JSONRenderer().render(res)
            # return HttpResponse(json_data,content_type = 'application/json')
            return JsonResponse(res)
        
        # json_data = JSONRenderer().render(serializer.errors)
        # return HttpResponse(json_data,content_type = 'application/json')
        return JsonResponse(serializer.errors)
    
    if request.method == "DELETE":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id = id)
        stu.delete()
        res = {
            'msg':'Data deleted',
        }
        # json_data = JSONRenderer().render(res)
        # return HttpResponse(json_data,content_type = 'application/json')

        return JsonResponse(res,safe=False)'''