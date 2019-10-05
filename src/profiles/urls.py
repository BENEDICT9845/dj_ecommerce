from django.urls import path

from .views import (
    profile_list_view,
    profile_detail_view,
    profile_create_view,
    profile_update_view,
    profile_create_experience_view,
    profile_experience_list_view,
    profile_experience_update_view,
    profile_experience_delete_view,
    profile_create_education_view,
    profile_education_list_view,
    profile_education_update_view,
    profile_education_delete_view
)

app_name = 'profiles'
urlpatterns = [
    path(
        '',
        profile_list_view,
        name='profile_list'
    ),
    path(
        'create/',
        profile_create_view,
        name='profile_create'
    ),
    path(
        '<int:pk>/detail/',
        profile_detail_view,
        name='profile_detail'
    ),
    path(
        '<int:pk>/update/',
        profile_update_view,
        name='profile_update'
    ),
    path(
        '<int:pk>/experiences/',
        profile_experience_list_view,
        name='profile_experience_list'
    ),
    path(
        '<int:pk>/educations/',
        profile_education_list_view,
        name='profile_education_list'
    ),
    path(
        '<int:pk>/experiences/create/',
        profile_create_experience_view,
        name='profile_create_experience'
    ),
    path(
        'experiences/<int:pk>/update/',
        profile_experience_update_view,
        name='profile_experience_update'
    ),
    path(
        'experiences/<int:pk>/delete/',
        profile_experience_delete_view,
        name='profile_experience_delete'
    ),
    path(
        '<int:pk>/educations/create/',
        profile_create_education_view,
        name='profile_create_education'
    ),
    path(
        'educations/<int:pk>/update/',
        profile_education_update_view,
        name='profile_education_update'
    ),
    path(
        'educations/<int:pk>/delete/',
        profile_education_delete_view,
        name='profile_education_delete'
    ),
]
