from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from myday.models import product
from django.urls import reverse


# =========================
# HOME
# =========================

def home(request):

    return render(request, 'home.html')


# =========================
# CREATE
# =========================

def newProductForm(request):

    return render(request, 'newProductForm.html')


def saveuser(request):

    p_name = request.POST['p_name']
    p_price = request.POST['p_price']
    p_offer = request.POST['p_offer']

    pro = product(
        p_name=p_name,
        p_price=p_price,
        p_offer=p_offer
    )

    pro.save()

    url = reverse('Productlist')

    return HttpResponseRedirect(url)


# =========================
# READ
# =========================

def Productlist(request):

    Products = product.objects.all()

    return render(
        request,
        'productlist.html',
        {'Products': Products}
    )


# =========================
# UPDATE FORM
# =========================

def updateProductForm(request):

    id = request.GET.get('id')

    productdata = product.objects.filter(id=id).values()

    return render(
        request,
        'updateProductForm.html',
        {'product': productdata[0]}
    )


# =========================
# UPDATE
# =========================

def updateProduct(request):

    id = request.POST['id']
    p_name = request.POST['p_name']
    p_price = request.POST['p_price']
    p_offer = request.POST['p_offer']

    product.objects.filter(id=id).update(
        p_name=p_name,
        p_price=p_price,
        p_offer=p_offer
    )

    url = reverse('Productlist')

    return HttpResponseRedirect(url)


# =========================
# DELETE
# =========================

def deleteProduct(request):

    id = request.GET.get('id')

    if id:
        product.objects.filter(id=id).delete()

    url = reverse('Productlist')

    return HttpResponseRedirect(url)