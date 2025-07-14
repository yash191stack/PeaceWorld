from django.urls import path
from . import views
urlpatterns = [

    path("",views.home,name="name"),
    path("dashboard/", views.dashboard, name="dashboard"),  
    path("message/", views.message, name="message"), 
    path("about/", views.about, name="about"), 
    path("contact/", views.about, name="contact"), 
    path("show_message/",views.show_message,name="show_message"),
    path("delete_message/<int:id>",views.delete_message,name="delete_message"),
    path("update_message/<int:id>",views.update,name="update_message")
]
