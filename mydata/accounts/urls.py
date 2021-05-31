from . import views
from django.urls import path
urlpatterns = [
    path('', views.welcome),
    path('signup/', views.signup, name='signup'),
    path('loadform/', views.load_form),
    path('add', views.add),
    path('show/', views.show),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.delete),
    path('search', views.search)
]

