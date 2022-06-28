from django.urls import path
from . import views
urlpatterns = [
    # URL form : "/api/messages/1/2"
    # path('summary/<int:sender>/<int:receiver>', views.summary_list, name='summary-detail'),  # For GET request.
    # URL form : "/api/summary/"
    path('summary/', views.summary_list, name='summary-list'),   # For GET
    # URL form "/api/users/1"
    #path('api/v1/users/<int:pk>', views.user_list, name='user-detail'),      # GET request for user with id
    #path('api/v1/users/', views.user_list, name='user-list'),    # POST for new user and GET for all users list
]
