from django.urls import path

from api import views as v

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path(
        'forums/',
        v.ForumListView.as_view(),
        name='forum-list'
    ),

    # --- Auth data ---
    path(
        'auth/login/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair',
    ),
    path(
        'auth/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh',
    ),

    path(
        'auth/register/',
        v.RegisterView.as_view(),
        name='register',
    ),
]
