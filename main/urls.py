from django.urls import path
from . views import *

urlpatterns = [
    path("", main_page, name = "main_page"),
    path('register/', register_page, name = 'register_page'),
    path('login/', login_page, name = 'login_page'),
    path('logout/', log_out, name='log_out'),
    path('order/<int:id_product>/', make_order, name = 'make_order'),
 ]
