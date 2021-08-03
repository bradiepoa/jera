from django.urls import path
from .import views


App_name='shop'
urlpatterns =[
	path('', views.Home_view,name="homepage"),
	path('payement/', views.Pay_view, name="paymentPage"),
	path('contact/',views.Contact_view, name="contact_page"),
	path('details/',views.Details, name="detailspage")

]