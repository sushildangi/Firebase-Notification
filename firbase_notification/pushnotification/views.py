import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from fcm.utils import FCMMessage


def index(request):
    return render(request, 'pushnotification/push_form.html', {})


def pushCategory(request):
    return render(request, 'pushnotification/push_form_cat.html', {})


def sendData(request):
    if request.method == 'POST':
        message_text = request.POST.get('message_text')
        message_label = request.POST.get('message_lable')
        title = request.POST.get('title')
        notification_type = request.POST.get('notification_type')
        image = request.POST.get('image')
        message = request.POST.get('message')
        url_product = request.POST.get('url_product')
        unit_price = request.POST.get('unit_price')

        d = {'data': {'title': title, 'is_background': False, 'message': message, 'image': image,
                      'payload': {'notification': notification_type, 'url_product': url_product,
                                  'unit_price': unit_price}, 'timestamp': str(datetime.datetime.now())}}
        res =FCMMessage().send(d, to='/topics/global')

        return render(request, 'pushnotification/thanks.html', {"res": res, })


def sendDataCat(request):
    if request.method == 'POST':
        message_text = request.POST.get('message_text')
        message_label = request.POST.get('message_lable')
        title = request.POST.get('title')
        notification_type = request.POST.get('notification_type')
        image = request.POST.get('image')
        message = request.POST.get('message')
        slug = request.POST.get('slug')

        d = {'data': {'title': title, 'is_background': False, 'message': message, 'image': image,
                      'payload': {'notification': notification_type, 'slug': slug},
                      'timestamp': str(datetime.datetime.now())}}
        res = FCMMessage().send(d, to='/topics/global')

        return render(request, 'pushnotification/thanks.html', {"res": res, })

def thanksMethod(request):
    return render(request, 'pushnotification/thanks.html', {})


class Test(TemplateView):
    template_name = "pushnotification/push_form.html"
