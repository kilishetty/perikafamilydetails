from django.shortcuts import render
from django.http import HttpResponse
from .models import FamilyDetails

# Create your views here.

def home(request):
    return render(request, 'base.html', {'name' : 'Nagaraj'})

def family(request):
    val1 = request.POST['hno']
    val2 = request.POST['mobileno']
    val3 = request.POST['ownername']
    val4 = request.POST['uscno']
    val5 = request.POST['age']
    val6 = request.POST['occupation']
    val7 = request.POST['fathername']
    val8 = request.POST['mothername']

    val9 = request.POST['child1name']
    val10 = request.POST['child1age']
    val11 = request.POST['child1education']

    val12 = request.POST['child2name']
    val13 = request.POST['child2age']
    val14 = request.POST['child2education']

    val15 = request.POST['child3name']
    val16 = request.POST['child3age']
    val17 = request.POST['child3education']

    val18 = request.POST['village']
    val19 = request.POST['mandal']
    val20 = request.POST['district']
    val21 = request.POST['state']

    family_details = FamilyDetails(hno=val1, mobileno=val2, ownername=val3, uscno=val4, age=val5, occupation=val6, fathername=val7, mothername=val8, child1name=val9, child1age=val10, child1education=val11, child2name=val12, child2age=val13, child2education=val14, child3name=val15, child3age=val16, child3education=val17, village=val18, Mandal=val19, District=val20, State=val21) 
    family_details.save()
    return render(request, 'result.html', {'hno':val1, 'mobileno':val2, 'ownername':val3, 'uscno':val4, 'age':val5, 'occupation':val6, 'fathername':val7, 'mothername':val8, 'child1name':val9, 'child1age':val10, 'child1education':val11, 'child2name':val12, 'child2age':val13, 'child2education':val14, 'child3name':val15, 'child3age':val16, 'child3education':val17, 'village':val18, 'mandal':val19, 'district':val20, 'state':val21})

