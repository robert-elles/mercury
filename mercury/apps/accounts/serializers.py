from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers

from apps.accounts.models import Invitation, Membership, Site, UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ("info",)


class UserSerializer(UserDetailsSerializer):
    profile = UserProfileSerializer()

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + ("profile",)


class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        read_only_fields = ("id", "created_at", "created_by", "updated_at", "status", "domain")
        fields = (
            "id",
            "created_at",
            "created_by",
            "updated_at",
            "title",
            "slug",
            "share",
            "welcome",
            "active",
            "status",
            "info",
            "domain"
        )


class MembershipSerializer(serializers.ModelSerializer):
    user = UserDetailsSerializer(many=False, read_only=True)

    class Meta:
        model = Membership
        read_only_fields = ("id", "created_at", "created_by", "updated_at")
        fields = read_only_fields + ("rights", "user")


class InvitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invitation
        read_only_fields = ("id", "invited", "created_at", "created_by", "rights")
        fields = read_only_fields
