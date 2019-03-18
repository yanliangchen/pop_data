from django.contrib import admin
from django.urls import path,include
from  . import  views
from .views import Index,SpeedDisplay
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('test/', views.test, name="test"),
    path('', Index.as_view()),
    path('network/speed/', SpeedDisplay.as_view(), name="speed_display"),
]
# app_name = 'pop_data'