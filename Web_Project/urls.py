from django.contrib import admin
from django.urls import path
from Home_App import views as hv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hv.home, name='home'),
    path('about/', hv.about, name='about'),
    path('order/', hv.order, name='order'),
    path('contact/', hv.contact, name='contact'),
    path('book_table/', hv.book_table, name='book_table'),
    path('show_text/', hv.show_text, name='show_text'),
]
