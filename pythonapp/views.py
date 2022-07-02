from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from pythonapp.forms import DoctorRegister

# Create your views here.


@csrf_exempt
def login_view(request):
    if request.method=='POST':
        username=request.POST.get('uname')
        password=request.POST.get('pass')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if user.is_staff:
                type='staff'
                result=user.is_authenticated
    try:
        result=user.is_authenticated
        data={
            'status':True,
            'result':{
                'id':user.username,
                'email':user.email,
                'type':type
            }
        }
    except:
        data={
            'status':False
        }
    return JsonResponse(data,safe=False)



@csrf_exempt
def doc_reg(request):
    result_data = None
    if request.method == 'POST':
        form = DoctorRegister(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.is_active = True
            form.is_doctor = True
            form.save()
            result_data = True
    try:
        if result_data:
            data = {'result': True}
        else:
            print(list(form.errors))
            errors_data = form.errors
            error_dict = {}
            for i in list(form.errors):
                error_dict[i] = errors_data[i][0]

            data = {
                'result': False,
                'errors': error_dict
            }
    except:
        data = {
            'result': False

        }
    return JsonResponse(data, safe=False)
