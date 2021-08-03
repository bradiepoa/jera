from django.shortcuts import render

# Create your views here.

def Home_view(request):
	return render(request, 'shop/index.html')

def Pay_view(request):
	return render(request, 'shop/payement.html')

def Contact_view(request):
	return render(request, 'shop/contact.html')

def Details(request):
	return render(request, 'shop/details.html')