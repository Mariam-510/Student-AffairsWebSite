from django.urls import path
from . import views
urlpatterns = [
    path('', views.HomePage, name='HomePage'),
    path('Student Affairs', views.StudentAffairs, name='StudentAffairs'),
    path('Login', views.Login, name='LoginStudent'),
    path('Logout', views.Logout, name='Logout'),
    path('Register', views.Register, name='Register'),
    path('Add', views.AddStudent, name='AddStudent'),
    path('Edit', views.EditStudent, name='EditStudent'),
    path('Department', views.Department, name='DepartmentStudent'),
    path('Search', views.Search, name='SearchStudent'),
    path('Status', views.Status, name='StatusStudent'),
    path('DeletePage', views.DeletePage, name='DeletePage'),
    path('update/<int:id>', views.update, name='update'),
    path('update2/<int:id>', views.update2, name='update2'),
    path('depUpdate/<int:id>', views.depUpdate, name='depUpdate'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('delete2/<int:id>', views.delete2, name='delete2'),
    path('staUpdate/<int:id>', views.staUpdate, name='staUpdate'),
]
