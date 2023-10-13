from django.urls import path
import author.views as views

app_name = 'author'

urlpatterns = [
        path('', views.get_all, name='all_author'),
#     path("create/", views.create_author, name="create_author"),
#     path('author/<int:id>/', views.author_id, name='author_by_id_url'),
#     path("delete/<int:id>/", views.delete_author, name="delete_author"),
#
    ]
