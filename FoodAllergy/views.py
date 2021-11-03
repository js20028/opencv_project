from django.shortcuts import render, get_object_or_404, redirect
from .models import Allergy
# Create your views here.


def index(request):
    """
       pybo 목록 출력
    """
    allergy_list = Allergy.objects.order_by()
    context = {'allergy_list': allergy_list}
    return render(request, 'FoodAllergy/allergy_list.html', context)


def detail(request, allergy_id):
    """
    pybo 내용 출력
    """
    allergy = Allergy.objects.get(id=allergy_id)
    context = {'allergy': allergy}
    return render(request, 'FoodAllergy/allergy_detail.html', context)


def allergy_register(request):
    """
    pybo 알러지등록
    """
    #allergy = get_object_or_404(Allergy, pk=allergy_id)
    #allergy.allergyName.create(allergyName=request.POST.get('allergyName'))

    #allergy = Allergy.objects.get()
    #context = {'allergy': allergy}
    #a = Allergy(allergyName=request.POST.get('allergyName'), highLevelAllergy=request.POST.get('highLevelAllergy'),
    #            level=request.POST.get('level'), myAllergy=request.POST.get('myAllergy'))
    #a.save()
    return render(request,'FoodAllergy/allergy_regist.html')

def regist(request):

    highLevelAllergy = request.POST.get('highLevelAllergy')
    if highLevelAllergy == "":
        level = 1
        a = Allergy(allergyName=request.POST.get('allergyName'), highLevelAllergy=highLevelAllergy,
                    level=level, myAllergy="N")
    else:
        level = 2
        a = Allergy(allergyName=highLevelAllergy, highLevelAllergy=request.POST.get('allergyName'),
                    level=level, myAllergy="N")

    a.save()

    return redirect('FoodAllergy:register')