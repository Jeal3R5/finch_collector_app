from django.contrib import admin
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
    # new route used to show a form and create a germ
    path('germs/create/', views.GermCreate.as_view(), name='germs_create'),
    # New routes used to update and delete a germ
    path('germs/<int:pk>/update/', views.GermUpdate.as_view(), name='germs_update'),
    path('germs/<int:pk>/delete/', views.GermDelete.as_view(), name='germs_delete'),
    path('germs/<int:germ_id>/add_treatment/', views.add_treatment, name='add_treatment'),
    path('symptoms/', views.SymptomList.as_view(), name='symptoms_index'),
    path('symptoms/<int:pk>/', views.SymptomDetail.as_view(), name="symptoms_detail"),
    path('symptoms/create/', views.SymptomCreate.as_view(), name="symptoms_create"),
    path('symptoms/<int:pk>/update/', views.SymptomUpdate.as_view(), name="symptoms_update"),
    path('symptoms/<int:pk>/delete/', views.SymptomDelete.as_view(), name='symptoms_delete'),
    path('account/signup/', views.signup, name='signup'),
]