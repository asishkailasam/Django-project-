from django.urls import path
from Myapp import views

urlpatterns = [
    path('index/',views.index,name='index'),
    path('indexpage/', views.indexpage, name="indexpage"),
    path('adminpage/',views.adminpage,name="adminpage"),
    path('displaypage/',views.displaypage,name="displaypage"),
    path(' adminpage_save/',views. adminpage_save,name="adminpage_save"),
    path(' editpage/',views.editpage,name="editpage"),
    path(' deletedata/<int:dataid>/', views.deletedata, name="deletedata"),
    path('cat_page/',views.cat_page,name="cat_page"),
    path('cat_save/',views.cat_save,name="cat_save"),
    path('category_display/',views.category_display,name="category_display"),
    path('pro_page/',views.pro_page,name="pro_page"),
    path('pro_save/',views.pro_save,name="pro_save"),
    path('pro_display/',views.pro_display,name="pro_display"),
    path('delete_cat/<int:dataid>/', views.delete_cat, name="delete_cat"),
    path('delete_pro/<int:dataid>/',views.delete_pro,name="delete_pro"),
    path('update_2data/<int:dataid>/',views.update_2data,name="update_2data"),
    path('editcat_page1/<int:dataid>/',views.editcat_page1,name="editcat_page1"),
    path('signpage/',views.signpage,name="signpage"),
    path('adminlogin/', views.adminlogin, name="adminlogin"),
    path('edit_pro/<int:dataid>/',views.edit_pro, name="edit_pro"),
    path('updateproduct/<int:dataid>/',views.updateproduct,name="updateproduct"),
    path('edit_ad/<int:dataid>/',views.edit_ad,name="edit_ad"),
    path('update_1data/<int:dataid>/',views.update_1data,name="update_1data"),
    path('acontactpage/',views.acontactpage, name='acontactpage'),
    path('deletecontactdata/<int:dataid>/',views.deletecontactdata,name='deletecontactdata'),
    path('customerlogout/',views.customerlogout, name='customerlogout')







]