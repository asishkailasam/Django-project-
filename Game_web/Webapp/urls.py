from django.urls import path
from Webapp import views

urlpatterns=[
     path('index/',views.index,name="index"),
     path('webpage/', views.webpage, name="webpage"),

     path('categoryonlyFNurl/<itemcatg>',views.categoryonlyFN,name="categoryonlyFN"),
     path('prodetails/<int:dataid>/', views.prodetails, name="prodetails"),
     path('pro2_page/', views.pro2_page, name="pro2_page"),
     path('datafill_page/', views.datafill_page, name="datafill_page"),
     path('savelogin/', views.savelogin, name='savelogin'),
     path('customerlogin/',views.customerlogin, name='customerlogin'),
     path('contactpage/', views.contactpage, name='contactpage'),
     path('savedata_a/', views.savedata_a, name='savedata_a'),
     path('clogout/',views.clogout, name='clogout')



]