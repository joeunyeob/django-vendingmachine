from django.shortcuts import redirect
from django.core.paginator import Paginator
from twilio.rest import Client

from .models import BeverageList
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render


@login_required
def index(request):
    beverages_list = BeverageList.objects.all()

    paginator = Paginator(beverages_list, 7)

    page = request.GET.get('page')

    beverages_list = paginator.get_page(page)

    return render(request, '../templates/VendingMachine/index.html', {'beverages_list': beverages_list})


def create(request):
    beverages_create = BeverageList(title=request.POST.get['title'], photo=request.POST.get['photo'],
                                    price=request.POST.get['price'], count=request.POST.get['count'])
    beverages_create.save()

    return render(request, '../templates/VendingMachine/create.html', {'beverages_create': beverages_create})


@user_passes_test(lambda u: u.is_superuser)
def edit(request, id):
    beverages = BeverageList.objects.get(id=id)
    context = {'beverages': beverages}
    return render(request, '../templates/VendingMachine/edit.html', context)


@user_passes_test(lambda u: u.is_superuser)
def update(request, id):
    beverages = BeverageList.objects.get(id=id)
    beverages.title = request.POST['title']
    beverages.price = request.POST['price']
    beverages.count = request.POST['count']

    beverages.save()
    return redirect('/VendingMachine/')


@user_passes_test(lambda u: u.is_superuser)
def delete(request, id):
    beverages = BeverageList.objects.get(id=id)
    beverages.delete()
    return redirect('/VendingMachine/')


def buy(request, id, count):
    beverages = BeverageList.objects.get(id=id)

    int_count = int(count)

    beverages.count = beverages.count - int_count

    # 문자 푸시 부분
    # if 0 <= beverages.count <= 10:
    #     account_sid =   # apikey 부분삭제
    #     auth_token =      # apikey 부분삭제
    #     client = Client(account_sid, auth_token)
    #
    #     client.messages.create(
    #         to=      # 개인전화번호 부분 삭제
    #         from_= # twilio에서 발급받은 미국 전화번호부분 삭제
    #         body=beverages.title + '의 수량이 10개 이하입니다. 현재수량은' + str(beverages.count) + '개 입니다.'
    #     )

    total = beverages.price * int_count
    value = {'value': total}

    if beverages.count >= 0:
        beverages.save()
        return render(request, '../templates/VendingMachine/buy_done.html', value)
    else:
        return render(request, '../templates/VendingMachine/buy_fail.html')


@user_passes_test(lambda u: u.is_superuser)  # 슈퍼유저(관리자인지 확인)
def get_data(request):
    labels = BeverageList.objects.all()
    values = BeverageList.objects.all()

    return render(request, '../templates/VendingMachine/charts.html', {'labels': labels, 'values': values})




