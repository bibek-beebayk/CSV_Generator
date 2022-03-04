from django.urls import path
from . import views

urlpatterns = [
    path('/usertypes/', views.usertype_index, name='usertype.name'),
    path('/usertypes/create', views.usertype_create, name='usertype.create'),
    path('/usertypes/edit/<int:id>', views.usertype_edit, name='usertype.edit'),
    path('/usertypes/store', views.usertype_store, name='usertype.store'),
    path('/usertypes/update', views.usertype_update, name='usertype.update'),
    path('/usertypes/delete/<int:id>', views.usertype_delete, name='usertype.delete'),
    path('/usertypes/show/<int:id>', views.usertype_show, name='usertype.show'),
]