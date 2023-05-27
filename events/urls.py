from django.urls import path
from .views import *
urlpatterns = [
    path('', event_list, name='Event_List'),
    path('event/<str:id>/', event_details, name='Event_Details'),
    path('create_event/', create_event, name='Create_Event'),
    path('event/delete/<str:id>', delete_event, name='Delete_Event'),
    path('event/edit/<str:id>',edit_event, name='Edit_Event')
]