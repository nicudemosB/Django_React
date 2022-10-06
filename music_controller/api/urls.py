from django.urls import path
from .views import main
# //if we get a url that is blank then call the main function and fdo what it says in the main function 
urlpatterns = [
    path('home', main),
    path('', main)
]
    