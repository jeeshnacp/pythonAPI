from django.urls import path

from pythonapp import views

urlpatterns=[
    path('login_view',views.login_view,name='login_view'),
    path('login',views.doc_reg,name='login')
]