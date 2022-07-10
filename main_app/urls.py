from django.urls import path
from . import views

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('about/', views.about, name='about'),
#     path('germs/', views.germs_index, name='germs'),
#     path('germs/<int:germ_id', views.germs_detail, name='detail')
#     # new route used to show a form and create a cat
#    path('germs/create/', views.GermCreate.as_view(), name='germs_create'),
#    path('germs/<int:germ_id>/update/', views.GermUpdate.as_view(), name="germ_update"),
#    path('germs/<int:germ_id>/delete', views.GermDelete.as_view(), name="germs_delete")
# ]
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('germs/', views.germs_index, name='germs'), 
    path('germs/<int:germ_id>/', views.germs_detail, name='detail'),
    # new route used to show a form and create a cat
]