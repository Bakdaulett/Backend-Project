from django.urls import path
from doctors import views


urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search),
    path('search/details/<int:id>', views.details, name='details'),
    path('create_view/', views.create_view),
    path('all/', views.all, name='all'),
    path('<int:id>', views.detail_view),
    path('<int:id>/update', views.update_view, name='update'),
    path('<id>/delete', views.delete_view),
    path('signup', views.signup, name='signup'),
    path('signout', views.signout, name='signout'),
    path('signin', views.signin, name='signin'),

]