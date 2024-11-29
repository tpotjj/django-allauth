from allauth.socialaccount.providers.oauth2.urls import default_urlpatterns

from .provider import UberOAuth2Provider


urlpatterns = default_urlpatterns(UberOAuth2Provider)