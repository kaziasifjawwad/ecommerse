from django.urls import path
from .views import *
urlpatterns = [
    path('user', createUser, name='createuser'),
    path('user/addfev/<int:userId>/<int:carId>',addFevMovie,name='addFevMovie'),
    path('user/removefev/<int:userId>/<int:carId>',removeFevMovie,name="removeFevMovie"),
    path('user/getfevcar/<int:id>',SearchFevCar.as_view(),name='searchfevcar'),
    path('user/searchcarbyrange/<int:start>/<int:end>',SearchCarByRange.as_view(),name='searchcarbyrange'),
    path('user/SearchByComplexQuery/<str:name>/<str:brand>',SearchByComplexQuery.as_view(),name='searchcarbyrange')
]