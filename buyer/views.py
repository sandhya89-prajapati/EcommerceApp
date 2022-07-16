from django.shortcuts import render, redirect
from seller.models import Products, Category
from .models import Cart
from django.http import HttpResponse
from EcommerceApp.models import Profile
from django.db import connection
# Create your views here.

def home(request):

	p = Profile.objects.get(user__username=request.user)
	myCursor = connection.cursor()
	myCursor.execute('select count(*) from buyer_cart where user_id={}'.format(p.id))
	res = myCursor.fetchone()
	pObjs = Products.objects.all()
	catObjs = Category.objects.all()
	return render(request, 'WelcomeBuyer.html', {'data':pObjs, 'cdata':catObjs, 'count':res[0]})

def cart(request, id):
	pObj = Products.objects.get(id=id)
	uObj = Profile.objects.get(user__username=request.user)
	url = '/buyer/home/'
	try:
		c = Cart(user=uObj, product=pObj)
		c.save()
	except:
		return HttpResponse('<script>alert("Product is already added in your cart");\
			window.location="%s"</script>'%url)

	return HttpResponse('<script>alert("Product has been added in your cart");\
			window.location="%s"</script>'%url)
	return redirect('/buyer/home/')

def cartdetails(request):
	pObj = Profile.objects.get(user__username=request.user)
	cartObjs = Cart.objects.filter(user_id=pObj.id)
	proItems = []
	for i in cartObjs:
		proItems.append(Products.objects.get(id=i.product_id))
	return render(request, 'CartDetails.html',{'added_product':proItems})

def profile(request):
	if request.method == 'POST':
		nm = request.POST['name']
		mob = request.POST['mobile']
		pincode = request.POST['pincode']
		loc = request.POST['locality']
		add = request.POST['address']
		city = request.POST['city']
		state = request.POST['state']
		landmark = request.POST['landmark']
		uObj = Profile.objects.get(user__username=request.user)
		a = Address(user=uObj, name=nm, mobile=mob, pincode=pincode, locality=loc, address=add, city=city, state=state, landmark=landmark)
		a.save()
		return redirect('/buyer/profile/')

	return render(request, 'BuyerProfile.html')

def cartcalculate(request):
	q = request.POST.getlist('productqty')
	price = request.POST.getlist('price')
	pid = request.POST.getlist('pid')
	pObj = Profile.objects.get(user__username=request.user)
	sum = 0
	for i in range(len(q)):
		sum = sum + int(q[i])*float(price[i])
	
		#Update Stock
		updatePro = Products.objects.filter(id=pid[i])
		updatedQty = updatePro[0].qty - int(q[i])
		updatePro.update(qty=updatedQty)
	cartObjs = Cart.objects.filter(user_id=pObj.id)
	cartObjs.delete()


	return redirect('/buyer/cartdetails/')