from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
import simplejson

from .forms import *
from .models import *
from products.models import *
from orders.models import *
from .serializers import *

from rest_framework import viewsets
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_protect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework import generics

import qrcode


class UserViewSet(generics.ListCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

def reg(request):
    registrationForm = RegistForm(request.POST or None)

    if (registrationForm.is_valid()):
        registrationForm.save()
        login = registrationForm.cleaned_data['login']
        request.session['login'] = login
        return HttpResponseRedirect('../')

    return render(request, 'auth_reg/index.html', locals())


def main(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    if request.session.get('login', False):
        auth = request.session['login']
        context['auth'] = auth

    return render(request, 'auth_reg/main.html', context)


def auth(request):
    authorizationForm = AuthForm(request.POST or None)

    if request.POST and authorizationForm.is_valid():
        login = authorizationForm.cleaned_data['login']
        password = authorizationForm.cleaned_data['password']
        try:
            user = User.objects.get(login=login, password=password)
            request.session['login'] = login
            return HttpResponseRedirect('../')
        except ObjectDoesNotExist:
            print('DoesNotExist')
    return render(request, 'auth_reg/auth.html', locals())


def logout(request):
    try:
        del request.session['login']
    except:
        pass
    return HttpResponseRedirect('../')


def products(request, id):
    weapons = ProductImage.objects.all().filter(product__category__id=id, main=True)
    name = Category.objects.all().get(id=id)
    surname = Category.objects
    if request.session.has_key('login'):
        auth = request.session['login']
        return render(request, 'auth_reg/products.html', locals())
    else:
        print('Not Auth')
    return render(request, 'auth_reg/products.html', locals())


def basket(request):
    orders = ProductInOrder.objects.all().filter(order__status='n')
    if len(orders) != 0:
        total_price = orders[0].order.total_price
        if request.session.has_key('login'):
            auth = request.session['login']
            return render(request, 'auth_reg/basket.html', locals())
        else:
            print('Not Auth')
    return render(request, 'auth_reg/basket.html', locals())


@csrf_protect
def buy(request):
    product_id = request.POST.get('id', 'b')
    amount = request.POST.get('amount', None)
    json = {}
    if request.method == 'POST':
        product_in_order = ProductInOrder()
        product = Product.objects.get(pk=int(product_id))
        product_in_order.product = product
        # print(len(ProductInOrder.objects.all().filter(order__status='n')))
        if len(ProductInOrder.objects.all().filter(order__status='n')) == 0:
            order = Order.objects.create()
            product_in_order.order = order
            product_in_order.amount = int(amount)
            product_in_order.save()
        else:
            order = Order.objects.all().filter(status='n')
            product_in_order.order = order[0]
            product_in_order.amount = int(amount)
            product_in_order.save()
        json['notification'] = True
    data = simplejson.dumps(json)
    return HttpResponse(data, content_type="application/json")


@csrf_protect
def purchase(request):
    order = Order.objects.get(status='n')
    order.status = 'o'
    order.save()
    return render(request, 'auth_reg/basket.html')


@csrf_protect
def on_change_basket(request):
    count = int(request.POST.get('count', 1))
    id = int(request.POST.get('id', None))
    print(count, id)

    order = ProductInOrder.objects.filter(order__status='n')
    product = order[id]
    product.amount = count
    product.save()
    json = {'total_price': product.order.total_price}
    data = simplejson.dumps(json)
    return HttpResponse(data, content_type='application/json')


def product(request, slug):
    product = ProductImage.objects.get(product__slug=slug, main=True).product
    image = ProductImage.objects.get(product__slug=slug, main=True).image
    images = ProductImage.objects.filter(product__slug=slug)
    print(images)

    form = CommentForm(request.POST or None)

    if request.session.get('login', False):
        auth = request.session['login']
        comments = Comment.objects.filter(comment_product__slug=slug)
        if form.is_valid():
            comment = Comment()
            comment.comment_product = product
            comment.comment_author = User.objects.get(login=auth)
            comment.comment_text = form.cleaned_data['comment_text']
            comment.save()
            return HttpResponseRedirect(product.get_absolute_url())

    return render(request, 'auth_reg/product.html', locals())


def profile(request):
    return render(request, 'auth_reg/profile.html')


def finish(request):
    return render(request, 'auth_reg/finish.html')


def qr(request):
    a = request.GET.get('input', None)
    print(a)
    if a is not None:
        if len(a) != 0:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(a)
            qr.make(fit=True)

            img = qr.make_image(fill_color="black", back_color="white")
            img.save("static/media/img/nurlan.jpg")

    return render(request, "auth_reg/qr_code.html", locals())


def delete_from_basket(request):
    a = int(request.GET.get('id', None))
    order = Order.objects.get(status='n')
    order.get_product()[a].delete()
    print(order)
    if len(order.get_product()) == 0:
        order.delete()
    return HttpResponseRedirect('../basket')
