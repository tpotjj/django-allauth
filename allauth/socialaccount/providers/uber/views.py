from allauth.socialaccount.adapter import get_adapter
from allauth.socialaccount.providers.oauth2.views import (
    OAuth2Adapter,
    OAuth2CallbackView,
    OAuth2LoginView,
)


class UberOAuth2Adapter(OAuth2Adapter):
    provider_id = "uber_oauth2"
    access_token_url = "https://login.uber.com/oauth/v2/token"
    authorize_url = "https://login.uber.com/oauth/v2/authorize"
    profile_url = "https://api.uber.com/v1/me"
    basic_auth = True


oauth2_login = OAuth2LoginView.adapter_view(UberOAuth2Adapter)
oauth2_callback = OAuth2CallbackView.adapter_view(UberOAuth2Adapter)
