from django.urls import path, include
from tickets.views import no_rest_no_model, no_rest_from_model, FBV_List, FBV_pk, find_movie, find_reservation, new_reservation
from tickets import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('guests', views.viewsets_guest)
router.register('movies', views.viewsets_movie)
router.register('reservations', views.viewsets_reservation)

urlpatterns = [
    path('no_rest_no_model/', no_rest_no_model),
    path('no_rest_from_model/', no_rest_from_model),   
    #3.1 GET POST from rest framework function based view @api_view
    path('rest/fbv/', FBV_List),

    #3.2 GET PUT DELETE from rest framework function based view @api_view
    path('rest/fbv/<int:pk>', FBV_pk),

    #7 Viewsets
    path('rest/viewsets/', include(router.urls)),

    #8 find movie 
    path('fbv/findmovie/', find_movie),

    #8 find reservation
    path('fbv/findreservation/', find_reservation),

     #10 new reservation
    path('fbv/newreservation/',new_reservation),
]
