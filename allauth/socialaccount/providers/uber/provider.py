from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider
from allauth.socialaccount.providers.twitter_oauth2.views import (
    TwitterOAuth2Adapter,
)


class UberOAuth2Account(ProviderAccount):
    pass


class UberOAuth2Provider(OAuth2Provider):
    id = "uber_oauth2"
    name = "Uber"
    account_class = UberOAuth2Account
    oauth2_adapter_class = TwitterOAuth2Adapter

    def extract_uid(self, data):
        return data["id"]

    def extract_common_fields(self, data):
        return dict(
            name=data["name"],
            username=data["username"],
        )

    def get_fields(self):
        settings = self.get_settings()
        default_fields = [
            "id",
            "name",
            "username",
            "verified",
            "profile_image_url",
            "created_at",
        ]
        return settings.get("FIELDS", default_fields)

    def get_default_scope(self):
        return ["users.read", "tweet.read"]


provider_classes = [UberOAuth2Provider]
