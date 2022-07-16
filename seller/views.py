from django.shortcuts import render, redirect
from EcommerceApp.models import Profile
from .models import Category, Products
# Create your views here.
def home(request):
	pObj = Profile.objects.get(user__username=request.user)
	return render(request, 'WelcomeSeller.html', {'data':pObj})

def add_product(request):
	catObjs = Category.objects.all()
	if request.method == 'POST':
		pname = request.POST['pname']
		price = request.POST['price']
		qty = request.POST['qty']
		desc = request.POST['desc']
		pic = request.FILES['pic']
		cat = request.POST['category']
		catObj = Category.objects.get(id=cat)
		uObj = Profile.objects.get(user__username=request.user)

		p = Products(pname=pname, price=price, qty=qty, desc=desc, pic=pic, added_by=uObj, category=catObj)
		p.save()
		return redirect('/seller/add_product/')

	return render(request, 'add_product.html', {'cats':catObjs})