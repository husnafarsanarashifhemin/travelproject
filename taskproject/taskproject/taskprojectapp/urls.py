from . import views
from django.urls import path

urlpatterns = [
    path('',views.demo,name='demo'),
    #path('addition/',views.addition,name='addition'),
    #path('subtract/',views.subtract,name='subtract')
    #path('mul/',views.multiplication,name='multiplication'),
    #path('div/',views.division,name='division')
    #path('about/',views.about,name='about'),
    #path('contact/',views.contact,name='contact'),
    #path('detail/',views.detail,name='detail'),
    #path('thanks/',views.thanks,name='thanks')
    #path('operations/',views.operations,name='operations')

]