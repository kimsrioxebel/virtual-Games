from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='My_index',),
    path('about/',views.about, name='My_about'),
    path('product/',views.product, name='My_product'),
    path('video/',views.video, name='My_video'),
    path('remot/',views.remot, name='My_remot'),
    path('contact/',views.contact, name='My_contact')

]