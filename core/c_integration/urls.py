
from django.contrib import admin
from django.urls import path  , include
# from rest_framework_jwt.views import obtain_jwt_token
# from rest_framework_jwt.views import verify_jwt_token
# from rest_framework_jwt.views import refresh_jwt_token



urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls') ),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('', include('c_integration_app.api.urls')),
    

    # path('api-token-auth/', obtain_jwt_token),
    # path('api-token-refresh/', refresh_jwt_token),
    # path('api-token-verify/', verify_jwt_token),

]


# 